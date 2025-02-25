import tkinter as tk
from tkinter import filedialog
import os
import time

root = tk.Tk()
root.withdraw()
dir_path = filedialog.askdirectory()

file_list = os.listdir(dir_path)
previous_file_name = ""
for file_name in file_list:
    if file_name.startswith('PXL_'):
        new_file_name = file_name.split(".")[0] + "." + file_name.split(".")[1][:-3] + "." + file_name.split(".")[-1]
        if new_file_name == previous_file_name:
            new_file_name = file_name.split(".")[0] + "." + file_name.split(".")[1] + "." + file_name.split(".")[-1]
        os.rename(os.path.join(dir_path,file_name), os.path.join(dir_path,new_file_name))
        previous_file_name = new_file_name