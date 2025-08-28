import re
from time import strftime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Enricher:
    def __init__(self, weapon_list_file_path:str):
        self.weapon_list_file_path = weapon_list_file_path
        self.weapons_black_list = self.get_weapons_black_list()

        self.sentiment_analyzer = SentimentIntensityAnalyzer()


    # get the weapon black list
    def get_weapons_black_list(self):
        with open(self.weapon_list_file_path, 'r', encoding='utf-8') as f:

            weapons_black_list = {f.readline().strip()}

            for weapon in f:
                weapons_black_list.add(weapon.strip())

            return weapons_black_list

    # find the sentiment of text
    def find_txt_sentiment(self, txt:str):
        sentiment_dict = self.sentiment_analyzer.polarity_scores(txt)

        if sentiment_dict['compound'] >= 0.05:
            return "Positive"
        elif sentiment_dict['compound'] <= -0.05:
            return "Negative"
        else:
            return "Neutral"

    # find the weapons in a text
    def find_weapons(self, txt:str):
        txt = txt.split(' ')
        weapons_lst = [weapon for weapon in txt if weapon in self.weapons_black_list]

        return weapons_lst if weapons_lst else None

    # find the earliest timestamp from text
    @staticmethod
    def earliest_timestamp(txt:str):
        pattern = r"\d{2}-\d{2}-\d{4}"
        matches = re.findall(pattern, txt)

        if matches:

            if len(matches) == 1:
                return matches[0]

            else:
                return max(matches)

        return None