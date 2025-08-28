import os
import pymongo
from fastapi import FastAPI

app = FastAPI()




MONGO_HOST = os.environ.get('MONGO_HOST', 'mongo_db')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
DB_NAME = os.environ.get('DB_NAME', 'tweets')
ANTISEMITE_COLLECTION_NAME = os.environ.get('ANTISEMITE_DB_NAME', 'tweets_antisemitic')
NOT_ANTISEMITE_COLLECTION_NAME = os.environ.get('NOT_ANTISEMITE_COLLECTION_NAME', 'tweets_not_antisemitic')

@app.get('/anti')
def get_antisemietic_tweets():
    try:

        client = pymongo.MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
        mydb = client[DB_NAME]
        collection = mydb[ANTISEMITE_COLLECTION_NAME]

        data = collection.find()

        return data

    except Exception as e:
        print(e)

        return e

    finally:
        client.close()


@app.get('/not-anti')
def get_not_antisemietic_tweets():
    try:

        client = pymongo.MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
        mydb = client[DB_NAME]
        collection = mydb[NOT_ANTISEMITE_COLLECTION_NAME]

        data = collection.find()

        return data

    except Exception as e:
        print(e)
        return e
