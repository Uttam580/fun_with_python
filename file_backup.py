
import os , sys , datetime
import shutil

def take_bkp(src_file_loc,src_file_name,bkp_file_loc,bkp_file_name):
    try: 
        os.path.exists(src_file_loc)
        shutil.copy(os.path.join(src_file_loc, src_file_name),os.path.join(bkp_file_loc,bkp_file_name))        
    except:
        print('mentioned path does not exist')
    finally:
        print('code executed')
        
src_file_loc = input('Please enter source file location  : ')       
src_file_name = input('Please enter source file name  : ')
bkp_file_loc = input('Please enter bkp file location : ')
bkp_file_name = input('Please enter bkp file name : ')

take_bkp(src_file_loc,src_file_name,bkp_file_loc,bkp_file_name)

