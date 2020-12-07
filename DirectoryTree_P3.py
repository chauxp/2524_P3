#!/usr/bin/env python
#Created by Pierre Chaux
#ECE 2524 Project 3
#A Program for a Directory Tree --TO EDIT


import os
import tkinter as tk

#create tk window
window = tk.Tk() 
mainframe = tk.Frame(window)
#folderImg = tk.PhotoImage(file='./freefoldericon.png') 
#fileImg = tk.PhotoImage(file='./freefileicon.png')

def main():
	directory = os.environ.get('HOME') 
	#os.chdir(directory) #os set to home directory
	
	
	
	test = DirectoryTreeGUI()
	
	test.getContents()
	#commandlinebutton = tk.Button
	#outputFileButton = tk.Button
	guiButton = tk.Button
	
	
	print(test.getRoot())
	#tk._test()
	#app = tk.Window(window)
	greeting = tk.Label(text="Hello, Tkinter") 
	greeting.pack()
	test.printFullDir()
	
	
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
	def __init__ (self, rootDirectory= os.environ.get('HOME'), subpaths=[]):
		#windowFrame = tk.Frame(master) ##tk master window passed through constructor
		#
		self.rootDirectory = rootDirectory
		
		
		os.chdir(self.rootDirectory)
		self.subpaths = subpaths
		#self.master = master
		self.getDatafromRoot()
		self.makeGUI()
		
		self.selectedPath=rootDirectory
		
		#self.currSelect = currSelect
		##self.currSelect= tk.Button(self, image = self.selectFolderImg, command=self.changeSelection(self.selectedPath))
		
		

		
	def push(self, x): #append to subpaths
		self.subpaths.append(x)	
	
	def pop(self): ##pop from subpaths
		x = self.subpaths[-1]
		del self.subpaths[-1]
		return x
		
	def selectFolder(self,PathName): #when a folder is selected, the options change
		return 0
	
	
	def printToCommandLine(self):
		print(self.getRoot)
		for array in self.subpaths:
			i=0
			for path in array:
				if(i==0):
					print("\t",path)
					
				else:
					print("\t\t",path)
				i+=1
	
	def printFullDir(self):
		print(self.getRoot)
		for array in self.subpaths:
			i=1
			for path in array:
				if(i==1):
					print("\t"*i,path)
					i+=1
					
				else:
					print("\t"*i,path)
				
	
	def selectFile(self,PathName): #when a file is selected, the options change
		return 0
		
	def getContents(self): #returns contents of array -for testing
		return self.subpaths
		
	def dataClear(self):
		self.subpaths=[]
	
	def changeRoot(self,newRoot): #set new root
		self.rootDirectory = newRoot
		os.chdir(self.rootDirectory)
		self.getDatafromRoot()
		self.makeGUI()
		
	def getRoot(self): #gets root name
		return self.rootDirectory
	
	#def search(self, searched)
	
	def getDatafromRoot(self): #stores all subdirectories in subpaths list, with the name in the first index of the list, followed by (if they are a directory) their own subdirectories
		self.dataClear()
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
				for subpath in os.listdir(): ##for its subdirectories
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
			
	def makeGUI(self): ##to create gui
		mainframe.pack_forget()
		buttext =self.getRoot()
		rootbutton = tk.Button(window, text=buttext)
		rootbutton.pack()
	
		for array in self.subpaths:
			i=0
			for path in array:
				pathName = os.path.join(self.getRoot(),path)
				if os.path.isdir(pathName): ##IF IT IS A DIRECTORY
					if(i==0):
						directorybutton = tk.Button(window, text=path, command=self.changeRoot(path))
						directorybutton.pack()
					else:
						subdirbutton = tk.Button(window, text=path, command=self.changeRoot(path))
						subdirbutton.pack()
					i+=1
				elif os.path.isfile(pathName): ##IF IT IS A FILE
					if(i==0):
						directorybutton = tk.Button(window, text=path)
						directorybutton.pack()
					else:
						
						subdirbutton = tk.Button(window, text=path)
						subdirbutton.pack()
		
		window.mainloop()
		
	"""	
class buttonIcon:
	def __init__ (self):
		self.selected_IMG = tk.PhotoImage(file=
		
	def isDirectory(self):
		return bool(True)
		
	def returnPath(self):
		
		"""
		
	
#def toggleFileButton(self, selected):
	
	
		

	
		
main()
