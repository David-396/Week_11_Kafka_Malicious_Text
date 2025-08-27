import json
import os
from kafka import KafkaProducer, KafkaConsumer

KAFKA_HOST_NAME = os.environ.get('KAFKA_HOST_NAME', 'kafka')
KAFKA_PORT = os.environ.get('KAFKA_PORT', '9092')



def get_producer_config():
    return KafkaProducer(bootstrap_servers=[f'{KAFKA_HOST_NAME}:{KAFKA_PORT}'],
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'),
                             )


def get_consumer(topic:str, group_id:str):
    bootstrap_servers = [f'{KAFKA_HOST_NAME}:{KAFKA_PORT}']
    return KafkaConsumer(topic,
                                 group_id=group_id,
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 bootstrap_servers=bootstrap_servers,
                                 consumer_timeout_ms=10000)