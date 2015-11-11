count = 0
for item in list:
    count = count + 1
    print count 
    # print item
    try: 
        c.setopt(pycurl.URL, item)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.perform()
        print c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL)  
    except: 
        pass
