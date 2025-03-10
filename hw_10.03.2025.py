#-----------------kodun ilk adımı-------------------
import pprint
"""
while True:
    try:
        sayi = int(input("Bir sayı giriniz:  "))
        break
    except ValueError:
        print ("Sayı girmediniz!")

print(int(sayi)) #onluk tabana çevirdik "bin" yazdım
print(oct(sayi)) #sekizlik tabana çevirdik "bin" yazdım
print(hex(sayi)) #onaltılık tabana çevirdik "bin" yazdım
print(bin(sayi)) #ikilik tabana çevirdik "bin" yazdım


#-----------------kodun sonraki adımı-------------------
def print_formatted (sayi):
    for i in range(1, sayi + 1):
        onluk = int(i)
        sekizlik = oct(i)
        onaltilik = hex(i)
        ikilik = bin(i)

        print(onluk, sekizlik, onaltilik, ikilik)

sayi = int(input("Bir sayı giriniz:  "))
print_formatted(sayi)

"""
#-----------------kodun birsonraki adımı-------------------
def print_formatted (sayi):
    for i in range(1, sayi + 1):
        onluk = int(i)
        sekizlik = oct(i)[2:]
        onaltilik = hex(i)[2:]
        ikilik = bin(i)[2:]

        print(onluk, sekizlik, onaltilik, ikilik)

sayi = int(input("Bir sayı giriniz:  "))
print_formatted(sayi)


