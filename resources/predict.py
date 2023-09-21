import uuid
import pandas as pd
import pickle
from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel


from db import predict
import json


conf = SparkConf().setAppName(__name__)
conf = conf.set("spark.ui.port", "4042")  # Cambia "4041" al puerto que desees

sc = SparkContext(conf=conf)

blp = Blueprint("predict", __name__, description="Operations on predic")

#spark = SparkSession.builder.master("local").appName(__name__).getOrCreate()
spark = SparkSession.builder \
    .appName(__name__) \
    .config("spark.hadoop.io.native.lib.available", "false") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")


# Carga el modelo de PySpark
modelo_cargado = PipelineModel.load("libs/RandomForestClassifier_v1.0.4")



def run_pyspark_job():
    data = [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]
    df = spark.createDataFrame(data, ['id', 'name'])
    json_data = df.toJSON().collect()
    return [json.loads(data) for data in json_data]


@blp.route("/predict/")
class Predict(MethodView):
    #@blp.arguments(PredicSchema)
    #@blp.response(201, PredicSchema)
    def post(cls):
        print(cls)
        try:
            result = run_pyspark_job()
            return jsonify(result), 201
        except:
            return {"code":423,"message": "An error occurred while creating predict."}, 400
        
    
    