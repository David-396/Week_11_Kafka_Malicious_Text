import os
import time
from manager import EnricherManager

if __name__ == '__main__':

    GROUP_ID = os.environ.get('GROUP_ID', 'enricher-group')
    WEAPON_LIST_FILE_PATH = os.environ.get('WEAPON_LIST_FILE_PATH', 'weapon_list.txt')

    topic_mapping = {'preprocessed_tweets_antisemitic': 'enriched_preprocessed_tweets_antisemitic',
                     'preprocessed_tweets_not_antisemitic': 'enriched_preprocessed_tweets_not_antisemitic'}

    topics_list = ['preprocessed_tweets_antisemitic', 'preprocessed_tweets_not_antisemitic']

    enricher = EnricherManager(weapon_list_file_path=WEAPON_LIST_FILE_PATH, topic_mapping=topic_mapping, topics_list=topics_list, group_id=GROUP_ID)

    try:

        enricher.consume_process_produce()

    except Exception as e:
        print(f'------------ {e} ------------')

        enricher.producer.close()
        enricher.consumer.close()
