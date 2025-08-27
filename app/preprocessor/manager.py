from app.preprocessor.processor import Processor
from app.kafka_config import get_consumer, get_producer_config


class PreProcessorManager:
    def __init__(self):
        self.producer = get_producer_config()
        self.processor = Processor()


    def run(self):
        self.consume_process_produce(consume_topic='raw_tweets_antisemitic',
                                     produce_topic='preprocessed_tweets_antisemitic')

        self.consume_process_produce(consume_topic='raw_tweets_not_antisemitic',
                                     produce_topic='preprocessed_tweets_not_antisemitic')

        self.producer.flush()

    def consume_process_produce(self, consume_topic:str, produce_topic:str):
        try:
            msgs = get_consumer(topic=consume_topic,
                                group_id='group-1')

            for message in msgs:

                clean_msg = self.processor.clean_text_manager(message.value)
                clean_doc = {'original_msg': message.value, 'clean_msg': clean_msg}

                self.producer.send(topic=produce_topic, value=clean_doc)

        except Exception as e:
            print(f'------------ {e} ------------')