import qqapi
from translate import translate
from get_tweets import get_tweets
import os

name = "realDonaldTrump"

current_dir = os.path.dirname(os.path.abspath(__file__))
tweet_log = current_dir+"/{}.log".format(name)


tweets = get_tweets(name)

translated = []

for i in tweets:
	translated.append("{} {}".format(i, translate(i, 'en', 'zh')))

final_text = ""

for i in translated[:4]:
	final_text += i+"\n"

qq = qqapi.Sender("http://swz1994.com:5000")

qq.send_message(614291728, news, "group")