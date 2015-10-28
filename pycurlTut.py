import pycurl
from StringIO import StringIO

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://pycurl.sourceforge.net/')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
# Body is a string in some encoding.
# In Python 2, we can print it without knowing what the encoding is.
print(body)
# As long as the file is opened in binary mode, both Python 2 and Python 3
# can write response body to it without decoding.
with open('out.html', 'wb') as f:
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://pycurl.sourceforge.net/')
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()

    