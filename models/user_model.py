from mongoengine import Document, StringField, EmailField, DateTimeField, BooleanField
from datetime import datetime

class User(Document):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)

    role = StringField(
        required=True,
        choices=["viewer", "analyst", "admin"]
    )

    is_active = BooleanField(default=True)

    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'users'
    }