# -*- coding: UTF-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class DConfiguracion:
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file("FormConfiguracion.glade")
		self.window = self.builder.get_object("formConfiguracion")
		#self.builder.connect_signals(self)
		#self.window.show_all()
	
	def show(self):
		self.window.show_all()
	
	

