import os
import json
import asyncio
import logging
from aiokafka import AIOKafkaConsumer

logger = logging.getLogger(__name__)

KAFKA_BROKER_URL = os.getenv("KAFKA_BROKER_URL", "localhost:9092")

TOPIC_ANTISEMITIC = "tweets_antisemitic"
TOPIC_NOT_ANTISEMITIC = "tweets_not_antisemitic"


class KafkaConsumer:
    def __init__(self):
        self.consumer = None

    async def start_consumer(self):
        """Starts the Kafka consumer and subscribes to defined topics."""
        self.consumer = AIOKafkaConsumer(
            TOPIC_ANTISEMITIC,
            TOPIC_NOT_ANTISEMITIC,
            bootstrap_servers=KAFKA_BROKER_URL,
            group_id="persister-service",
            value_deserializer=lambda v: json.loads(v.decode("utf-8"))
        )
        await self.consumer.start()
        logger.info(f"Kafka consumer started")

    async def stop_consumer(self):
        if self.consumer:
            await self.consumer.stop()
            logger.info("Kafka consumer stopped")

    async def get_messages(self):
        if self.consumer is None:
            raise RuntimeError("Consumer not initialized")
        try:
            async for msg in self.consumer:
                logger.info(
                    f"Received message from {msg.topic} "
                    f"{str(msg.value)[:30]}..."
                )
                yield msg.topic,msg.value
        except Exception as e:
            logger.error(f"Error while consuming: {e}")
