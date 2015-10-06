import urllib2
import simplejson 

url = 'https://www.api.twitter.com/1.1/statuses/mentions_timeline.json'

if __name__ == '__main__':
	req = urllib2.Requests(url)
	
