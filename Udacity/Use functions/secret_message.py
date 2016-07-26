import os

def rename_files():
    #(1) get files names from folder
    file_list = os.listdir(r'D:\Udacity\prank\prank')
    #print (file_list)
    saved_parh = os.getcwd()
    print ('Current working directory is ' + saved_parh )
    os.chdir(r'D:\Udacity\prank\prank')
    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, '0123456789'))
        print('Old name - ' + file_name)
        print ('New name - ' + file_name.translate(None, '0123456789'))
    os.chdir(saved_parh)
rename_files()