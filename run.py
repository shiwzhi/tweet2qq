import qqapi
from translate import translate
from get_tweets import get_tweets
import os
from time import sleep


name = "realDonaldTrump"
current_dir = os.path.dirname(os.path.abspath(__file__))
tweet_log = current_dir+"/{}.log".format(name)



def get_latest():
	tweets = get_tweets(name)
	translated = []
	for i in tweets[:3]:
		translated.append(translate(i, 'en', 'zh'))

	# final_text = name+"\n"

	# for i in translated[:4]:
	# 	final_text += i+"\n"

	final_text = "@"+name+"\n"

	for i in translated[:4]:
		final_text += i+'\n'

	print(final_text)
	print(len(final_text))

	return final_text




while True:
	sleep(60)
	if not os.path.isfile(tweet_log):
		f = open(tweet_log, 'w')
		f.write("init")
		f.close()
	latest = get_latest()
	current = open(tweet_log, 'r').read()
	if latest == current:
		pass
	else:
		f = open(tweet_log, 'w')
		f.write(latest)
		f.close()
		qq = qqapi.Sender("http://swz1994.com:5000")
		qq.send_message(1179756234, latest, "friend")
		
