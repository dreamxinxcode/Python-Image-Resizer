from PIL import Image 
import time

basewidth = input("Enter your desired basewidth:")

def action():
	#basewidth = 300 
	bar = progressbar.ProgressBar()
	img = Image.open('somepic.jpg')
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), Image.ANTIALIAS)
	img.save('New.jpg') 
	pbar.finish()

action()