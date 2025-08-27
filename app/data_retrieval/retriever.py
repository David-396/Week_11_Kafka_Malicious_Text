import asyncio
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Retriever:
    def __init__(self, db, kafka):
        self.db = db
        self.kafka = kafka
        self.last_date = None
        self.last_id = None

    async def fetch_and_publish(self):
        while True:
            doc = await self.db['tweets'].find_one({})
            if not doc:
                logger.info("no documents found waiting")
                await asyncio.sleep(60)
                continue

            query = {}
            if self.last_date:
                query["$or"] = [
                    {"CreateDate": {"$gt": self.last_date}},
                    {"CreateDate": self.last_date, "_id": {"$gt": self.last_id}}
                ]

            logger.info(f"last_date={self.last_date}, last_id={self.last_id}")
            logger.info(f"query to run: {query}")


            cursor = self.db['tweets'].find(query).sort([
                ("CreateDate", 1),
                ("_id", 1)
            ]).limit(100)

            tweets = await cursor.to_list(length=100)

            if tweets:
                logger.info(f"Found {len(tweets)} tweets to publish to Kafka")
                for tweet in tweets:
                    tweet['id'] = str(tweet['_id'])
                    tweet.pop('_id', None)
                    topic = "raw_tweets_antisemitic" if tweet.get('Antisemitic') else "raw_tweets_not_antisemitic"
                    await self.kafka.publish(topic, tweet)
                    logger.debug(f"Sent tweet ID: {tweet['id']} to topic: {topic}")

                self.last_date = tweets[-1]['CreateDate']
                self.last_id = tweets[-1]['id']
            else:
                logger.info("No new tweets found")

            await asyncio.sleep(60)




