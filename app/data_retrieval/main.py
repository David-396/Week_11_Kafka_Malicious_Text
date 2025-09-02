import os
import pymongo
import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()




MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
DB_NAME = os.environ.get('DB_NAME', 'tweets')
ANTISEMITE_COLLECTION_NAME = os.environ.get('ANTISEMITE_DB_NAME', 'tweets_antisemitic')
NOT_ANTISEMITE_COLLECTION_NAME = os.environ.get('NOT_ANTISEMITE_COLLECTION_NAME', 'tweets_not_antisemitic')

MDB_USER = os.getenv("MDB_USER", "root")
MDB_PASSWORD = os.getenv("MDB_PASSWORD", "example")

MDB_URI = f"mongodb://{MDB_USER}:{MDB_PASSWORD}@{MONGO_HOST}/{DB_NAME}?authSource=admin"

@app.get('/anti')
def get_antisemitic_tweets():
    try:

        client = pymongo.MongoClient(MDB_URI)
        mydb = client[DB_NAME]
        collection = mydb[ANTISEMITE_COLLECTION_NAME]

        data = collection.find({},{'_id':0}).to_list()

        return JSONResponse(content=data)

    except Exception as e:
        print(e)

        return e

    finally:
        client.close()


@app.get('/not-anti')
def get_not_antisemitic_tweets():
    try:

        client = pymongo.MongoClient(MDB_URI)
        mydb = client[DB_NAME]
        collection = mydb[NOT_ANTISEMITE_COLLECTION_NAME]

        data = collection.find({},{'_id':0}).to_list()

        return JSONResponse(content=data)

    except Exception as e:
        print(e)
        return e


uvicorn.run(app=app, host='localhost', port=8080)