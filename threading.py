import smtplib

smtObj = smtplib.SMTP('smtp.gmail.com', 587)
smtObj.ehlo()
smtObj.starttls()
smtObj.login('MightyGuy@gmail.com', 'PASSWORD')
smtObj.sendmail("MightyGuy@gmail.com","MightyGuy@hotmail.com",'Subject: SMTP check. \n This is a test email')
smtObj.quit()