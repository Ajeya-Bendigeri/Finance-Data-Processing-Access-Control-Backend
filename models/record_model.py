from mongoengine import Document, StringField, DateTimeField, FloatField, ReferenceField, BooleanField
from datetime import datetime
from models.user_model import User


class FinancialRecord(Document):
    user = ReferenceField(User, required=True)

    amount = FloatField(required=True)

    type = StringField(
        required=True,
        choices=["income", "expense"]
    )

    title = StringField(required=True)
    
    description = StringField()

    category = StringField(required=True)

    date = DateTimeField(required=True)

    is_deleted = BooleanField(default=False)

    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'financial_records'
    }