import asyncio
import logging
from db_client import MongoDB
from kafka_producer import KafkaProducer
from retriever import Retriever

logging.basicConfig(level=logging.INFO)


async def main() :
    mongo = MongoDB()
    kafka = KafkaProducer()

    await mongo.connect()
    await kafka.start_producer()

    retriever = Retriever(mongo.db, kafka)

    try :
        await retriever.fetch_and_publish()
    except KeyboardInterrupt :
        logging.info("Shutting down...")
    finally :
        await kafka.stop_producer()
        mongo.close()


if __name__ == "__main__" :
    asyncio.run(main())
