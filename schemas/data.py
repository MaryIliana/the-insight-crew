from marshmallow import Schema, fields
import typing
from werkzeug.datastructures import FileStorage

class FileStorageField(fields.Field):
    default_error_messages = {
        "invalid": "Not a valid datafile."
    }
    def _deserialize(self, value, attr, data) -> FileStorage:
        if value is None:
            return None
        if not isinstance(value, FileStorage):
            self.fail('invalid') # raises validationError
        return value


class DataSchema(Schema):
    data = FileStorageField(required=True) 