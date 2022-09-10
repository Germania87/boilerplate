from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.roles_models import RoleModel


class RolesRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Role Create', {
            'name': fields.String(required=True, max_length=120)
        })

    def update(self):
        return self.namespace.model('Role Update', {
            'name': fields.String(required=True, max_length=120)
        })


class RolesResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RoleModel
        ordered = True

    users = Nested('UsersResponseSchema', exclude=['role'], many=True)
