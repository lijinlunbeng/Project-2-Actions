import os
import unittest

from tweepy import Status

import Tweepy_file
import Tweeter_time
import Tweepy_Hashtag
import google1
import google2
import read_and_calculate
import utils
import tweepy


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)


class TweepyFileTestCase(unittest.TestCase):

    def test_get_new_tweets(self):
        res = Tweepy_file.get_new_tweets("@TheDailyShow")
        self.assertEqual(isinstance(res[0], Status), True)
        self.assertEqual(len(res), 10)

class TweepyFileTestCase(unittest.TestCase):

    def test_get_new_tweets_1(self):
        res = Tweeter_time.get_new_tweets("@TheDailyShow")
        self.assertEqual(isinstance(res[0], Status), True)
        self.assertEqual(len(res), 10)

class TweepyFileTestCase(unittest.TestCase):

    def test_get_hashtag_tweets(self):
        res = Tweepy_Hashtag.get_hashtag_tweets("#VOTE",100)
        self.assertEqual(isinstance(res, tweepy.cursor.ItemIterator), True)

class TestGooleJsonFile(unittest.TestCase):

    def test_google_json_file(self):
        tmp = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        with open("google.json", "w") as f:
            f.write(tmp)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google.json"
        text_content = "Google, headquartered in Mountain."
        google1.analyze_entity_sentiment(text_content)

class TestGooleJsonFile(unittest.TestCase):

    def test_google_json_file_1(self):
        tmp = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        with open("google.json", "w") as f:
            f.write(tmp)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google.json"
        file = '#VOTE_tweets.csv'
        google2.analyze_overal_entity_sentiment(file)

    def value_validation(self):
        tmp = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        with open("google.json", "w") as f:
            f.write(tmp)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google.json"
        file = '#VOTE_tweets.csv'
        google2.analyze_overal_entity_sentiment(file)
        result = google2.calculate_overal_entity_sentiment()
        self.assertEqual(result[0], -0.14700000323355197)
        self.assertEqual(result[1], 0.7190000089257955)

class TestGooleJsonFile(unittest.TestCase):

    def test_entity_sentiment_detail(self):
        tmp = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        with open("google.json", "w") as f:
            f.write(tmp)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google.json"
        result = read_and_calculate.analyze_entity_sentiment_detail()
        self.assertListEqual(result, ['OTHER', 'CONSUMER_GOOD', 'LOCATION', 'PERSON', 'EVENT', 'ORGANIZATION', 'WORK_OF_ART'])

    def test_test_num(self):
        tmp = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        with open("google.json", "w") as f:
            f.write(tmp)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google.json"
        category = ['OTHER', 'CONSUMER_GOOD', 'LOCATION', 'PERSON', 'EVENT', 'ORGANIZATION', 'WORK_OF_ART']
        self.assertListEqual(read_and_calculate.calculate_entity(category[0]), [0.34190871705652764, -0.12780083143983145])
        self.assertListEqual(read_and_calculate.calculate_entity(category[1]), [0.10000000149011612, 0.10000000149011612])
        self.assertListEqual(read_and_calculate.calculate_entity(category[2]), [0.18571428528853826, 0.04285714030265808])
        self.assertListEqual(read_and_calculate.calculate_entity(category[3]), [0.33043478477908217, 0.002173912104057229])
        self.assertListEqual(read_and_calculate.calculate_entity(category[4]), [0.2714285736992246, -0.08571428841068632])
        self.assertListEqual(read_and_calculate.calculate_entity(category[5]), [0.20000000058540277, -0.12857142809246266])
        self.assertListEqual(read_and_calculate.calculate_entity(category[6]), [0.2666666756073634, 0.13333334028720856])
