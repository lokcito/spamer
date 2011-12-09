# -*- coding: UTF-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class DMensaje:
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file("FormMensaje.glade")
		self.window = self.builder.get_object("formMensaje")
		#_txtMensaje = self.builder.get_object("entry1")
		#scroll = gtk.ScrolledWindow()
		#scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		#scroll.set_shadow_type(gtk.SHADOW_IN)
		#scroll.add(_txtMensaje)
		self.builder.connect_signals(self)

	def show(self):
		self.window.show_all()
	
