# -*- coding: UTF-8 -*-

import pygtk
pygtk.require('2.0')
import gtk


class Maincontrol:
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file("form_main.glade")
		self.window = self.builder.get_object("form")
		self._btnConfiguracion = self.builder.get_object('btnConfiguracion')
		self.builder.connect_signals(self)
		self.window.show_all()
	
	def click_btnConfiguracion(self, widget, data=None):
		print "Configurando"

	def click_btnRecuperar(self, widget, data=None):
		print "Editando"

	def click_btnRedactar(self, widget, data=None):
		print "Redactando"
	
	def click_btnEnviar(self, widget, data=None):
		print "Enviando"

if __name__ == "__main__":
	Maincontrol()
	gtk.main()


