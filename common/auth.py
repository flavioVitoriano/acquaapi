from passlib.apps import custom_app_context as pwd_context
from models import User
from uuid import uuid4


def hash_password(password):
    return pwd_context.encrypt(password)


def check_passwords(raw, hashed):
    return pwd_context.verify(raw, hashed)


def create_user(**data):
    user = User(**data)
    user.password = hash_password(data["password"])
    user.public_id = str(uuid4())
    user.save()

    return user
