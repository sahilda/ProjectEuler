import requests
import json

nba = 'http://api.espn.com/v1/sports/basketball/nba/teams?apikey='
apikey = 'f3rwtxfs97y5s8eg3fxauhqc'
response = requests.get(nba+apikey)

try:
	response = urlopen(request)
	text = response.read()
	print text
except URLError, e:
	print 'no work'