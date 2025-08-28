import logging
from enrich import Enricher
from kafka_config import get_consumer, get_producer_config

logging.basicConfig(level=logging.INFO)

class EnricherManager:
    def __init__(self, weapon_list_file_path:str, topic_mapping:dict, topics_list:list, group_id:str):
        self.producer = get_producer_config()
        self.enricher = Enricher(weapon_list_file_path=weapon_list_file_path)

        self.topic_mapping = topic_mapping
        self.topics_list = topics_list
        self.group_id = group_id



    def enrich_processors(self, doc:dict):
        original_text = doc['original_text']
        clean_text = doc['clean_text']

        doc['sentiment'] = self.enricher.find_txt_sentiment(clean_text)
        doc['weapons_detected'] = self.enricher.find_weapons(clean_text)
        relevant_time = self.enricher.earliest_timestamp(original_text)

        if relevant_time:
            doc['relevant_timestamp'] = relevant_time

    def consume_process_produce(self):
        try:
            consumer = get_consumer(group_id=self.group_id)
            consumer.subscribe(self.topics_list)
            msgs = consumer.poll(15000)

            if not msgs:
                return

            processed_count = 0

            for tp, ConsumerRecord in msgs.items():

                for record in ConsumerRecord:

                    source_topic = record.topic
                    target_topic = self.topic_mapping[source_topic]

                    doc = record.value
                    self.enrich_processors(doc)

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
