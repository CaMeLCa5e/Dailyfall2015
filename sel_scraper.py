class YahooSelTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = ""
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_yahoo_sel(self):
        driver = self.driver
        count = 0
        for i in list:
            count = count + 1
            print count 
            try:
                driver.get(self.base_url + i)
                # time.sleep(3)
                x = driver.page_source.encode("utf-8")
                f.write(x)                
                # url = x
                # page=urllib2.urlopen(url)
                # soup = BeautifulSoup(page.read())
                #"/a/profile/chauncey-palmer/1fo",
#
                # for item in y:
                    # print item

            except: 
                pass

