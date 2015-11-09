#!/usr/bin/python

import smtplib
import string
import sys
import os



email_list = ['XXX@gmail.com', 'XXX@gmail.com']
print email_list
for item in email_list: 
    fromaddr = 'XXX@gmail.com'

    print item
    toaddr = item
    cc = []
    subject = 'This is a test email'

    msg = string.join((
        'From: XXX',
        'To: %s' % toaddr,
        'CC: %s' % ', '.join(cc),
        'Subject: %s' % subject, '',
        'hello world'
    ), '\r\n')

    print msg
    toaddrs = [toaddr] + cc 

    print toaddrs 
    server = smtplib.SMTP('smtp.googlemail.com', 587)
    server.starttls()
    server.login('username@gmail.com','pw')
    server.sendmail(fromaddr,toaddrs,msg,)
    server.quit()
