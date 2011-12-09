# -*- coding: UTF-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class DConfiguracion:
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file("FormConfiguracion.glade")
		self.window = self.builder.get_object("formConfiguracion")
		self.builder.connect_signals(self)
		self._txtDominio = self.builder.get_object("txtDominio")
		self._txtAsunto = self.builder.get_object("txtAsunto")
		self._txtDominio.set_text("hotmail.com")
		self._txtAsunto.set_text("hola mundo")
		self._textoDominio = self._txtDominio.get_text()
		self._textoAsunto = self._txtAsunto.get_text()
		self._txtAsunto.set_property('editable', True)
		self.close = False
		self.fichero = open("data.txt","w")
		#self.window.show_all()
	
	def show(self):
		self.window.show_all()
	def click_btnCerrarOtro(self, widget, data=None):
		self.window.set_opacity(0.4)
		self.click_btnCerrar(self.window)
		return self.close
	def click_btnCerrar(self, widget, data=None):
		print "cerro"
		return self.close
		

	def click_btnAceptar(self, widget, data=None):
		self.click_btnCerrar(self.window)
		texto = self._txtDominio.get_text()
		if len(texto.strip()) <= 0:
			print "Mensaje error"
			return False
		else:
			self._txtDominio.set_property('editable', False)
		texto = self._txtAsunto.get_text()
		if len(texto.strip()) <= 0:
			print "Mensaje de Error"
			return False
		else:
			self._txtAsunto.set_property('editable', False)
			a = "Algo"
			self.close = True

	def click_btnRestaurar(self, widget, data=None):
		self._txtDominio.set_text(self._textoDominio)
		self._txtAsunto.set_text(self._textoAsunto)
		self._txtDominio.set_property('editable',True)
		self._txtAsunto.set_property('editable',True)
		
	def click_btnCancelar(self, widget, data=None):
		print "Cancelo"
		return True
