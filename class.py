#Sınıf özellikleri
class ogrenci():
    isim = []
    soyisim = "GUL"
    yas = 38
    bolum = "Cevre Muhendisligi"


#sınıfların özelliklerine erişmek
print(ogrenci.isim)
print(ogrenci.soyisim)
print(ogrenci.yas)
print(ogrenci.bolum)


#sınıfların özelliklerini değiştirme
ogrenci.soyisim = "Cicek"
ogrenci.yas = 40

#sınıfların Örneklendirilmesi
ertugrul = ogrenci()
irmak = ogrenci()
emirhan = ogrenci()
gizem = ogrenci()


print (ertugrul.isim)
print (irmak.isim)
print (emirhan.isim)
print (gizem.isim)

ertugrul.isim.append ("Ertuğrul")

print (ertugrul.isim)
print (irmak.isim)
print (emirhan.isim)
print (gizem.isim)


class ogrenci2():
    def __init__(self):
        self.soyisim = []
        self.bolum = []

ertugrul = ogrenci2()
irmak = ogrenci2()
emirhan = ogrenci2()
gizem = ogrenci2()

print (ertugrul.soyisim)
print (irmak.soyisim)
print (emirhan.soyisim)
print (gizem.soyisim)


ertugrul.soyisim.append ("GUL")

print(irmak.soyisim)
print(emirhan.soyisim)
print(ertugrul.soyisim)
print(gizem.soyisim)

irmak.soyisim.append ("SABUNCU")
emirhan.soyisim.append ("OYMAK")
gizem.soyisim.append ("KALENDER")


print(irmak.soyisim)
print(emirhan.soyisim)
print(ertugrul.soyisim)
print(gizem.soyisim)
