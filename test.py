# with open('data.txt',mode='r') as f:
#     data=f.readline()
#     print(data)

import os 
import csv

def read_csv_file():
    data=[]
    with open('data.csv') as f:
        res=csv.reader(f)
        next(res)
        for r in res:
            data.append(tuple(r))
            # print(r)
        f.close()
    print('data:',data)

read_csv_file()
