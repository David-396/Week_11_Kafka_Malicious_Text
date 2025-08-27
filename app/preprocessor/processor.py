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
        punctuation_marks = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                             ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

        no_punctuation = ''.join([ltr for ltr in txt if ltr not in punctuation_marks])

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
    def clean_text_manager(self, doc:dict):
        clean_doc = {}

        for k,v in doc.items():

            if type(v) == str:

                v = self.rm_punctuation_marks(v).lower().strip()
                v = self.rm_stop_words(v)
                v = self.lemmatize_words(v)

                clean_doc[k] = ' '.join(v)

        return clean_doc