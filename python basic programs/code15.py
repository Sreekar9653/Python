import glob
import os
dir_name = 'C:/'
# Get list of files in a directory
list_of_files = filter( os.path.isfile,
                        glob.glob(  dir_name + '*') )
print(glob.glob(dir_name +"*"))
