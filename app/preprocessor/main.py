import time
from app.preprocessor.manager import PreProcessorManager

if __name__ == '__main__':

    topic_mapping = {'raw_tweets_antisemitic':'preprocessed_tweets_antisemitic',
                     'raw_tweets_not_antisemitic':'preprocessed_tweets_not_antisemitic'}
    consume_topics = ['raw_tweets_antisemitic', 'raw_tweets_not_antisemitic']

    manager = PreProcessorManager(text_key='text', topic_mapping=topic_mapping, consume_topics=consume_topics, group_id='group-1')

    while True:
        try:

            manager.consume_process_produce()

            time.sleep(0.5)

        except Exception as e:
            print(f'------------ {e} ------------')

            manager.consumer.close()
            manager.producer.close()
