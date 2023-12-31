import os


FLASK_DEBUG = False
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
AWS_REGION = os.environ.get('AWS_REGION')
AWS_BUCKET = os.environ.get('AWS_BUCKET')
SWAGGER_PROPAGATE_EXCEPTIONS= os.environ.get('SWAGGER_PROPAGATE_EXCEPTIONS')
SWAGGER_API_TITLE = os.environ.get('SWAGGER_API_TITLE')
SWAGGER_API_VERSION = os.environ.get('SWAGGER_API_VERSION')
SWAGGER_OPENAPI_VERSION = os.environ.get('SWAGGER_OPENAPI_VERSION')
SWAGGER_OPENAPI_URL_PREFIX = os.environ.get('SWAGGER_OPENAPI_URL_PREFIX')
SWAGGER_OPENAPI_SWAGGER_UI_PATH = os.environ.get('SWAGGER_OPENAPI_SWAGGER_UI_PATH')
SWAGGER_OPENAPI_SWAGGER_UI_URL = os.environ.get('SWAGGER_OPENAPI_SWAGGER_UI_URL')


UPLOADED_DATA_DEST = "static/csv"
MAX_CONTENT_LENGTH = 16 * 1000 * 1000