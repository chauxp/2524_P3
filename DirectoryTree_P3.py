#!/usr/bin/env python
#Created by Pierre Chaux
#ECE 2524 Project 3
#A Program for a Directory Tree GUI that i show all the subdirectories and files down from a directory. It begins with the home directory and any directory clicked will be the root in a new window


import os
import tkinter as tk
#from tkinter import ttk
from functools import partial


def main():
	directory = os.environ.get('HOME') 
	#os.chdir(directory) #os set to home directory
	
	
	test = DirectoryTreeGUI()
	
	


class DirectoryTreeGUI:
	def __init__ (self, rootDirectory= os.environ.get('HOME'), subpaths=[]):
		
		self.rootDirectory = rootDirectory
				
		os.chdir(self.rootDirectory)
		self.subpaths = subpaths
		#self.master = master
		self.getDatafromRoot()
		self.makeGUI()
		
		self.selectedPath=rootDirectory
		


		
	def push(self, x): #append to subpaths
		self.subpaths.append(x)	
	
	
	
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
		os.chdir(newRoot)
		self.getDatafromRoot()
		self.makeGUI()
		
	def getRoot(self): #gets root name
		return self.rootDirectory
		
	def fileSelection(self):
		print("This is only a file, it cannot be accessed")
	
	#def search(self, searched)
	
	def getDatafromRoot(self): #stores all subdirectories in subpaths list, with the name in the first index of the list, followed by (if they are a directory) their own subdirectories
		self.dataClear()
		rootName = self.rootDirectory
		
	
		for path in os.listdir():
			pathName = os.path.join(rootName,path)
			subdirs = [] 
			
			
			if os.path.isdir(pathName): ##IF IT IS A DIRECTORY
				
				subdirs.append(pathName)
				for subpath in os.listdir(): ##for its subdirectories
					subName = os.path.join(pathName,subpath)
					subdirs.append(subName)
					
			elif os.path.isfile(pathName): ##IF IT IS A FILE
				
				subdirs.append(pathName)
					
			else: ##IF IT IS NEITHER
				print('This is neither a directory nor a file: ', pathName)
		
			self.push(subdirs)
			os.chdir(self.rootDirectory)
			
	def makeGUI(self): ##to create gui
		##mainframe.destroy()
		window = tk.Tk()
		window.geometry("500x400")
		
		window.title("File Directory GUI.")
		fileButton = tk.Label(window, text="Root: "+self.getRoot())
		fileButton.grid(padx=(0,0), sticky='nw')
		
		#mainframe = tk.Frame(window)
		#mainframe.pack(fill="both", expand="1")
		
		#canvas = tk.Canvas()
		#canvas.pack(side="left",fill="both", expand="1")
		
		#scrollbar = tk.Scrollbar(mainframe, orient="vertical", command=canvas.yview)
		#scrollbar.pack(side="right", fill ="y")
		
		#canvas.configure(yscrollcommand=scrollbar)
		#canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
		
		#secondframe = tk.Frame(canvas)
		
		#canvas.create_window((0,0), window=secondframe, anchor = "nw")
		
		#window = ttk.Frame(tkBox)
		#canvas = tk.Canvas(window)
		
		#scrollableframe = ttk.Frame(canvas)
		#canvas.configure(yscrollcommand=scrollbar)
		
		
		buttext =self.getRoot()
		#rootbutton = tk.Button(window, text=buttext)
		#rootbutton.pack()
		#buttons = {}
		#x=0
		
		for array in self.subpaths:
			i=0
			for path in array:
				fullPath = os.path.join(self.getRoot(),path)
				if os.path.isdir(path): #and not("." in path): ##IF IT IS A DIRECTORY
					if(i==0):
						directoryButton = tk.Button(window, text=path, command= partial(self.changeRoot,fullPath)) #Call changeroot to make a new window with new root
						directoryButton.grid(padx=(70,0), sticky='nw')
						#directoryButton.pack()
						
					else:
						subdirButton = tk.Button(window, text=path, command= partial(self.changeRoot, fullPath)) #Call changeroot to make a new window with new root
						
						subdirButton.grid(padx=(170,0), sticky='nw')
						#subdirButton.pack()
					i+=1
				elif os.path.isfile(fullPath): ##IF IT IS A FILE
					if(i==0):
						fileButton = tk.Label(window, text=path)
						fileButton.grid(padx=(70,0), sticky='nw')
						#fileButton.pack()
						
					else:
						subfileButton = tk.Label(window, text=path)
						subfileButton.grid(padx=(170,0), sticky='nw')
						#subfileButton.pack()
						
					i+=1
			
		
		window.mainloop()

		

	
		
main()
