from enrich import Enricher
from app.kafka_config import get_consumer, get_producer_config


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
            msgs = consumer.poll(10000)

            for message in msgs:

                source_topic = message.topic
                target_topic = self.topic_mapping[source_topic]

                doc = message.value
                self.enrich_processors(doc)

                self.producer.send(topic=target_topic, value=doc)

            self.producer.flush()

        except Exception as e:
            print(f'------------ {e} ------------')
