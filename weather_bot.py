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
	optionsUrl = 'https://weather.yahoo.com/'
	optionsPage = urlopen(optionsUrl)
	soup = BeautifulSoup(optionsPage)
	
	current_time = time.strftime("%H:%M:%S")

	temp = soup.findAll('div', attrs={'class' : 'temp'})
	temp = str(soup.find('span', attrs={'class' : 'c'}))
	temp = re.sub("span.*?num", "",temp).strip()
	temp = re.sub("<.*?>", "",temp).strip()
	
	location = soup.findAll('div', attrs={'id' : 'location-chooser'})
	location = str(soup.find('span', attrs={'class' : 'name'}))
	location = re.sub("span.*?name", "",location).strip()
	location = re.sub("<.*?>", "",location).strip()
	
		
	status = location+" "+current_time+" temp "+temp
	print status
	api.update_status(status=status)
	time.sleep(30)