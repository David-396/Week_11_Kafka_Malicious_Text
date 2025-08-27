from app.preprocessor.processor import Processor
from app.kafka_config import get_consumer, get_producer_config


class PreProcessorManager:
    def __init__(self, text_key:str):
        self.producer = get_producer_config()
        self.processor = Processor()
        self.text_key = text_key

    def consume_process_produce(self, consume_topic:str, produce_topic:str, group_id:str):
        try:
            msgs = get_consumer(topic=consume_topic,
                                group_id=group_id)

            for message in msgs:

                doc = message.value
                doc['original_text'] = text = doc.pop(self.text_key)
                clean_msg = self.processor.clean_text_manager(text)
                doc['clean_text'] = clean_msg

                self.producer.send(topic=produce_topic, value=doc)

            self.producer.flush()

        except Exception as e:
            print(f'------------ {e} ------------')