import smtplib
import requests as R
from bs4 import BeautifulSoup as B
import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "me@gmail.com"
you = "you@gmail.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = 'HackerNews Headlines : '  +str(datetime.date.today())
msg['From'] = me
msg['To'] = you

url = 'https://news.ycombinator.com'
req = R.get(url)
data = req.text
soup = B(data,"html.parser")

lt_text = soup.find_all("a",class_ = 'storylink')

html = '<div style="background-color:#ff6600;font-size:14px;padding:5px 20px 5px"><b>Hacker News | <a href="newest">new</a> | <a href="newcomments">comments</a> | <a href="show">show</a> | <a href="ask">as$

for i in range(10):
    html += '<p>' + str(i+1) + '. ' + '<a href="' +  lt_text[i].get('href')  + '">' + lt_text[i].string + ' </a></p>'

html += '</div>' 

part2 = MIMEText(html, 'html')

msg.attach(part2)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('me@gmail.com', 'MYPASSWORD')
mail.sendmail(me, you, msg.as_string())
mail.quit()