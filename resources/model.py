import uuid
import pandas as pd
import pickle
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import model

blp = Blueprint("model", __name__, description="Operations on predic")

@blp.route("/model/")
class Model(MethodView):
    #@blp.arguments(PredicSchema)
    #@blp.response(201, PredicSchema)
    def post(cls):
        # Consigo los datos de la petición
        #data = request.get_json(force=True)
        #predic_data
        
        # Leo el pickle con nuestro modelo
        with open("model.pkl", "rb") as file:
        # carga los datos del archivo pickle
            model = pickle.load(file)
        
        # Los datos llegan como json los tengo que pasar a numpy
        #parapred = pd.json_normalize(predic_data)
    
        # Make prediction using model loaded from disk as per the data.
        #prediction = model.predict(parapred)
    
        #pred_list = prediction.tolist()
    
        return jsonify(pred_list)