from app.preprocessor.manager import PreProcessorManager

if __name__ == '__main__':
    manager = PreProcessorManager()

    while True:
        manager.consume_process_produce(consume_topic='raw_tweets_antisemitic',
                                     produce_topic='preprocessed_tweets_antisemitic',
                                     group_id='group-1')

        manager.consume_process_produce(consume_topic='raw_tweets_not_antisemitic',
                                     produce_topic='preprocessed_tweets_not_antisemitic',
                                     group_id='group-1')