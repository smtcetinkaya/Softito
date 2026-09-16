# -*- coding: utf-8 -*-

print("pythonda eğleniyorum")

sehir = "Düzce"
print(sehir)

puan = 50
print(puan)
puan = 75
print(puan)

a = True
b = 3.67
c = "qqqq"
s = 5
print(type(a))
print(type(b))
print(type(c))
print(type(s))

print(type(10))
print(type("10"))

a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(17 % 5)
print(2 ** 8)

ad = input("Adınızı girin")
print("Merhaba, " + ad +"!")

yas = int(input("Yaşınızı girin: "))

print("10 yıl sonraki yaşınız:", yas + 10)

a = 8
b = 12
print(a > b)
print(b > a)
print(a == b)

sayi = int(input("Bir sayı girin: "))

print(sayi == 100)

yas = 22
ogrenci_mi = False
print( yas > 19 and ogrenci_mi)
print(yas > 18 or ogrenci_mi)
print(not ogrenci_mi)

yas = 22
kayitli_mi = True
sonuc = yas > 18 and kayitli_mi
print(sonuc)

sayi = int(input("Bir sayı girin: "))

if sayi >= 0:
    print("Pozitif")
else:
    print("Negatif")

notum = int(input("Notunuzu girin: "))

if notum >= 50:
    print("Geçti")
else:
    print("Kaldı")

ad = "Samet"
soyad = "Çetinkaya"

tam_ad = ad + " " + soyad

print(tam_ad)

kelime = "Python"

print(len(kelime))

yazi = "Python Öğreniyorum"

print(yazi.upper())
print(yazi.lower())

sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

carpim = sayi1 * sayi2

print("Çarpım:", carpim)

sayi = int(input("Bir sayı girin: "))

kare = sayi * sayi

print("Sayının karesi:", kare)