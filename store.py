from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError
from flask import request

from db import db
from models import StoreModel

blp = Blueprint("Stores", "stores", description="Operations on stores")


@blp.route("/store/<int:store_id>")
class Store(MethodView):
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return {
            "id": store.id,
            "name": store.name,
            "items": [{"id": item.id, "name": item.name, "price": item.price} for item in store.items]
        }

    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted."}


@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        stores = StoreModel.query.all()
        return {
            "stores": [
                {
                    "id": store.id,
                    "name": store.name,
                    "items": [{"id": item.id, "name": item.name, "price": item.price} for item in store.items]
                }
                for store in stores
            ]
        }

    def post(self):
        store_data = request.get_json()

        if "name" not in store_data:
            abort(400, message="Bad request. 'name' field is required.")

        store = StoreModel(name=store_data["name"])
        db.session.add(store)

        try:
            db.session.commit()
        except IntegrityError:
            abort(400, message="A store with that name already exists.")

        return {"id": store.id, "name": store.name}, 201
