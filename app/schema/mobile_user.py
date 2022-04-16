import string

import marshmallow_dataclass
from dataclasses import dataclass
from marshmallow_sqlalchemy import auto_field

from app.models import MobileUser
from .init_ma import ma


@dataclass
class MobileUserData:
    id: str


MobileUserSchema = marshmallow_dataclass.class_schema(MobileUserData)

