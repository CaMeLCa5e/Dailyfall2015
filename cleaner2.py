#! user/bin/env python 
import pycurl
c = pycurl.Curl()

list = [
    ""
    ]

for item in list:
    # print item
    c.setopt(pycurl.URL, item)
    c.setopt(pycurl.FOLLOWLOCATION, 1)

    c.perform()
    print c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL)  



