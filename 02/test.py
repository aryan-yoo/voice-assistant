# import urllib.request
# import webbrowser

# song = "blinding lights"

# query = urllib.parse.quote(song)
# webbrowser.open(f"https://www.youtube.com/results?search_query={query}")


# import urllib.request
# from bs4 import BeautifulSoup

# textToSearch = 'blinding lights'
# query = urllib.parse.quote(textToSearch)
# url = "https://www.youtube.com/results?search_query=" + query
# response = urllib.request.urlopen(url)
# html = response.read()
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.findAll(attrs={"class": "yt-uix-tile-link"}))

# for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
#     print('https://www.youtube.com' + vid['href'])
# import wikipedia
# import smtplib,ssl
# username ="aryanchristian55@gmail.com"
# password = "9173649500@Aryan"
# context = ssl.create_default_context()
# server = smtplib.SMTP('smtp.gmail.com',587)
# server.ehlo()
# server.starttls(context=context)
# server.login(username, password)
# # speak("What is the subject of the email")
# subject = "testing"
# print(subject)
# # speak("What is the body of the email")
# body = "lasan email"
# print(body)
# # speak("What is the recipient's email")
# recipient = "raj885057@gmail.com"
# message = f"{subject}\n \n {body}"
# server.sendmail(username,recipient,message)
# server.quit()
# print()

import smtplib

# # Gmail credentials
# username = "aryanchristian55@gmail.com"
# password = "9173649500@Aryan"  # Use your app password if 2FA is enabled

# # Email setup
# to = "raj885057@gmail.com"
# subject = "Test Email"
# body = "This is a test email."

# email_text = f"From: {username}\nTo: {to}\nSubject: {subject}\n\n{body}"

# try:
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(username, password)
#     server.sendmail(username, to, email_text)
#     server.quit()
#     print("Email sent successfully!")
# except smtplib.SMTPAuthenticationError:
#     print("Failed to authenticate. Please check your credentials.")
# except Exception as e:
#     print(f"An error occurred: {e}")

try:
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    server.starttls()
    server.login("aryanchristian5@outlook.com", "9173649500Aryan")
    to = "recipient_email@example.com"
    subject = "Test Email"
    body = "This is a test email."
    email_text = f"From: {"aryanchristian5@outlook.com"}\nTo: {"rajp885050@gmail.com"}\nSubject: {"test prg"}\n\n{"test mail..."}"
    server.sendmail("aryanchristian5@outlook.com","rajp885050@gmail.com", email_text)
    server.quit()
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError as e:
    print(f"SMTP Authentication Error: {e.smtp_code} - {e.smtp_error}")
except Exception as e:
    print(f"An error occurred: {e}")


# a = "hello this is aryan"
# b = a.replace(" ","")
# print(b)