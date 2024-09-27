# %%
import csv, os
import requests

url = r'https://raw.githubusercontent.com/jmclawson/TopicKit/refs/heads/main/shakespeare.csv'

with open(r'shakespear.txt', 'r') as file:
  reader = csv.reader(file)
  # files = [_ for _ in reader]
  for row in reader:
    if '/files/' in row[0]:      
      # print(row[0], row[3])
      txt_file = f'{row[3]}.txt'.replace(' ','_')
      if not os.path.isfile(txt_file):
        response = requests.get(row[0])
        content=response.text
        try:
          with open(txt_file, 'w') as file:
            file.write(content)
        except UnicodeEncodeError:
          print(f'Could not write {txt_file}')
        print(f'File {txt_file} saved!!!')
# %%
# import pandas as pd
# import os

# for _ in os.listdir():
#   print(_)


# files = pd.read_csv(r'shakespear.txt')
# print(files)
# %%
