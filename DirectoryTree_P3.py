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
	
	test.getContents()
	
	window.mainloop()
	print(test.getRoot())
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
		windowFrame = tk.Frame(master) ##tk master window passed through constructor
		self.rootDirectory = rootDirectory
		os.chdir(self.rootDirectory)
		self.subpaths = subpaths
		self.master = master
		self.getDatafromRoot()

		
	def push(self, x): #append to subpaths
		self.subpaths.append(x)	
	
	def pop(self): ##pop from subpaths
		x = self.subpaths[-1]
		del self.subpaths[-1]
		return x
		
	def selectFolder(self,PathName): #when a folder is selected, the options change
		return 0
	
	def selectFile(self,PathName): #when a file is selected, the options change
		return 0
		
	def getContents(self): #returns contents of array -for testing
		print(self.subpaths)
		print(len(self.subpaths))
		
	def changeRoot(self,newRoot): #set new root
		self.rootDirectory = newRoot
		os.chdir(self.rootDirectory)
		
	def getRoot(self): #gets root name
		return self.rootDirectory
	
	def getDatafromRoot(self): #stores all subdirectories in subpaths list, with the name in the first index of the list, followed by (if they are a directory) their own subdirectories
		rootName = self.rootDirectory
		##treeGenerator(rootName):
		#print(rootName)
		#print(os.listdir())
	
		for path in os.listdir():
			pathName = os.path.join(rootName,path)
			subdirs = []
			
			
			if os.path.isdir(pathName): ##IF IT IS A DIRECTORY
				#print('THIS IS A DIRECTORY: ', path)
				subdirs.append(pathName)
				for subpath in os.listdir():
					subName = os.path.join(pathName,subpath)
					subdirs.append(subName)
										
				#print('THESE ARE THE SUBDIRECTORIES: ')
				#print(os.listdir(pathName))
				#self.push(subdirs)
					
			elif os.path.isfile(pathName): ##IF IT IS A FILE
				#print('THIS IS A FILE: ', path)
				subdirs.append(pathName)
					
			else: ##IF IT IS NEITHER
				print('THIS IS NOTHING: ', pathName)
		
			self.push(subdirs)
			#os.chdir(self.rootDirectory)
			
	def makeGUI(self):
		return 0
		
	
		
		
	
#def toggleFileButton(self, selected):
	
	
		

	
		
main()
