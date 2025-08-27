import logging
from motor.motor_asyncio import AsyncIOMotorClient
from app.data_retrieval.config import MDB_URI,DB_NAME,COLLECTION_NAME

logger = logging.getLogger(__name__)

class MongoDB :
    def __init__(self) :
        self.client = None
        self.db = None
        # self.collection = None

    async def connect(self) :
        logging.info("Connecting to MongoDB...")
        self.client = AsyncIOMotorClient(MDB_URI)
        self.db = self.client[DB_NAME]
        # self.collection = self.db[COLLECTION_NAME]
        logger.info("Connected to IranMalDB/tweets")

    def close(self) :
        if self.client :
            self.client.close()
            logger.info("MongoDB connection closed")

