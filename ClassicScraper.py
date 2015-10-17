
from bs4 import BeautifulSoup
import urllib2
import pycurl

url = 'url'
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, 'html.parser')
print(soup.prettify())

# soup.find_all('a')

# for link in soup.find_all('a'):
#     print(link.get('href'))


# post_id = ['name']
# post_name = ['gen']
# post_date = ['postdetails']
# post_body = ['postbody']

# required_fields = post_id, post_name, #post_date, post_body

# print required_fields
