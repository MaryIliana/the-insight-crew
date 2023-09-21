# app.py
import os
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_uploads import configure_uploads #, patch_request_class
from dotenv import load_dotenv

#Para el modelo
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import json



from resources.model import blp as ModelBlueprint
from resources.preprocessed import blp as PreprocessedBlueprint
from resources.predict import blp as PredictBlueprint
from resources.data import blp as DataBlueprint
#from resources.data import DataUpload
from libs.data_helper import DOC_DATA
#from libs import aws_helper
#from sklearn.externals import joblib
#import numpy as np


app = Flask(__name__)
# Carga las variables de entorno desde .flaskenv
load_dotenv(".env", verbose=True)


# Carga la configuración de la aplicación
#app.config.from_object("config")
#app.config.from_envvar("APPLICATION_SETTINGS")

app.config['UPLOADED_DATA_DEST'] = "static/csv"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
#patch_request_class(app, 10 * 1024 * 1024) # 10MB max size upload
configure_uploads(app, DOC_DATA)



## API Documentación 
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/doc-api"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

app.config["JWT_SECRET_KEY"] = "jose"
jwt = JWTManager(app)
    
api = Api(app)

api.register_blueprint(PreprocessedBlueprint)
api.register_blueprint(ModelBlueprint)
api.register_blueprint(PredictBlueprint)
api.register_blueprint(DataBlueprint)

#api.add_resource(DataUpload, "/upload/data")
#api.register_blueprint(PredictBlueprint)