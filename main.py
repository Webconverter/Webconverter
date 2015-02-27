from PIL import Image
import os.path

class Picture():
	def __init__(self, infile):
		self.infile = infile
		self.im = Image.open(infile)
	def convert(self, fileType):
		name, ext =  os.path.splitext(self.infile)
		print("Converting from {0} to {1}".format(ext, fileType))
		self.im.save(name, fileType)

p = Picture("linux.jpg")
p.convert("PNG")



