# -*- coding: UTF-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
from Data import Data

class DConfiguracion:
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file("FormConfiguracion.glade")
		self.window = self.builder.get_object("formConfiguracion")
		self.builder.connect_signals(self)
		self._txtDominio = self.builder.get_object("txtDominio")
		self._txtAsunto = self.builder.get_object("txtAsunto")
		self._txtAsunto.set_property('editable', True)
		self.close = False
		self.datos = Data('cv.txt')
		self.datos.file_to_open()
		texto = self.datos.read_to_file()
		texto = self.datos.split_to_string(texto,"\n")
		datos=[self.datos.split_to_string(texto[0],":"),
				self.datos.split_to_string(texto[1],":"),
		]
		self._txtDominio.set_text(datos[0][1].strip())
		self._txtAsunto.set_text(datos[1][1].strip())
		self._textoDominio = self._txtDominio.get_text()
		self._textoAsunto = self._txtAsunto.get_text()
		#self.fichero = open("data.txt","w")
		#self.window.show_all()
	
	def show(self):
		self.window.show_all()
#	def click_btnCerrarOtro(self, widget, data=None):
#		return self.close
#	def click_btnCerrar(self, widget, data=None):
#		return self.close
		

	def click_btnAceptar(self, widget, data=None):
		texto = self._txtDominio.get_text()
		if len(texto.strip()) <= 0:
			print "Mensaje error"
			return False
		else:
			#self._txtDominio.set_property('editable', False)
			self._txtDominio.set_text(str(texto.strip()))
		texto = self._txtAsunto.get_text()
		if len(texto.strip()) <= 0:
			print "Mensaje de Error"
			return False
		else:
			self._txtAsunto.set_text(str(texto.strip()))
			#self._txtAsunto.set_property('editable', False)
			self.datos.file_to_open()
			texto = self.datos.read_to_file()
			texto = self.datos.split_to_string(texto,"\n")
			datos=[self.datos.split_to_string(texto[0],":"),
					self.datos.split_to_string(texto[1],":"),
			]
			datos[0][1] = self._txtDominio.get_text()
			datos[1][1] = self._txtAsunto.get_text()
			strout = datos[0][0] +":"+ datos[0][1] + "\t\t\t\t\t" + "\n"
			strout += datos[1][0] + ":" + datos[1][1] + "\t\t\t\t\t"
			self.datos.write_to_file(strout)
			self.datos.file_to_close()
			self.close = True

	def click_btnRestaurar(self, widget, data=None):
		self._txtDominio.set_text(self._textoDominio)
		self._txtAsunto.set_text(self._textoAsunto)
		#self._txtDominio.set_property('editable',True)
		#self._txtAsunto.set_property('editable',True)
		self.datos.file_to_open()
		texto = self.datos.read_to_file()
		texto = self.datos.split_to_string(texto,"\n")
		datos=[self.datos.split_to_string(texto[0],":"),
				self.datos.split_to_string(texto[1],":"),
		]
		datos[0][1] = self._txtDominio.get_text()
		datos[1][1] = self._txtAsunto.get_text()
		strout = datos[0][0] +":"+ datos[0][1] + "\t\t\t\t\t" + "\n"
		strout += datos[1][0] + ":" + datos[1][1] + "\t\t\t\t\t"
		self.datos.write_to_file(strout)
		self.datos.file_to_close()
		self.close = True

	def click_btnCancelar(self, widget, data=None):
		print "Cancelo"
		return True
