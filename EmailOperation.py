import smtplib
import imapclient
import pyzmail36

conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)
conn
conn.ehlo()     # send out internet traffic
conn.starttls()
conn.login('alenyin0403@gmail.com', 'blablabla')

conn.sendmail('alenyin0403@gmail.com'       # from the email address
              'alenyim0403@hotmail.com'     # to the email address
              'Subject: So long...\n\nDear Al, \nSo long, and thanks for all the fish.\n\n-Al')
# need to insert two line between subject and main body

conn.quit()     # closing connection


# checking email
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)    # using ssl encryption
conn.login('alenyin0403@gmail.com', 'fejwioajfeoiwa')
conn.select_folder('INBOX', readonly=True)                  # we want read only unless we want to delete emails

UIDs = conn.search(['SINCE 20-Aug-2015'])                   # get emails from 20 Aug 2015, returning the IDs

rawMessage = conn.fetch([47474], ['BODY[]', 'FLAGS'])

message = pyzmail36.PyzMessage.factory(rawMessage[47474][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')
message.text_part   # to check if the content in the body is in pure text form
message.html_part   # or if it is under html form

message.text_part.get_payload().decode('UTF-8')

conn.list_folders()     # list of folders in the email