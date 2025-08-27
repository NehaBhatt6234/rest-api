import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", "items", description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    @jwt_required()
    def get(self, item_id):
        return ItemModel.query.get_or_404(item_id)

    @jwt_required()
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted successfully."}, 200

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    @jwt_required()
    def put(self, item_data, item_id):
        item = ItemModel.query.get_or_404(item_id)
        for key, value in item_data.items():
            setattr(item, key, value)
        db.session.add(item)
        db.session.commit()
        return item


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    @jwt_required()
    def get(self):
        return ItemModel.query.all()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    @jwt_required()
    def post(self, item_data):
        item = ItemModel(id=str(uuid.uuid4()), **item_data)
        db.session.add(item)
        try:
            db.session.commit()
        except IntegrityError:
            abort(400, message="Item with these details already exists.")
        return item
