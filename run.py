import qqapi
from translate import translate
from get_tweets import get_tweets
import os
from time import sleep

name = "realDonaldTrump"

current_dir = os.path.dirname(os.path.abspath(__file__))
tweet_log = current_dir+"/{}.log".format(name)


tweets = get_tweets(name)

translated = []

for i in tweets[:4]:
	translated.append(translate(i, 'en', 'zh'))

# final_text = name+"\n"

# for i in translated[:4]:
# 	final_text += i+"\n"

final_text = "@"+name+"\n"

for i in translated[:4]:
	final_text += i+'\n'

print(final_text)
print(len(final_text))

qq = qqapi.Sender("http://swz1994.com:5000")

qq.send_message(614291728, final_text, "group")