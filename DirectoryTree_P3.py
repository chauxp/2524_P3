#!/usr/bin/env python
#Created by Pierre Chaux
#A Program for a Directory Tree --TO EDIT


import os
import tkinter as tk

def main():
	directory = os.environ.get('HOME')
	#os.chdir(directory)
	print (os.environ.get('HOME'))
	window = tk.Tk()
	#tk._test()
	#app = tk.Window(window)
	greeting = tk.Label(text="Hello, Tkinter")
	greeting.pack()
	window.mainloop()
	
	treeGenerator(directory)
	print (os.path.basename('/home/pierrechaux/Documents.txt'))

def treeGenerator(pathName):
	print(pathName)
	for dirpath, dirnames, filenames in os.walk(pathName):
		print('dirpath:',dirpath)
		print('dirname: ',dirnames)
		print('Files: ' , filenames)
		print()
		
		
main()
