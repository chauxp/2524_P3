#!/usr/bin/env python
#Created by Pierre Chaux
#ECE 2524 Project 3
#A Program for a Directory Tree --TO EDIT


import os
import tkinter as tk



def main():
	directory = os.environ.get('HOME') 
	os.chdir(directory) #os set to home directory
	
	#os.chdir(directory)
	print (os.environ.get('HOME'))
	window = tk.Tk() #create tk window
	#tk._test()
	#app = tk.Window(window)
	greeting = tk.Label(text="Hello, Tkinter") 
	greeting.pack()
	window.mainloop()
	
	treeGenerator(directory)
	print (os.path.basename('/home/pierrechaux/Documents.txt'))

def treeGenerator(rootName):
	print(rootName)
	print(os.listdir())
	
	for path in os.listdir():
		pathName = os.path.join(rootName,path)
		if os.path.isdir(pathName):
			print('THIS IS A DIRECTORY: ', path)
			
			print('THESE ARE THE SUBDIRECTORIES: ')
			print(os.listdir(pathName))
			
		elif os.path.isfile(pathName):
			print('THIS IS A FILE: ', path)
		else:
			print('THIS IS NOTHING: ', pathName)
	

	
	
	
	#for dirpath, dirnames, filenames in os.walk(rootName):
	#	print('dirpath:',dirpath)
	#	print('dirname: ',dirnames)
	#	print('Files: ' , filenames)
	#	print()
		

	
		
main()
