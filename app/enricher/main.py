import os
import time
from app.enricher.manager import EnricherManager

if __name__ == '__main__':

    WEAPON_LIST_FILE_PATH = os.environ.get('WEAPON_LIST_FILE_PATH', 'weapon_list.txt')

    topic_mapping = {
            'enriched_preprocessed_tweets_antisemitic': 'tweets_antisemitic',
            'enriched_preprocessed_tweets_not_antisemitic': 'tweets_not_antisemitic'
        }

    topics_list = ['enriched_preprocessed_tweets_antisemitic', 'enriched_preprocessed_tweets_not_antisemitic']
    enricher = EnricherManager(weapon_list_file_path=WEAPON_LIST_FILE_PATH, topic_mapping=topic_mapping, topics_list=topics_list, group_id='group-1')

    while True:
        try:

            enricher.consume_process_produce()

            time.sleep(0.5)

        except Exception as e:
            print(f'------------ {e} ------------')

            enricher.consumer.close()
            enricher.producer.close()
