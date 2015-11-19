def send_email(smtp_address, usr, password, msg, mode):
    server = smtplib.SMTP(smtp_address);
    server.ehlo();
    server.starttls();
    server.ehlo();
    server.login(username,password);
    if (mode == 0 and msg['To'] != ''):
        server.sendmail(msg['From'],(msg['To']+msg['Cc']).split(","), msg.as_string());
    elif (mode == 1 and msg['Bcc'] != ''):
        server.sendmail(msg['From'],msg['Bcc'].split(","),msg.as_string());
    elif (mode != 0 and mode != 1):
        print 'error in send mail bcc'; print 'email cancled'; exit();
    server.quit();
