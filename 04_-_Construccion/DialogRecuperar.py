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
		#self.window.show_all()
	
	def show(self):
		self.window.show_all()
	
	def click_btnCancelar(self, widget, data=None):
		print "cancelado"

	def click_btnEmpezar(self, widget, data=None):
		
		_progreso = self.builder.get_object("pgProgreso")
		_progreso.set_fraction(0.5)
		
		print "Empezar"
	
	

