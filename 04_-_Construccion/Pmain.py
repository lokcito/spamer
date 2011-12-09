# -*- coding: UTF-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
from DialogConfiguracion import DConfiguracion
from DialogRecuperar import DRecuperar
from DialogMensaje import DMensaje

#import smtplib
#import mimetypes
#from email.MIMEText import MIMEText
#from email.Encoders import encode_base64
from Mail import Mail
a="nada"
class Maincontrol(object):
	def __init__(self):
			
		self.builder = gtk.Builder()
		self.builder.add_from_file("Form_Main.glade")
		self.window = self.builder.get_object("form")
		self.builder.connect_signals(self)
		self.window.show_all()
	
	def config(self, dominio, asunto):
		self.dominio = dominio
		self.asunto = asunto

	def click_toolbtnConfiguracion(self, widget, data=None):
		wConfiguracion = DConfiguracion()
		saveW = wConfiguracion.show()
		#if wConfiguracion.window.hide_on_delete():
		if True:
			print "d"
		else:
			print "c"
		print "xD"

	def click_toolbtnRecuperar(self, widget, data=None):
		wRecuperar = DRecuperar()
		wRecuperar.show()

	def click_toolbtnMensaje(self, widget, data=None):
		wMensaje = DMensaje()
		wMensaje.show()
		print a
	
	def click_toolbtnEnviar(self, widget, data=None):
		sMail = Mail("enciso.leo@hotmail.com","enciso.leo@gmail.com,leo_14_4@hotmail.com","Hola mundo de leo","Si hola mundo de leo.")
		sMail.connect_to_mail("leo.enciso@gmail.com","lloekocito_14@gmail.com")
		sMail.send_to_mail()

if __name__ == "__main__":
	Maincontrol()
	gtk.main()



