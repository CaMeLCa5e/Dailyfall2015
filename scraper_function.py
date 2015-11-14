for item in url_list: 
    time.sleep(2)
    try:
        # url = item
        page=urllib2.urlopen(item)
        soup = BeautifulSoup(page.read())
        a_tags=soup.findAll('a',)
        for link in a_tags:
            print link['href']
    except: 
        pass