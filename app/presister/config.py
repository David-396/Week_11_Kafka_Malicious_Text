import os
from dotenv import load_dotenv


load_dotenv()

import os

MDB_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")


KAFKA_BROKER_URL = os.getenv("KAFKA_BROKER_URL")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID")

# MDB_USER = os.getenv("MDB_USER")
# MDB_PASSWORD = os.getenv("MDB_PASSWORD")
# MDB_HOST = os.getenv("MDB_HOST")
#
# DB_NAME = os.getenv("DB_NAME", "IranMalDB")
# COLLECTION_NAME = os.getenv("COLLECTION_NAME", "tweets")
# MDB_URI = f"mongodb+srv://{MDB_USER}:{MDB_PASSWORD}@{MDB_HOST}/"

