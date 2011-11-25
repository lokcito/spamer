# -*- coding: UTF-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class DRecuperar:
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file("FormRecuperar.glade")
		self.window = self.builder.get_object("formRecuperar")
		self.builder.connect_signals(self)
	
	def show(self):
		self.window.show_all()
	
	def click_btnCancelar(self, widget, data=None):
		self.set_progreso(self,0)
		print "cancelado"

	def click_btnEmpezar(self, widget, data=None):
		print "Empezar"

	def set_progreso(self,value):
		_progreso = self.builder.get_object("pgProgreso")
		_progreso.set_fraction(value)
	
	def get_progreso(self,value):
		_progreso = self.builder.get_object("pgProgreso")
		return _progreso.set_fraction()
	
	
