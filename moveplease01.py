#!/usr/bin/env python3
# import shutil and os module
import shutil
import os

# force the Python program to 'start' int he home user directory
os.chdir('/home/student/mycode/')

# move the file or folder at the path source to the path destination and return a string of the absolute path of the new location
shutil.move('raynor.obj', 'ceph_storage/')

#prompt the user for a new name 
xname = input('What is the new name for kerrigan.obj? ')

#Rename the current file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



