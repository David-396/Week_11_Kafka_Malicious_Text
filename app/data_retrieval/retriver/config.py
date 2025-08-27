import os

MDB_USER = os.getenv("MDB_USER","IRGC")

MDB_PASSWORD = os.getenv("MDB_PASSWORD","iraniraniran")

DB_NAME = os.getenv("DB_NAME","IranMalDB")

MONGO_URI = os.getenv(
    "MDB_CONNECTION",
    f"mongodb+srv://{MDB_USER}:{MDB_PASSWORD}@iranmaldb.gurutam.mongodb.net/"
)

COLLECTION_NAME = os.getenv("COLLECTION_NAME", "tweets")