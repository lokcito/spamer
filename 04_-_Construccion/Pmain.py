# -*- coding: UTF-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
from DialogConfiguracion import DConfiguracion
from DialogRecuperar import DRecuperar
from DialogMensaje import DMensaje

class Maincontrol:
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file("Form_Main.glade")
		self.window = self.builder.get_object("form")
		self.builder.connect_signals(self)
		self.window.show_all()
	
	def click_toolbtnConfiguracion(self, widget, data=None):
		wConfiguracion = DConfiguracion()
		wConfiguracion.show()

	def click_toolbtnRecuperar(self, widget, data=None):
		wRecuperar = DRecuperar()
		wRecuperar.show()

	def click_toolbtnMensaje(self, widget, data=None):
		wMensaje = DMensaje()
		wMensaje.show()
	
	def click_toolbtnEnviar(self, widget, data=None):
		print "Enviando"

if __name__ == "__main__":
	Maincontrol()
	gtk.main()


