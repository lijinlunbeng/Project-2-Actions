import unittest
import twitter_example
import os


class MyTestCase(unittest.TestCase):
    def test_fetch_successful(self):
        """
        test
        :return:
        """
        at = os.getenv('ACCESS_TOKEN')
        ats = os.getenv('ACCESS_TOKEN_SECRET')
        ck = os.getenv('CONSUMER_KEY')
        cs = os.getenv('CONSUMER_SECRET')

        res = twitter_example.fecth_random_tweets(ck, cs, at, ats)

        txt = []
        for tweet in res:
            txt.append(tweet.text)
        print(txt)


        self.assertEqual(1, len(txt))




if __name__ == '__main__':
    unittest.main()
