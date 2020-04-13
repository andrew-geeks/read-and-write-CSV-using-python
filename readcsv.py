#import the module
import csv

with open('file.csv',mode='r') as file:
    read=csv.reader(file)
    for row in read:
        print(row)
