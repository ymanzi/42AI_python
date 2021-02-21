#!/usr/bin/python

class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.content = None
		self.file = ""
		self.header_content = ""

	def __enter__(self):
		print("enter")
		try:
			self.file = open(self.filename, "r")
			self.content = [elem.split(self.sep) for elem in self.file.read().split('\n')]
			if (self.header):
				self.header_content = self.content.pop(0)
			if (self.skip_top and len(self.content) >= self.skip_top):
				del self.content[:self.skip_top]
				self.skip_top = 0
			while (len(self.content) and self.skip_top):
				self.content.remove(self.content[0])
				self.skip_top -= 1
			if (self.skip_bottom and len(self.content) >= self.skip_bottom):
				del self.content[-self.skip_bottom:]
				self.skip_bottom = 0
			while (len(self.content) and self.skip_bottom):
				self.content.remove(self.content[-1])
				self.skip_bottom -= 1
			size_line = len(self.content[0])
			for elem in self.content:
				if size_line != len(elem):
					return None
			return self
		except Exception:
			print("Error occured: The file can't be open", )
			return None

	def __exit__(self, exc_type, exc_value, exec_traceback):
		print("exit")
		if type(self.content) != type(None):
			self.file.close()
	
	def getdata(self):
		return self.content

	def getheader(self):
		return self.header_content

	



