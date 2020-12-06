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
	#print (os.environ.get('HOME'))
	window = tk.Tk() #create tk window
	test = DirectoryTreeGUI(window)
	test.getDatafromRoot()
	test.getContents()
	window.mainloop()
	#tk._test()
	#app = tk.Window(window)
	greeting = tk.Label(text="Hello, Tkinter") 
	greeting.pack()
	
	
	#treeGenerator(directory)
	
	#print (os.path.basename('/home/pierrechaux/Documents.txt'))

def treeGenerator(rootName):
	#print(rootName)
	#print(os.listdir())
	test = DirectoryTreeGUI()
	test.getDatafromRoot()
	test.getContents()
	window.mainloop()
	
	"""
	for path in os.listdir():
		pathName = os.path.join(rootName,path)
		if os.path.isdir(pathName): ##IF IT IS A DIRECTORY
			print('THIS IS A DIRECTORY: ', path)
			
			print('THESE ARE THE SUBDIRECTORIES: ')
			print(os.listdir(pathName))
			
		elif os.path.isfile(pathName): ##IF IT IS A FILE
			print('THIS IS A FILE: ', path)
			
		else: ##IF IT IS NEITHER
			print('THIS IS NOTHING: ', pathName)
	
"""
	
	
	
	#for dirpath, dirnames, filenames in os.walk(rootName):
	#	print('dirpath:',dirpath)
	#	print('dirname: ',dirnames)
	#	print('Files: ' , filenames)
	#	print()
"""	
def toggleDirButton(but, selected):
	if but.button['image'] == True:
		but.button['image'] = tk.PhotoImage(file='freefoldericon.jpg')
	
	else:
		but.button['image'] = tk.PhotoImage(file='freefoldericon-selected.jpg')
	"""

class DirectoryTreeGUI:
	def __init__ (self, master, rootDirectory= os.environ.get('HOME'), subpaths=[]):
		myFrame = tk.Frame(master)
		self.rootDirectory = rootDirectory
		os.chdir(self.rootDirectory)
		self.subpaths = subpaths
		self.master = master
		#self.getDatafromRoot()

		
	def push(self, x):
		self.subpaths.append(x)
		
	def setRoot(self, rootDir):
		self.rootDirectory = rootDir
	
	def getRoot(self):
		return self.rootDirectory
		
	def pop(self):
		x = self.items[-1]
		del self.items[-1]
		return x
		
	def empty(self):
		return len(self.items)== 0
		
	def selectFolder(self,PathName):
		return 0
	
	def selectFile(self,PathName):
		return 0
	
	def changeRoot(self, RootName):
		return 0
		
	def getContents(self):
		print(self.subpaths)
		print(len(self.subpaths))
	
	def getDatafromRoot(self):
		rootName = self.rootDirectory
		##treeGenerator(rootName):
		#print(rootName)
		#print(os.listdir())
	
		for path in os.listdir():
			pathName = os.path.join(rootName,path)
			subdirs = []
			
			
			if os.path.isdir(pathName): ##IF IT IS A DIRECTORY
				print('THIS IS A DIRECTORY: ', path)
				subdirs.append(pathName)
				for subpath in os.listdir():
					subName = os.path.join(pathName,subpath)
					subdirs.append(subName)
										
				print('THESE ARE THE SUBDIRECTORIES: ')
				print(os.listdir(pathName))
				self.push(subdirs)
					
			elif os.path.isfile(pathName): ##IF IT IS A FILE
				print('THIS IS A FILE: ', path)
				subdirs.append(pathName)
					
			else: ##IF IT IS NEITHER
				print('THIS IS NOTHING: ', pathName)
		
		#self.push(subdirs)
		
	
		
		
	
#def toggleFileButton(self, selected):
	
	
		

	
		
main()
