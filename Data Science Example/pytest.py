import csv
with open('test.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
    
mpg[:3] #
print(mpg)

value=list(d['TITLE'] for d in mpg)
print(value)