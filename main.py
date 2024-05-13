from barcode import EAN13
from barcode.writer import ImageWriter

name = input("Coloque o nome do produto: ")
number = input("Coloque o numero do produto: ")
if  len(number) != 12 or number[0]!="97" :

    my_code = EAN13(number, writer=ImageWriter())
    my_code.save('barcodes/barcode_{}'.format(name))
    
    print("Código de barras criado! ")
else :
    print ("É necessário que o produto tenha 12 digitos!")