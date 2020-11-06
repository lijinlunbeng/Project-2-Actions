import tweepy as tw





def fecth_random_tweets(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    # Define the search term and the date_since date as variables
    search_words = "#kpop"
    date_since = "2018-11-16"

    # Collect tweets
    tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since).items(1)

    # Iterate and print tweets
    return tweets
