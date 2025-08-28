import asyncio
import logging
from db_handler import MongoDB
from consumer import KafkaConsumer
from persister import Persister

logging.basicConfig(level=logging.INFO)


async def main() :
    mongo = MongoDB()
    kafka = KafkaConsumer()


    await kafka.start_consumer()
    await mongo.connect()

    persister = Persister(mongo.db, kafka)

    try :
        await persister.consume_and_persist()
    except KeyboardInterrupt :
        logging.info("Shutting down...")
    finally :
        await kafka.stop_consumer()
        mongo.close()


if __name__ == "__main__" :
    asyncio.run(main())