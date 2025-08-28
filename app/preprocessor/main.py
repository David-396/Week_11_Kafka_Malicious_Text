import os
import time
from manager import PreProcessorManager

if __name__ == '__main__':

    TEXT_KEY = os.environ.get('TEXT_KEY', 'text')
    GROUP_ID = os.environ.get('GROUP_ID', 'preprocessor-group')

    topic_mapping = {'raw_tweets_antisemitic':'preprocessed_tweets_antisemitic',
                     'raw_tweets_not_antisemitic':'preprocessed_tweets_not_antisemitic'}

    consume_topics = ['raw_tweets_antisemitic', 'raw_tweets_not_antisemitic']

    manager = PreProcessorManager(text_key=TEXT_KEY, topic_mapping=topic_mapping, consume_topics=consume_topics, group_id=GROUP_ID)

    while True:
        try:

            manager.consume_process_produce()

            time.sleep(0.5)

        except Exception as e:
            print(f'------------ {e} ------------')

            manager.producer.close()
