import os
from string import digits
def rename_files():
    file_list = os.listdir(r"C:\Users\lubo\Desktop\alphabet\alphabet")
    print(file_list)
    saved_path = os.getcwd()
    print("Working dir is " + saved_path)
    os.chdir(r"C:\Users\lubo\Desktop\alphabet\alphabet")
    remove_digits = str.maketrans("", "", digits)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(remove_digits))
        os.chdir(saved_path)

rename_files()