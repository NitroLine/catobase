import os

DB_REGION_NAME = os.environ.get('DB_REGION_NAME', "ru-central1")
DB_ENDPOINT_URL = os.environ.get('DATABASE_ENDPOINT', "")
AWS_PRIVATE_KEY = os.environ.get("ACCESS_ID", "")
AWS_ACCESS_KEY_ID = os.environ.get("ACCESS_KEY", "")