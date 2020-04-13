#import the module
import csv

#defining fields
fields=['Rollno.','Name','Marks']

#defining data
data= [[1,'Andrew',20],
       [2,'Roger',18],
       [3,'John',14],
       [4,'Dipin',17]]

#opening a new csv file
with open('file.csv',mode='w') as file:
    writer=csv.writer(file) #defing csv writer object

    writer.writerow(fields) #writing the fields
    writer.writerows(data)   #writing the data

    
