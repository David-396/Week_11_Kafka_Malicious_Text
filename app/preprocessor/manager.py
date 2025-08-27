from app.preprocessor.processor import Processor
from app.kafka_config import get_consumer, get_producer_config


class PreProcessorManager:
    def __init__(self, text_key:str, topic_mapping:dict, consume_topics:list, group_id:str):
        self.producer = get_producer_config()
        self.processor = Processor()
        self.text_key = text_key
        self.topic_mapping = topic_mapping
        self.consumer =  get_consumer(topics=consume_topics, group_id=group_id)

    def consume_process_produce(self):
        try:

            for message in self.consumer:

                source_topic = message.topic
                target_topic = self.topic_mapping[source_topic]

                doc = message.value
                doc['original_text'] = text = doc.pop(self.text_key)
                clean_msg = self.processor.clean_text_manager(text)
                doc['clean_text'] = clean_msg

                self.producer.send(topic=target_topic, value=doc)

            self.producer.flush()

        except Exception as e:
            print(f'------------ {e} ------------')