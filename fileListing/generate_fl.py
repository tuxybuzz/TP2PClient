import os
import pickle
import sendListing
import fl_class
from fileListing import utilities

def generate_fl(root_dir, username, server_ip):
    #Generate and Store the FileListing
    fl_obj = fl_class.FileListing()   
    fl_obj.setUsername(username)
    
    os.chdir(root_dir)
    utilities.cleanListings()
    file_ls = open(username+".fls","wb")
    
    #OPEN FILES
    try:
        os.chdir('Open')
        for f_file in os.listdir('.'):
            stat = os.stat(f_file)
            fl_obj.addOpenFile(f_file, size=stat.st_size)
        os.chdir('..')
    except(OSError):
        os.mkdir('Open')
        
        
    #PRIVATE FILES
    try:
        os.chdir('Private')
        for f_file in os.listdir('.'):
            stat = os.stat(f_file)
            fl_obj.addPrivFile(f_file, size=stat.st_size)
        os.chdir('..')
    except(OSError):
        os.mkdir('Private')
        
    pickle.dump(fl_obj,file_ls)
    file_ls.close()
    sendListing.sendListing(server_ip, root_dir, username) 
    os.chdir(root_dir)   
    
    