import re

from lemmatization import Lemmatizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Processor:
    def __init__(self):
        self.lemmatizer = Lemmatizer()
        nltk.download('stopwords')
        nltk.download('punkt')

    # remove punctuation marks
    @staticmethod
    def rm_punctuation_marks(txt:str):

        no_punctuation = re.sub('[^A-Za-z0-9 ]+', '', txt)

        return no_punctuation

    # remove the stop words
    @staticmethod
    def rm_stop_words(txt:str):
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(txt)

        filtered_txt = ' '.join([word for word in tokens if word not in stop_words])

        return filtered_txt

    # find the root for every word
    def lemmatize_words(self, txt:str):
        lemmatized = self.lemmatizer.lemmatize(txt)
        return lemmatized

    # clean the text manager
    def clean_text_manager(self, txt:str):

        clean_txt = self.rm_punctuation_marks(txt).lower().strip()
        clean_txt = self.rm_stop_words(clean_txt)
        clean_txt = self.lemmatize_words(clean_txt)

        clean_txt = ' '.join(clean_txt)

        return clean_txt