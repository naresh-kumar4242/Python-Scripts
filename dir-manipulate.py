#In this script we will create directories & files using Python and manipuate them!

import os
import time
import glob

def createFolders(BASE_DIR):
    ''' This function creates directories '''
    for i in range(10):
            os.mkdir(BASE_DIR + str(i) + '-Folder')

def createFiles(BASE_DIR):
    ''' This function creates .txt files '''
    for i in range(10):
        f = open(BASE_DIR + str(i) + 'Folder.txt', 'w')
        f.close()

def renameFiles(BASE_DIR):
    ''' This function renames files '''
    os.chdir(BASE_DIR) #Change directory to list the files
    for i in glob.glob('*.txt'):
        #print i
        os.rename(i, i.replace('Folder', '-Folder'))

if __name__ == '__main__':
    BASE_DIR = '/home/z0x/Dropbox/Python/reboot/test/'
    createFolders(BASE_DIR)
    createFiles(BASE_DIR)
    time.sleep(10)
    renameFiles(BASE_DIR)
