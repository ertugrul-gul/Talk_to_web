#ilk sayı girme
sayi1 = float(input('işlem yapmak istediğiniz İlk Sayıyı Giriniz: '))

#ikinci sayı girme
sayi2 = float(input('işlem yapmak için İkinci Sayıyı Giriniz: '))

#sayıları topla
topla = sayi1 + sayi2

print('Toplam:', topla)
print("{0} {1} {2}".format("Toplam", "=", topla))
print("{0} {1} {2}".format("Toplam", "=", sayi1 + sayi2))
print(f"""{sayi1} + {sayi2} = {topla}""")
