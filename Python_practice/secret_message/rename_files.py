import os

def rename_files():
    file_list = os.listdir(r"C:\Users\Stephanie\Documents\Intro to Programming (udacity)\Stephanie_Project3\Python_practice\secret_message\secret_message")
    print file_list
    saved_path = os.getcwd()
    print "Current Working Directory is " + saved_path
    os.chdir(r"C:\Users\Stephanie\Documents\Intro to Programming (udacity)\Stephanie_Project3\Python_practice\secret_message\secret_message")

    for file_name in file_list:
        print "Old name: " + file_name
        print "New name: " + file_name.translate(None, "0123456789")
        os.rename(file_name, file_name.translate(None, "0123456789"))

    os.chdir(saved_path)
    
rename_files()
