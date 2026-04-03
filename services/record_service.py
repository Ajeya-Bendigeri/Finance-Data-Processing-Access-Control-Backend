from models.user_model import User
from models.record_model import FinancialRecord
from datetime import datetime
from bson import ObjectId

def create_record(data, user_id):
    user = User.objects(id=user_id).first()

    if not user:
        return {"error": "User not found"}, 404

    record = FinancialRecord(
        user=user,
        amount=data["amount"],
        type=data["type"],
        title=data["title"],
        description=data.get("description"),
        category=data["category"],
        date=datetime.strptime(data["date"], "%Y-%m-%d")
    )

    record.save()

    return {"message": "Record created successfully"}, 201


def get_records(filters, user_id, role):
    query = {"is_deleted": False}
    

    if filters.get("type"):
        query["type"] = filters["type"]

    if filters.get("category"):
        query["category"] = filters["category"]

    if filters.get("start_date") and filters.get("end_date"):
        query["date"] = {
            "$gte": datetime.strptime(filters["start_date"], "%Y-%m-%d"),
            "$lte": datetime.strptime(filters["end_date"], "%Y-%m-%d")
        }

    page = int(filters.get("page", 1))
    limit = int(filters.get("limit", 10))
    total = FinancialRecord.objects(__raw__=query).count()

    records = FinancialRecord.objects(__raw__=query) \
        .skip((page - 1) * limit) \
        .limit(limit)

    result = []
    for r in records:
        result.append({
            "id": str(r.id),
            "amount": r.amount,
            "type": r.type,
            "title": r.title,
            "category": r.category,
            "date": r.date.strftime("%Y-%m-%d")
        })

    return {
        "page": page,
        "limit": limit,
        "data": result,
        "total": total
    }, 200


def update_record(record_id, data, user_id, role):
    query = {
        "id": record_id,
        "is_deleted": False
    }

    if role != "admin":
        query["user"] = ObjectId(user_id)

    record = FinancialRecord.objects(**query).first()

    if not record:
        return {"error": "Record not found"}, 404

    record.amount = data.get("amount", record.amount)
    record.type = data.get("type", record.type)
    record.title = data.get("title", record.title)
    record.category = data.get("category", record.category)

    if data.get("date"):
        record.date = datetime.strptime(data["date"], "%Y-%m-%d")

    record.save()

    return {"message": "Record updated successfully"}, 200

def delete_record(record_id, user_id, role):
    query = {
        "id": record_id,
        "is_deleted": False
    }

    if role != "admin":
        query["user"] = ObjectId(user_id)

    record = FinancialRecord.objects(**query).first()

    if not record:
        return {"error": "Record not found"}, 404

    record.is_deleted = True
    record.save()

    return {"message": "Record deleted successfully"}, 200