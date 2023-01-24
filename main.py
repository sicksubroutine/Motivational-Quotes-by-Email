import schedule, time, os, smtplib, random, ast
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

username = os.environ['mailUsername']
password = os.environ['mailPassword']

def motivate():
  quotes = []
  with open('quotes.txt', 'r') as f:
    quotes = ast.literal_eval(f.read())
  quote = random.choice(quotes)
  return quote

def sendMail(quote):
  email_body = f"This is today's motivational quote:\n{quote}"
  server = os.environ['STMP_SERVER']
  port = 587
  s = smtplib.SMTP(host = server,port = port)
  s.starttls()
  s.login(username, password)
  msg = MIMEMultipart()
  msg['To'] = os.environ['emailTo']
  msg['From'] = os.environ['emailFrom']
  msg['Subject'] = "Quote of the Day!"
  msg.attach(MIMEText(email_body, 'html'))
  s.send_message(msg)
  del msg

def printMe():
  quote = motivate()
  print(f"⏰ Sending motivational quote to you: {quote}")
  sendMail(quote)

schedule.every().day.at("18:00").do(printMe)

while True:
  schedule.run_pending()
  time.sleep(5)