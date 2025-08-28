import logging
from motor.motor_asyncio import AsyncIOMotorClient
from config import MDB_URI, DB_NAME

logger = logging.getLogger(__name__)

class MongoDB :
    def __init__(self) :
        self.client = None
        self.db = None

    async def connect(self) :
        logging.info("Connecting to MongoDB...")
        self.client = AsyncIOMotorClient(MDB_URI)
        self.db = self.client[DB_NAME]
        logger.info("Connected to DB")

    def close(self) :
        if self.client :
            self.client.close()
            logger.info("MongoDB connection closed")
