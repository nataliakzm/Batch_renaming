#!/usr/bin/env python

# Pythono3 code to rename multiple files in a directory or folder

# importing os module
import os

def addition(f_zeros):
    final_number = int(f_zeros) + 60
    return(str(final_number))
    #For calculating the offset time

path = os.chdir('C:/your/path/to/rttm/')
#path to rttm is the absolute path to the folder containing the rttm you want to change the name

list_rttm =[ f for f in os.listdir(path) if '.rttm' in f]
#This is made to be sure that all the f elements are ending with '.rttm', so you'll not make any changes to not rttm files
#So all element of list_rttm, which are named f, should be something like: name2017_C18_C17_M1_20170718_056040.rttm

for f in list_rttm:
    
    f_name, f_rttm = os.path.splitext(f)
    #print(f_name) - It will separate the filename from its extension
    s_name = f_name.split('_')
    #print(s_name) - this and the ones below will divide each part of the name to separate “columns”
    
    f_title = s_name[0]
    #print(f_title) - Name2017
    f_chi = s_name[1]
    #print(f_chi) - the key child e.g. C18
    f_del = s_name[2]
    #print(f_del) - it will delete the sibling of the key child e.g. C17
    f_delete = s_name[3]
    #print(f_delete) - and this one deletes their mother e.g.M1
    f_day = s_name[4]
    #print(f_day) - the day of a recording e.g. 20170718
    f_onset = s_name[5]
    #print(f_onset) - the time of onsete e.g. 056040
    #In case you have more details in your filename, it's necessary to add two more columns: e.g. f_part = s_name[5] and f_recording = s_name[6]
    
    
    f_zeros = f_onset.zfill(6)
    #print(f_zeros) - adds 00 to the beginning of onset time
    f_offset = addition(f_zeros).zfill(6)
    #the offset time is the sum of the onset and 60 -> 056100
    #the number will alse be preceded by zeros
	
	#new name is name2017_C18_ 20170718_056040_056100.rtt
    #print('{}_{}_{}_{}_{}{}'.format(f_title, f_chi, f_day, f_zeros, f_offset, f_rttm))
    new_name = '{}_{}_{}_{}_{}{}'.format(f_title, f_chi, f_day, f_zeros, f_offset, f_rttm)
    #print(new_name)
    
    os.rename(f, new_name)

    
    

    
