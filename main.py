import csv
from barcode import EAN13
from barcode.writer import ImageWriter

def create_barcode(name, number):
    
    if len(number) != 12 or number[0] != "97":
        
        my_code = EAN13(number, writer=ImageWriter())
        my_code.save('barcodes/barcode_{}'.format(name))
        
        print("The barcode of {}, was created!".format(name))
    else:
        print("The product id needs to have 12 characters!")

def read_csv(filename):
    
    with open(filename, 'r', newline='') as file:
        
        reader = csv.reader(file)
        next(reader) 
        
        for row in reader:
            name, number = row
            create_barcode(name, number)

# Name of the CSV
csv_filename = 'products.csv'
read_csv(csv_filename)
