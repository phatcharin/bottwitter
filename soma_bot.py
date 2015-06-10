import tweepy, time, sys, re
from bs4 import BeautifulSoup
from tweepy import OAuthHandler
from urllib import urlopen

CONSUMER_KEY = 'VqMW9UukjypwEEhVcuOEjqcLH'
CONSUMER_SECRET = 'fabR698EYRfkZAqeL8UnQTZgyhLGjL8LvafMD7nxAB9Fgt4Cd1'
ACCESS_KEY = '3240534936-jC9mUQ0udrSK7FopcFnflwT4aQOlAxmeinMWYr2'
ACCESS_SECRET = 'RPn4bs3dA840Bask4p29klyeyZ5fa6qfn2j6rvmgTPgin'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
	optionsUrl = 'http://www.nipponanime.net/forum/shokugeki-no-soma/'
	optionsPage = urlopen(optionsUrl)
	soup = BeautifulSoup(optionsPage)
	
	current_time = time.strftime("%d %m %Y")

	timeUpdate = str(soup.find('td', attrs={'class' : 'lastpost windowbg2'}))
	timeUpdate = re.sub(".*?</a>", "",timeUpdate).strip()
	timeUpdate = re.sub(".*?windowbg2", "",timeUpdate).strip()
	timeUpdate = re.sub("</td>", "",timeUpdate).strip()
	timeUpdate = re.sub("<br/>", "",timeUpdate).strip()
	timeUpdate = re.sub(".*?>", "",timeUpdate).strip()
	
	#print timeUpdate
	
	title = soup.find('span', attrs={'id' : 'msg_588064'})
	title = str(title)
	title = re.sub(".*?Soma", "",title).strip()
	title = re.sub("</a.*?span>", "",title).strip()
	title = "shokugeki-no-soma "+title
	#print title
	
	link = soup.find('span', attrs={'id' : 'msg_588064'})
	link = str(link)
	link = re.sub(".*?href=", "",link).strip()
	link = re.sub(">Shokugeki.*?span>", "",link).strip()
	#print link
	
	nowtime = str(current_time)
	#print nowtime
	status = title+" "+link
	print status
	api.update_status(status=status)
	time.sleep(1000)