##import smtplib
##from email.message import EmailMessage
##
##with open('email_id.txt','r') as f:
##    email = next(f)
##    pas = next(f)
##
##msg = EmailMessage()
##msg['Subject'] = 'Testing mail sending'
##msg['TO'] = 'manav.upflairs@gmail.com'
##msg['from'] = 'manav.upflairs@gmail.com'
##msg.set_content('hey! whats up..have to complete 1 task:GUI for email client')
##
##server = smtplib.SMTP_SSL('smtp.gmail.com',465)
##server.login(email,pas)
##server.send_message(msg)
##server.quit()


########## Image ############

##import smtplib
##from email.message import EmailMessage
##import imghdr
##
##with open('email_id.txt','r') as f:
##    email = next(f)
##    pas = next(f)
##
##msg = EmailMessage()
##msg['Subject'] = 'Testing mail sending'
##msg['TO'] = 'manav.upflairs@gmail.com'
##msg['from'] = 'manav.upflairs@gmail.com'
##msg.set_content('hey! whats up..have to complete 1 task:GUI for email client')
##
##
##with open('cars_heatmap.PNG','rb') as f1:
##    file_data = f1.read()
##    file_type = imghdr.what(f1.name)
##    file_name = f1.name
##
##msg.add_attachment(file_data,maintype='image',subtype=file_type,
##                       filename=file_name)
##
##
##
##server = smtplib.SMTP_SSL('smtp.gmail.com',465)
##server.login(email,pas)
##server.send_message(msg)
##server.quit()



######## pdf #########

##import smtplib
##from email.message import EmailMessage
##
##with open('email_id.txt','r') as f:
##    email = next(f)
##    pas = next(f)
##
##msg = EmailMessage()
##msg['Subject'] = 'Testing mail sending'
##msg['TO'] = 'manav.upflairs@gmail.com'
##msg['from'] = 'manav.upflairs@gmail.com'
##msg.set_content('hey! whats up..have to complete 1 task:GUI for email client')
##
##with open('DataTypes25 ques.pdf','rb') as f1:
##    file_data = f1.read()
##    file_name = f1.name
##msg.add_attachment(file_data,maintype='application',subtype='octet-stream',
##                               filename=file_name)
##
##
##server = smtplib.SMTP_SSL('smtp.gmail.com',465)
##server.login(email,pas)
##server.send_message(msg)
##server.quit()



######### Multiple Recipient ########
##
##import smtplib
##from email.message import EmailMessage
##
##with open('email_id.txt','r') as f:
##    email = next(f)
##    pas = next(f)
##
##recipients = ['manav.upflairs@gmail.com','yudhisthir1998@gmail.com','ravibarwar77@gmail.com']
##
##msg = EmailMessage()
##msg['Subject'] = 'Testing mail sending'
##msg['TO'] = recipients
##msg['from'] = 'manav.upflairs@gmail.com'
##msg.set_content('hey! whats up..have to complete the excercises')
##
##
##with open('DataTypes25 ques.pdf','rb') as f1:
##    file_data = f1.read()
##    file_name = f1.name
##msg.add_attachment(file_data,maintype='application',subtype='octet-stream',
##                                   filename=file_name)
##
##
##server = smtplib.SMTP_SSL('smtp.gmail.com',465)
##server.login(email,pas)
##server.send_message(msg)
##server.quit()

####### Receiving Mail ##########
##
from imap_tools import MailBox

with MailBox('imap.gmail.com').login(email,pas,'INBOX') as mailbox:
    bodies = [msg.text or msg.html for msg in mailbox.fetch()]








