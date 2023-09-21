import uuid
import pandas as pd
import pickle
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import processed

blp = Blueprint("preprocessed", __name__, description="Operations on predic")


@blp.route("/preprocessed/")
class Preprocessed(MethodView):
    #@blp.arguments(PredicSchema)
    #@blp.response(201, PredicSchema)
    def post(cls):
        pass
        return []