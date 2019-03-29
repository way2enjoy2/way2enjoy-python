#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import os.path
import click
import way2enjoypy

way2enjoypy.key = "pwMyPHRdvZjj2SVFDgtfxP259C6LDgYn"		# API KEY
version = "1.0.1"				# version

# Compressed core
def compress_core(inputFile, outputFile, img_width):
	source = way2enjoypy.from_file(inputFile)
	if img_width is not -1:
		resized = source.resize(method = "scale", width  = img_width)
		resized.to_file(outputFile)
	else:
		source.to_file(outputFile)

# Compress images in a folder
def compress_path(path, width):
	print "compress_path-------------------------------------"
	if not os.path.isdir(path):
		print "This is not a folder, please enter the correct path to the folder!"
		return
	else:
		fromFilePath = path 			# Source path
		toFilePath = path+"/way2enjoy" 		# Output path
		print "fromFilePath=%s" %fromFilePath
		print "toFilePath=%s" %toFilePath

		for root, dirs, files in os.walk(fromFilePath):
			print "root = %s" %root
			print "dirs = %s" %dirs
			print "files= %s" %files
			for name in files:
				fileName, fileSuffix = os.path.splitext(name)
				if fileSuffix == '.png' or fileSuffix == '.jpg' or fileSuffix == '.jpeg':
					toFullPath = toFilePath + root[len(fromFilePath):]
					toFullName = toFullPath + '/' + name
					if os.path.isdir(toFullPath):
						pass
					else:
						os.mkdir(toFullPath)
					compress_core(root + '/' + name, toFullName, width)
			break									# Traverse only the current directory

# Compress only the specified file
def compress_file(inputFile, width):
	print "compress_file-------------------------------------"
	if not os.path.isfile(inputFile):
		print "This is not a file, please enter the correct path to the file!"
		return
	print "file = %s" %inputFile
	dirname  = os.path.dirname(inputFile)
	basename = os.path.basename(inputFile)
	fileName, fileSuffix = os.path.splitext(basename)
	if fileSuffix == '.png' or fileSuffix == '.jpg' or fileSuffix == '.jpeg':
		compress_core(inputFile, dirname+"/way2enjoy_"+basename, width)
	else:
		print "This file type is not supported!"

@click.command()
@click.option('-f', "--file",  type=str,  default=None,  help="Single file compression")
@click.option('-d', "--dir",   type=str,  default=None,  help="Compressed folder")
@click.option('-w', "--width", type=int,  default=-1,    help="Image width, default")
def run(file, dir, width):
	print ("Way2enjoy Optimizer V%s" %(version))
	if file is not None:
		compress_file(file, width)				# Compress only one file
		pass
	elif dir is not None:
		compress_path(dir, width)				# Compress files in the specified directory
		pass
	else:
		compress_path(os.getcwd(), width)		# Compress files in the current directory
	print "End!"

if __name__ == "__main__":
    run()

