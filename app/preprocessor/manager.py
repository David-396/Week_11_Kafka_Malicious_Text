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


    def consume_process_produce(self):
        try:

            consumer = get_consumer(group_id=self.group_id)
            consumer.subscribe(self.consume_topics)

            msgs = consumer.poll(20000)

            if not msgs:
                return

            processed_count = 0

            for tp, ConsumerRecord in msgs.items():

                for record in ConsumerRecord:

                    source_topic = record.topic
                    target_topic = self.topic_mapping[source_topic]

                    doc = record.value
                    doc['original_text'] = text = doc.pop(self.text_key)

                    clean_msg = self.processor.clean_text_manager(text)
                    doc['clean_text'] = clean_msg

                    future = self.producer.send(topic=target_topic, value=doc)

                    try:

                        future.get(timeout=10)
                        processed_count += 1
                        logging.info(f'Successfully sent: {doc}')

                    except Exception as send_error:
                        logging.error(f'Failed to send message: {send_error}')
                        raise

                if processed_count > 0:
                    self.producer.flush()
                    consumer.commit()
                    logging.info(f'Successfully processed and committed {processed_count} messages')

        except Exception as e:
            logging.error(f'Error in consume_process_produce: {e}')

            raise

        finally:
            if consumer:
                consumer.close()
