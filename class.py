# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""class ogrenci():
    isim1 = ""
    print("bu sınıf öğrencileri belirtir")
"""

#Sınıf özellikleri
class ogrenci():
    isim = "er"
    soyisim = "GUL"
    yas = "50"
    bolum = "Cevre Muhendisligi"



#sinif örneklendirilmesi
ertugrul = ogrenci()
irmak = ogrenci()
emirhan = ogrenci()
gizem = ogrenci ()


#sınıfların özelliklerine erişmek
print(irmak.isim)
print(irmak.soyisim)
print(irmak.yas)
print(irmak.bolum)
irmak.isim #eski versiyonlarda yazdırma bu şekilde oluyor mu?

#sınıfların özelliklerini değiştirme
ogrenci.soyisim = "Cicek"


print(ogrenci.soyisim)
print(irmak.soyisim)
print(emirhan.soyisim)
print(ertugrul.soyisim)
print(gizem.soyisim)



class ogrenci2():
    def __init__(self):
        self.soyisim = []
        self.yas = []

ertugrul = ogrenci2()
irmak = ogrenci2()
emirhan = ogrenci2()
gizem = ogrenci2()

ertugrul.soyisim.append ("GUL")
irmak.soyisim.append ("SABUNCU")
emirhan.soyisim.append ("OYMAK")
gizem.soyisim.append ("KALENDER")
ertugrul.yas.append ("38")



print(ogrenci.soyisim)
print(irmak.soyisim)
print(emirhan.soyisim)
print(ertugrul.soyisim)
print(gizem.soyisim)


print(dir(ogrenci2))