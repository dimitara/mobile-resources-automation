from PIL import Image, ImageDraw
import os
import sys, getopt
import argparse

icons = {
	'android': [
		{'size': (72,72), 'path': 'icon-72-hdpi.png'},
		{'size': (96,96), 'path': 'icon-96-xhdpi.png'}
	],
	'ios': [
		{'size': (173,173), 'path': 'icon-40.png'},
		{'size': (173,173), 'path': 'icon-40@2x.png'},
		{'size': (173,173), 'path': 'icon-50.png'},
		{'size': (173,173), 'path': 'icon-50@2x.png'},
		{'size': (60,60), 'path': 'icon-60.png'},
		{'size': (120,120), 'path': 'icon-60@2x.png'},
		{'size': (72,72), 'path': 'icon-72.png'},
		{'size': (144,144), 'path': 'icon-72@2x.png'},
		{'size': (76,76), 'path': 'icon-76.png'},
		{'size': (152,152), 'path': 'icon-76@2x.png'},
		{'size': (29,29), 'path': 'icon-small.png'},
		{'size': (58,58), 'path': 'icon-small@2x.png'},
		{'size': (57,57), 'path': 'icon.png'},
		{'size': (114,114), 'path': 'icon@2x.png'}
	],
	'common':[
		{'size': (128,128), 'path': 'icon.png'}
	]	
}

splashes = {
	'android': [
		{'size': (800, 480), 'path': 'screen-hdpi-landscape.png'},
		{'size': (480, 800), 'path': 'screen-hdpi-portrait.png'},
		{'size': (320, 200), 'path': 'screen-ldpi-landscape.png'},
		{'size': (200, 320), 'path': 'screen-ldpi-portrait.png'},
		{'size': (480, 320), 'path': 'screen-mdpi-landscape.png'},
		{'size': (320, 480), 'path': 'screen-mdpi-portrait.png'},
		{'size': (1280, 720), 'path': 'screen-xhdpi-landscape.png'},
		{'size': (720, 1280), 'path': 'screen-xhdpi-portrait.png'}
	],
	'ios': [
		{'size': (2008, 1536), 'path': 'screen-ipad-landscape-2x.png'},
		{'size': (1024, 783), 'path': 'screen-ipad-landscape.png'},
		{'size': (1536, 2008), 'path': 'screen-ipad-portrait-2x.png'},
		{'size': (768, 1004), 'path': 'screen-ipad-portrait.png'},
		{'size': (960, 640), 'path': 'screen-iphone-landscape-2x.png'},
		{'size': (480, 320), 'path': 'screen-iphone-landscape.png'},
		{'size': (640, 960), 'path': 'screen-iphone-portrait-2x.png'},
		{'size': (640, 1136), 'path': 'screen-iphone-portrait-568h-2x.png'},
		{'size': (640, 1136), 'path': 'Default-568h@2x~iphone.png'},
		{'size': (2048, 1536), 'path': 'Default-Landscape@2x~ipad.png'},
		{'size': (1024, 768), 'path': 'Default-Landscape~ipad.png'},
		{'size': (1536, 2048), 'path': 'Default-Portrait@2x~ipad.png'},
		{'size': (768, 1024), 'path': 'Default-Portrait~ipad.png'},
		{'size': (640, 960), 'path': 'Default@2x~iphone.png'},
		{'size': (320, 480), 'path': 'screen-iphone-portrait.png'},
		{'size': (320, 480), 'path': 'Default~iphone.png'}
	]	
}

def generateResources(sourceFile, iconFile, backgroundFile):
	print "Start generating resources"
	
	if not os.path.exists('res'):
		os.mkdir('res')

	if not os.path.exists('icons'):
		os.mkdir('icons')

	icon = Image.open(iconFile)
	icon.convert('RGBA') 

	for platform in icons:
		if not os.path.exists('icons/' + platform):
			os.chdir('icons')
			os.mkdir(platform)
			os.chdir('..')

		for item in icons[platform]:
			rIcon = icon
			rIcon = rIcon.resize(item['size'], Image.ANTIALIAS)
			
			rIcon.save('icons/' + platform + '/' + item['path'])

	splash = Image.open(sourceFile)
	splash.convert('RGBA') 
	for platform in splashes:
		if not os.path.exists('res/' + platform):
			os.chdir('res')
			os.mkdir(platform)
			os.chdir('..')

		for item in splashes[platform]:
			background = Image.new('RGBA',item['size'], (255,255,255,255))
			xOffset = background.size[0] / 2 - splash.size[0] / 2
			yOffset = background.size[1] / 2 - splash.size[1] / 2

			background.paste(splash, (xOffset,yOffset));

			background.save('res/' + platform + '/' + item['path'])


def main():
  	sourceFile = None
  	iconFile = None
	backgroundFile = None

	parser = argparse.ArgumentParser()

	parser.add_argument('-s', '--source')
	parser.add_argument('-i', '--icon')
	parser.add_argument('-b', '--background')
	#parser.add_argument('-h', '--help')
	args = parser.parse_args()

	#if args.help:
	#	print 'help'

	sourceFile = args.source
	backgroundFile = args.background
	iconFile = args.icon or sourceFile 
   
	if sourceFile != None:
   		generateResources(sourceFile, iconFile, backgroundFile)
   	else:
   		print 'usage: generate.py -s <sourcefile> -b <backgroundfile>'


if __name__ == "__main__":
   main()