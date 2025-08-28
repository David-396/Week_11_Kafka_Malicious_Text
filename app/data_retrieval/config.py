import os
from dotenv import load_dotenv


load_dotenv()

MDB_USER = os.getenv("MDB_USER")
MDB_PASSWORD = os.getenv("MDB_PASSWORD")
MDB_HOST = os.getenv("MDB_HOST")
DB_NAME = os.getenv("DB_NAME", "IranMalDB")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "tweets")
MDB_URI = f"mongodb+srv://{MDB_USER}:{MDB_PASSWORD}@{MDB_HOST}/"

