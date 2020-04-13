#import the module
import csv

ndict=[{'name':'Andrew','rollno.':1,'marks':19},
       {'name':'John','rollno.':2,'marks':18},
       {'name':'Roger','rollno.':3,'marks':16}]
#define fields
fields=['rollno.','name','marks']

with open('dictnew.csv',mode='w') as file:
    writer=csv.DictWriter(file,fieldnames=fields)#create writer object
    writer.writeheader() #writing field names(headings)
    writer.writerows(ndict) #writing the data
    

