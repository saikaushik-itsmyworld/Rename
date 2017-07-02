import os
def rename_files():
    file_list = os.listdir(r"C:\Users\sunny\Documents\prank")
    print(file_list)
    saved_path=os.getcwd()
    print("current working directory is"+saved_path)
    os.chdir(r"c:\Users\sunny\Documents\prank")
    remove="0123456789"
    table=str.maketrans("","",remove)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(table))
    os.chdir(saved_path)
        
rename_files()
