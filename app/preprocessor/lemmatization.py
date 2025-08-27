from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
import nltk


class Lemmatizer:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        nltk.download('punkt_tab')
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        nltk.download('averaged_perceptron_tagger_eng')

    @staticmethod
    def get_wordnet_pos(tag):
        if tag.startswith('J'):
            return 'a'
        elif tag.startswith('V'):
            return 'v'
        elif tag.startswith('N'):
            return 'n'
        elif tag.startswith('R'):
            return 'r'
        else:
            return 'n'

    def lemmatize(self, txt:str):
        lemmatized_sentence = []

        tokens = word_tokenize(txt)
        tagged_tokens = pos_tag(tokens)

        for word, tag in tagged_tokens:
            lemmatized_sentence.append(self.lemmatizer.lemmatize(word, self.get_wordnet_pos(tag)))

        return lemmatized_sentence