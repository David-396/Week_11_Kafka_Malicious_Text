from app.preprocessor.processor import Processor
from app.kafka_config import get_consumer, get_producer_config


class PreProcessorManager:
    def __init__(self):
        self.producer = get_producer_config()
        self.processor = Processor()

    def consume_process_produce(self, consume_topic:str, produce_topic:str, group_id:str):
        try:
            msgs = get_consumer(topic=consume_topic,
                                group_id=group_id)

            for message in msgs:

                clean_msg = self.processor.clean_text_manager(message.value)
                clean_doc = {'original_msg': message.value, 'clean_msg': clean_msg}

                self.producer.send(topic=produce_topic, value=clean_doc)

            self.producer.flush()

        except Exception as e:
            print(f'------------ {e} ------------')