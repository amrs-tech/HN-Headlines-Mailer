import smtplib
import requests as R
from bs4 import BeautifulSoup as B
import datetime

url = 'https://news.ycombinator.com'
req = R.get(url)
data = req.text
soup = B(data,"html.parser")

#lt_text = soup.find_all("a",class_ = 'storylink').string.strip()
#lt_link = soup.find_all("a",class_ = 'storylink').get('href')

lt_text = soup.find_all("a",class_ = 'storylink')

email_text = ''

for i in range(10):
    email_text += str(i+1) + '. ' + lt_text[i].string + ' \n ' + lt_text[i].get('href') + ' \n '

#print(email_text.encode('utf-8'))


email_text = email_text.encode('utf-8')

subject = 'HackerNews Headlines : '+str(datetime.date.today())

gmail_user = 'ahamedmusthafars@gmail.com'   #mailid
gmail_password = '________' #password


sent_from = gmail_user  
to = ['ahamed.musthafa9@gmail.com']

email_body = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (sent_from, ", ".join(to), subject, email_text)


try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_body)
    server.close()

    print ('Email sent!')
except smtplib.SMTPAuthenticationError as e:  
    print (e)

