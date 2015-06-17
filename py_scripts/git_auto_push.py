#!/usr/bin/python -tt

from PyQt4 import QtGui
import sys
import os

foldername = {}

def git_pull_push(dictionary,length) :
	for j in range(length) :
		name = dictionary[j]
		dirs = os.listdir(name)
		if ".git" in dirs :
			os.chdir(name)
			returnval1 = os.system("git pull")
			returnval2 = os.system("git push -u origin --all")

if __name__ == "__main__" :

	app = QtGui.QApplication(sys.argv)
	
	widget = QtGui.QWidget()
	widget.resize(500, 250)
		
	screen = QtGui.QDesktopWidget().screenGeometry()
	widget_size = widget.geometry()
	
	widget.move((screen.width()-widget_size.width())/2,(screen.height()-widget_size.height())/2)
		
	widget.setWindowTitle('https://github.com/OpenSourceOrganisation/')
	# widget.setWindowIcon(QtGui.QIcon('exit.png'))
	
	if foldername == {} :
		i = 0
		while True : 
			name = QtGui.QFileDialog.getExistingDirectory(widget,'Choose a GIT directory')
			if name :
				foldername[i] = str(name)
				i = i + 1
			else :
				# do the real task here
				break
	
	print foldername
	git_pull_push(foldername,i)

	
	
			
				
				
