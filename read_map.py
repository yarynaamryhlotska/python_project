import os.path
import csv

def read_map(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as map_file:
            content = [row for row in csv.reader(map_file)]
        return content
    else:
        print("File not found.")
        return None
