import os
import datetime
import pandas as pd
# from openpyxl import load_workbook

# f = open(path + "\LargeFiles.txt", "r")
# for line in f:
#     print(line)
# C:\Users\anshu\OneDrive\Code\EDG\LargeFiles.txt
def get_file_size(size):
    if size < (1024 * 1024):
        return round(size / 1024, 2), "KB"
    elif size < (1024 * 1024 * 1024):
        return round(size / (1024 * 1024), 2), "MB"
    else:
        return round(size / (1024 * 1024 * 1024), 2), "GB"


# path = r"C:\Users\1270816\Documents\GitHub\EDG"
path = os.getcwd()
xl_file = path + "\\" + "LargeFiles.xlsx"
today_ = str(datetime.date.today())
data_ = dict()

counter = 0
f = open(path + "\LargeFiles.txt", "a")
f.write("\n\n\n" + str(datetime.date.today()))
f.write("\n" + "==========")
f.write("\n" + "Folder Name, File Name, Size, Size Group")
for foldername, subfolders, filenames in os.walk(path):
    for filename in filenames:
        size = round(os.path.getsize(os.path.join(foldername, filename)), 2)
        if get_file_size(size)[0] >= 100.0 and get_file_size(size)[1] == "MB":
            f.write(
                f"\n{foldername}\, {filename}, {get_file_size(size)[0]}, {get_file_size(size)[1]}"
            )
f.close()
