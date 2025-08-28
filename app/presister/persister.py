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
        async for topic,msg in self.kafka.get_messages():
            # collection_name = topic

            if topic not in ["enriched_preprocessed_tweets_antisemitic",
                "enriched_preprocessed_tweets_not_antisemitic"]:
                logger.warning(f"Received message from unhandled topic:"
                               f" '{topic}'. Message: {str(msg)[:50]}...")
                continue

            try:
                collection_name = None
                if topic == "enriched_preprocessed_tweets_antisemitic":
                    collection_name = "tweets_antisemitic"
                else:
                    collection_name = "tweets_not_antisemitic"
                # collection_name = collection_name.replace("enriched_preprocessed_tweets_","")
                result = await self.db[collection_name].insert_one(msg)
                logger.info(f"Inserted message into {collection_name}, id: {result.inserted_id}")


            except RuntimeError as e:
                logger.critical(f"Persister failed to start due to consumer error: {e}")
            except asyncio.CancelledError:
                    logger.info("Persister task cancelled.")
            except Exception as e:
                    logger.critical(f"Unhandled error in persister: {e}", exc_info=True)
