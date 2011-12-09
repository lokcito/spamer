# coding: utf-8

class Data:
	def __init__(self,filee):
		self.filee = filee
		self.ram = open(self.filee,'r+')
	def file_to_open(self):
		self.ram = open(self.filee,'r+')
	def write_to_file(self,string):
		self.ram.seek(0)
		self.ram.write(str(string))
	
	def file_to_close(self):
		self.ram.close()
	
	def read_to_file(self):
		return self.ram.read()
	
	def split_to_string(self,string,patron):
		return string.split(patron)

		
