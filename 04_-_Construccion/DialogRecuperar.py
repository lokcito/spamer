# -*- coding: UTF-8 -*-

import sys
import re
import string
import httplib
import urllib2
import re

import pygtk
pygtk.require('2.0')
import gtk
from Data import Data

class DRecuperar:
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file("FormRecuperar.glade")
		self.window = self.builder.get_object("formRecuperar")
		self._lblDominio = self.builder.get_object("txtDominio")
		self.builder.connect_signals(self)
		self.datos = Data("cv.txt")
		self.datos.file_to_open()
		texto = self.datos.read_to_file()
		texto = self.datos.split_to_string(texto,"\n")
		datos=[self.datos.split_to_string(texto[0],":"),
			self.datos.split_to_string(texto[1],":"),
		]
		self._lblDominio.set_text(datos[0][1].strip())
		
	def show(self):
		self.window.show_all()
	
	def click_btnCancelar(self, widget, data=None):
		self.set_progreso(self,0)
		print "cancelado"

	def click_btnEmpezar(self, widget, data=None):
		self.search_GoogleGroups()
		self.guardarMails()
		#self.mostrarMails()

	def set_progreso(self,value):
		_progreso = self.builder.get_object("pgProgreso")
		_progreso.set_fraction(value)
	
	def get_progreso(self,value):
		_progreso = self.builder.get_object("pgProgreso")
		return _progreso.set_fraction()
		
	def search_GoogleGroups(self):
		self.d={}
		page_counter = 0.0
		try:
			while page_counter < 1 :
				print "xD"
				results = 'http://groups.google.com/groups?q=' + str('hotmail.com')+'&hl=en&lr=&ie=UTF-8&start=' + repr(page_counter) + '&sa=N'
				request = urllib2.Request(results)
				request.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)')
				opener = urllib2.build_opener()
				text = opener.open(request).read()
				emails = (re.findall('([\w\.\-]+@'+'hotmail.com'+')',self.StripTags(text)))
				for email in emails:
					self.d[email]=1
					uniq_emails=self.d.keys()
				page_counter = page_counter + 0.2
				print str(page_counter)
				self.set_progreso(page_counter)
				
		except IOError:
			print "Can't connect to Google Groups!"+""
    
	def StripTags(self,text):
		finished = 0
		while not finished:
			finished = 1
			start = text.find("<")
			if start >= 0:
				stop = text[start:].find(">")
				if stop >= 0:
					text = text[:start] + text[start+stop+1:]
					finished = 0
		return text
	
	def mostrarMails(self):
		for uniq_emails_web in self.d.keys():
			print uniq_emails_web+""
	def guardarMails(self):
		strmail = ""
		for uniq_emails_web in self.d.keys():
			uniq_emails_web=uniq_emails_web.replace(" ",".")
			strmail += uniq_emails_web + "\n"
		filename = 'mails/mail.txt'
		ram = open(filename,'w')
		ram.write(str(strmail))
		ram.close()
		
		
		
