from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from app.database.models import User


class UserSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
