import tweepy
import sys



# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

def get_tweets(name):
	consumer_key = "C6RO2DoLXwQehvbNnZRdCi4rp"
	consumer_secret = "zRTB10DNJXVInNTHgnbriO29FFIJPUgBwjT0C8W4vwGTUo6kXA"
	access_token = "115904327-6bqjKzxRDPFzGAdwvz6oCYoElHewvocztydZm2ks"
	access_secret = "emm0zSyicWkNAxg1YZQD8qgn5yKYi19NAMUOqafBxP3WI"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)

	tweets_list = []
	tweets = api.user_timeline(screen_name=name)
	for i in tweets:
		tweets_list.append("{} {}".format(i.created_at, i.text))
	return tweets_list

