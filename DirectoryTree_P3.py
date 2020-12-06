#!/usr/bin/env python
#Created by Pierre Chaux
#A Program for a Directory Tree --TO EDIT


import os

def main():
	directory = '/home/pierrechaux/Documents/'
	os.chdir(directory)
	print (dir(os.path))
	
	treeGenerator(directory)
	print (os.path.basename('/home/pierrechaux/Documents.txt'))

def treeGenerator(pathName):
	for dirpath, dirnames, filenames in os.walk(pathName):
		print('dirpath:',dirpath)
		print('dirname: ',dirnames)
		print('Files: ' , filenames)
		print()
		
		
main()
