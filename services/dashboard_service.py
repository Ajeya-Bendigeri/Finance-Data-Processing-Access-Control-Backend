from models.record_model import FinancialRecord
from models.user_model import User
from bson import ObjectId
from extensions.cache import redis_client
import json

def get_summary(user_id, role):
    cache_key = f"dashboard_summary:{user_id}"

    cached_data = redis_client.get(cache_key)
    if cached_data:
        return json.loads(cached_data.decode("utf-8")), 200

    query = {"is_deleted": False}

    if role != "admin":
        query["user"] = ObjectId(user_id)

    pipeline = [
        {"$match": query},
        {
            "$group": {
                "_id": "$type",
                "total": {"$sum": "$amount"}
            }
        }
    ]

    result = FinancialRecord.objects.aggregate(*pipeline)

    income = 0
    expense = 0

    for item in result:
        if item["_id"] == "income":
            income = item["total"]
        elif item["_id"] == "expense":
            expense = item["total"]

    response = {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }

    redis_client.setex(cache_key, 60, json.dumps(response))

    return response, 200


def category_breakdown(user_id, role):
    query = {"is_deleted": False}

    if role != "admin":
        query["user"] = ObjectId(user_id)

    pipeline = [
        {"$match": query},
        {
            "$group": {
                "_id": "$category",
                "total": {"$sum": "$amount"}
            }
        }
    ]

    result = FinancialRecord.objects.aggregate(*pipeline)

    return [
        {"category": item["_id"], "total": item["total"]}
        for item in result
    ], 200


def monthly_trends(user_id, role):
    query = {"is_deleted": False}

    if role != "admin":
        query["user"] = ObjectId(user_id)

    pipeline = [
        {"$match": query},
        {
            "$group": {
                "_id": {
                    "year": {"$year": "$date"},
                    "month": {"$month": "$date"},
                    "type": "$type"
                },
                "total": {"$sum": "$amount"}
            }
        },
        {
            "$sort": {
                "_id.year": 1,
                "_id.month": 1
            }
        }
    ]

    result = FinancialRecord.objects.aggregate(*pipeline)

    trends = {}

    for item in result:
        key = f"{item['_id']['year']}-{item['_id']['month']:02d}"

        if key not in trends:
            trends[key] = {"income": 0, "expense": 0}

        trends[key][item["_id"]["type"]] = item["total"]

    return {"trends": trends}, 200


def recent_transactions(user_id, role):
    query = {"is_deleted": False}

    if role != "admin":
        query["user"] = ObjectId(user_id)

    records = FinancialRecord.objects(**query).order_by("-created_at")[:5]

    return [
        {
            "title": r.title,
            "amount": r.amount,
            "type": r.type,
            "date": r.date
        }
        for r in records
    ], 200