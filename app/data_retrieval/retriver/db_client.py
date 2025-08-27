import logging
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI,DB_NAME,COLLECTION_NAME


class MongoDB :
    def __init__(self) :
        self.client = None
        self.db = None
        self.collection = None

    async def connect(self) :
        logging.info("Connecting to MongoDB...")
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client[DB_NAME]
        self.collection = self.db[COLLECTION_NAME]
        logging.info("Connected to IranMalDB/tweets")

    def close(self) :
        if self.client :
            self.client.close()
            logging.info("MongoDB connection closed")

# from motor.motor_asyncio import AsyncIOMotorClient
#
# client = AsyncIOMotorClient(MONGO_URI)
# db = client[DB_NAME]
# collection = db[COLLECTION_NAME]