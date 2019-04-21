import csv
import os

def get_root_path():
    print(os.path.abspath(__file__))
    root_path=os.path.dirname(os.path.abspath(__file__))
    return root_path

def read_csv_file(file_path):
    data=[]
    with open(file_path) as f:
        res=csv.reader(f)
        next(res)
        for r in res:
            data.append(tuple(r))
            # print(r)
        f.close()
    # print('data:',data)
    return data