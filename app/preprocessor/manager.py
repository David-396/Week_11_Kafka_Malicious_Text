import logging
from processor import Processor
from kafka_config import get_consumer, get_producer_config

logging.basicConfig(level=logging.INFO)

class PreProcessorManager:
    def __init__(self, text_key:str, topic_mapping:dict, consume_topics:list, group_id:str):
        self.producer = get_producer_config()
        self.processor = Processor()
        self.text_key = text_key
        self.topic_mapping = topic_mapping
        self.consume_topics = consume_topics
        self.group_id = group_id

        self.consumer = get_consumer(group_id=self.group_id)
        self.consumer.subscribe(self.consume_topics)


    def consume_process_produce(self):

        if not self.consumer:
            return

        processed_count = 0

        for message in self.consumer:

            source_topic = message.topic
            target_topic = self.topic_mapping[source_topic]

            doc = message.value
            doc['original_text'] = text = doc.pop(self.text_key)

            clean_msg = self.processor.clean_text_manager(text)
            doc['clean_text'] = clean_msg

            self.producer.send(topic=target_topic, value=doc)
            processed_count += 1
            logging.info(f'Successfully sent: {doc}')

        if processed_count > 0:
            self.producer.flush()
            self.consumer.commit()
            logging.info(f'Successfully processed and committed {processed_count} messages')

