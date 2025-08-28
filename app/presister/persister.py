import asyncio
import logging

logger = logging.getLogger(__name__)


class Persister:
    def __init__(self, db, kafka):
        self.db = db
        self.kafka = kafka

    async def consume_and_persist(self):
        """
        Continuously consumes messages from Kafka and persists them to MongoDB
        into collections named after their respective Kafka topics.
        """
        logger.info("Starting message consumption and persistence...")
        async for topic,msg in self.kafka:
            collection_name = topic

            if collection_name not in ["tweets_antisemitic","tweets_not_antisemitic"]:
                logger.warning(f"Received message from unhandled topic:"
                               f" '{collection_name}'. Message: {str(msg)[:50]}...")
                continue

            try:
                result = await self.db[collection_name].insert_one(msg)
                logger.info(f"Inserted message into {collection_name}, id: {result.inserted_id}")
            except Exception as e :
                logger.error(f"Error inserting message into '{collection_name}': {e}")