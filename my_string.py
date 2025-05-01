my_str= "Deniz Aras GÜL"

# for x in "Deniz Aras GÜL":
#     print (x)
#
#
# for d in my_str:
#     print (d)
# print(len (my_str))
#
# print ("Deniz" in my_str)
# print ("Aysun" not in my_str)
# if "Aysun" not in my_str:
#     print("Hayır, 'Aysun' kelimesi stringde yok.")

"""
Dilimlemeler [ilk değer : son değer : adım sayısı] şeklinde gerçekleşir.
ilk değer daima "0" olarak kabul edilir.
Dilimlemeler yapılırken daima soldan - sağa doğru yapılır. Başına - konulması durumu tersine çevirir.
"""


print(my_str[0]) #ilk elemanı yazdır.
print(my_str[-2]) # eksi işareti (-) sondan başlanılması gerektiğini ifade eder
print(my_str[::2]) # hiçbirşey yazılmaması default olarak başlangıç-bitişi ifade eder. 2'de adım sayısıdır.
print(my_str[::-2]) # bu seferde -2 olduğundan sağdan sola doğru hareket eder.
print(my_str[-1:0:-3]) # sondan başa doğru 3'er atlayarak dilimleme yapılmasını söyler



for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print (x)