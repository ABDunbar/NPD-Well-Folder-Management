# -*- coding: utf-8 -*-
# Diskos_move_wells.py
"""
@author: Alexander Dunbar

This will do the following;
    1. Write the current folders at the level of "folders_path" to a list (folder_list)
    2. Create a new directory 'DISKOS' at the "folders_path" level
    3. Move all files under the 'WELL' folder up one level
    4. Move all folders from "folder_list" down one level into the 'DISKOS' folder
    5. Delete the now empty 'WELL' folder from the 'DISKOS' folder

"""
def main():
    
    import os, glob, shutil
    
    """
    Use root = input() below if root directory 
    (S:\02_Wells\07_Data_Management\WellDownload_Diskos) 
    changes but directory structure below is unchanged.
    """
    ################ FILE AND DIRECTORY PATHS #######################
    #    print("Enter the absolute path up to but not including EXPLORATION level")
    #    print("EXAMPLE:  \"S:\\02_Wells\\07_Data_Management\\WellDownload_Diskos\"")
    #    
    #    root = input("Enter directory path:  ")
    #    folders_path = os.path.join(root, "*\\*\\*\\*") # EXPLORATION\1\1_3-1\<folders>
    #    diskos = os.path.join(root, "*\\*\\*") # DEVELOPMENT\9\9_2-7\<folders>
    #    files = os.path.join(root, "*\\*\\*\\WELL\\*") # PRODUCTION\6407\WELL\<files>
    #    del_well_folder = os.path.join(root, "*\\*\\*\\DISKOS\\WELL")
    
    ################ FILE AND DIRECTORY PATHS #######################
    ## folders_path refers to all folders below the individual well folder (eg 'DRILLING', 'WELL_SEISMIC', etc)
    folders_path = r"S:\02_Wells\07_Data_Management\WellDownload_Diskos\*\*\*\*"
    ## diskos refers to the folder location where the 'DISKOS' folder will be created
    diskos = r"S:\02_Wells\07_Data_Management\WellDownload_Diskos\*\*\*"
    ## files refers to all files in the 'WELL' folder
    files = r"S:\02_Wells\07_Data_Management\WellDownload_Diskos\*\*\*\WELL\*"
    ##
    del_well_folder = r"S:\02_Wells\07_Data_Management\WellDownload_Diskos\*\*\*\DISKOS\WELL"
    well_folder = r"S:\02_Wells\07_Data_Management\WellDownload_Diskos\*\*\*\WELL"
    
    ############### WELL, FILE AND FOLDER LISTS ####################
    
    no_of_wells = []             # List of all wells
    folder_list = []             # List of all folders under the well folder
    wells_with_well_folder = []  # List of wells that have 'WELL' folder
    well_files = []              # List of files under the 'WELL' folder
    
    ############## CAPTURE INFO FOR POST MOVE QC ###################
    """Total number of wells"""
    for well in glob.glob(diskos):
        no_of_wells.append(well)
    """ Number of wells that have a 'WELL' folder
    Will have a 'WELL' folder if >20 years or traded or owner """
    for well in glob.glob(well_folder):
        wells_with_well_folder.append(well)
    """ Number of files under the 'WELL' folder
    Compare this with post move result """
    for file in glob.glob(files):
        well_files.append(file)
    
    ####################### 1 ########################
    """
    ## glob returns a list containing the full directory path of each folder
    ## the location of which is specified in "folders_path"
    """
    for folder in glob.glob(folders_path):
        folder_list.append(folder)
    
    ####################### 2 ########################
    """
    ## glob returns every well folder as specified in the "diskos" path
    ## check to see if 'DISKOS' folder already exists
    ## os.mkdir creates the 'DISKOS' folder at the "diskos" path
    ## ie. at the folder level of 'DRILLING' etc
    """
    for fn in glob.glob(diskos):
        #if not os.path.isdir(fn + '\\' + 'DISKOS'):
        if not os.path.exists(fn + '\\' + 'DISKOS'):
            os.mkdir(fn + '\\' + 'DISKOS')
        else:
            print("DISKOS folder already exists")
    
    ####################### 3 ########################
    """
    ## glob will find all files in the 'WELL' folder
    ## and shutil will move those files up one level
    """
    for fn in glob.glob(files):
        #file = os.path.basename(fn)
        dirs = os.path.dirname(fn)
        updir = os.path.dirname(dirs)
        shutil.move(fn, updir)
        #print(updir +'\\'+ file)
    
    ####################### 4 ########################
    """
    ## shutil will move all the folders that were saved in
    ## "folder_list" down one level into the 'DISKOS' folder
    """
    for path in folder_list:
        #old_folder = os.path.basename(path)
        old_dir = os.path.dirname(path)
        shutil.move(path, old_dir+'\\'+'DISKOS')
        #print(old_dir+'\\'+'DISKOS')
    
    ####################### 5 ########################
    """
    ## Check that the 'WELL' folder now in the 'DISKOS' folder
    ## is empty and if so, delete it.
    """
    for well_dir in glob.glob(del_well_folder):
        # test to see if 'WELL' folder is empty
        if not os.listdir(well_dir):
            print(f"Directory {well_dir} is empty and has been deleted")
            os.rmdir(well_dir)
        else:
            print(f"Directory {well_dir} is not empty")


if __name__ == '__main__':
    main()

















