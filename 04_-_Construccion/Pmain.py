# -*- coding: UTF-8 -*-

import pygtk
pygtk.require('2.0')
import gtk


class Maincontrol:
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file("Form_Main.glade")
		self.window = self.builder.get_object("form")
		#self._btnConfiguracion = self.builder.get_object('btnConfiguracion')
		#icono = gtk.Image()
		#icono.set_from_file("icono.png")
		#self._btnConfiguracion.set_image(icono)
		self.builder.connect_signals(self)
		self.window.show_all()
	
	def click_toolbtnConfiguracion(self, widget, data=None):
		print "Configurando"

	def click_toolbtnRecuperar(self, widget, data=None):
		print "Editando"

	def click_toolbtnMensaje(self, widget, data=None):
		print "Redactando"
	
	def click_toolbtnEnviar(self, widget, data=None):
		print "Enviando"

if __name__ == "__main__":
	Maincontrol()
	gtk.main()


