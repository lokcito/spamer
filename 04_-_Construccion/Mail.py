# -*- coding: UTF-8 -*-

import smtplib
import mimetypes
from email.MIMEText import MIMEText
from email.Encoders import encode_base64


class Mail:
	def __init__(self,fromm,contacts,subject,text):
		self.fromm = fromm
		self.text = text
		self.contacts = contacts
		self.subject = subject
		self.mensaje = MIMEText(self.text)
		self.mensaje["From"] = self.fromm
		self.mensaje["To"] = self.contacts
		self.mensaje["Subject"] = self.subject

	def connect_to_mail(self,mail,passwd):
		self.mailServer = smtplib.SMTP('smtp.gmail.com',587)
		#self.mailServer = smtplib.SMTP('smtp.200.60.61.3',587)
		self.mailServer.ehlo()
		self.mailServer.starttls()
		self.mailServer.ehlo()
		self.mailServer.login(mail,passwd)
	def send_to_mail(self):
		self.mailServer.sendmail(self.fromm,self.contacts,self.mensaje.as_string())
		self.connet_close()
	
	def connet_close(self):
		self.mailServer.close()


