from flask_restful import Resource
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_uploads import UploadNotAllowed
from flask import request

from libs import data_helper
from schemas.data import DataSchema

data_schema = DataSchema()

blp = Blueprint("DataUpload", __name__, description="Operations on DataUpload")

@blp.route("/upload/data/")
class DataUpload(MethodView):
    def post(cls):
        """
        Used to upload an data file
        If there is a filename conflict, it appends a number at the end.
        """
        filedata = data_schema.load(request.files)
        folder = "files"
        
        try:
            data_path = data_helper.save_data(filedata["data"], folder=folder)
            basename = data_helper.get_basename(data_path)
            return {"message": "document '{}' uploaded.".format(basename)}, 201
        except UploadNotAllowed:
            extension = data_helper.get_extension(filedata["data"])
            return {"message": "Extension '{}' is not allowed".format(extension)}, 400
        