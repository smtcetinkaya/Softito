# -*- coding: utf-8 -*-

birim_fiyat = 250
adet = 3

toplam = birim_fiyat * adet

print(f"Toplam tutar: {toplam} TL")

maas = 8000

maas += 1500

print(f"Yeni maaş: {maas} TL")

yas = int(input("Yaşınızı girin: "))
ogrenci_mi = input("Öğrenci misiniz? (Evet/Hayır): ")

if yas > 65:
    print("Ücretsiz")
else:
    if ogrenci_mi == "Evet":
        print("İndirimli")
    else:
        print("Tam ücret")

sayi = int(input("Bir sayı girin: "))

if sayi > 0:
    if sayi % 2 == 0:
        print("Sayı pozitif ve çifttir.")
    else:
        print("Sayı pozitif ama tektir.")
else:
    print("Sayı pozitif değildir.")

sicaklik = int(input("Sıcaklığı girin: "))

if sicaklik > 30:
    print("Sıcak")
elif sicaklik >= 15:
    print("Ilıman")
else:
    print("Soğuk")

ay = int(input("Ay numarasını girin: "))

if ay == 12 or ay == 1 or ay == 2:
    print("Kış")
elif ay == 3 or ay == 4 or ay == 5:
    print("İlkbahar")
elif ay == 6 or ay == 7 or ay == 8:
    print("Yaz")
elif ay == 9 or ay == 10 or ay == 11:
    print("Sonbahar")
else:
    print("Geçersiz ay numarası")

sayilar = [5, 15, 8, 22, 3, 19]

en_buyuk = sayilar[0]

for sayi in sayilar:
    if sayi > en_buyuk:
        en_buyuk = sayi

print(f"En büyük sayı: {en_buyuk}")

sayilar = [5, 15, 8, 22, 3, 19]

sayac = 0

for sayi in sayilar:
    if sayi > 10:
        sayac += 1

print(f"10'dan büyük sayı adedi: {sayac}")

sayi = 10

while sayi >= 1:
    print(sayi)
    sayi -= 1

dogru_sifre = "1234"

sifre = input("Şifreyi girin: ")

while sifre != dogru_sifre:
    print("Yanlış şifre!")
    sifre = input("Şifreyi tekrar girin: ")

print("Şifre doğru!")

for sayi in range(1, 21):
    if sayi % 3 == 0:
        print(sayi)

sayilar = [-5, 10, -3, 8, -1, 15]

negatifler = []
pozitifler = []

for sayi in sayilar:
    if sayi < 0:
        negatifler.append(sayi)
    elif sayi > 0:
        pozitifler.append(sayi)

print(f"Negatifler: {negatifler}")
print(f"Pozitifler: {pozitifler}")

def kup_al(sayi):
    return sayi ** 3


sonuc = kup_al(4)

print(sonuc)

def topla(sayi1, sayi2):
    return sayi1 + sayi2


sonuc = topla(10, 20)

print(sonuc)

def sayi_durumu(sayi):
    if sayi > 0:
        return "Pozitif"
    elif sayi < 0:
        return "Negatif"
    else:
        return "Sıfır"


print(sayi_durumu(10))
print(sayi_durumu(-5))
print(sayi_durumu(0))

def en_buyuk(sayi1, sayi2, sayi3):
    en_buyuk_sayi = sayi1

    if sayi2 > en_buyuk_sayi:
        en_buyuk_sayi = sayi2

    if sayi3 > en_buyuk_sayi:
        en_buyuk_sayi = sayi3

    return en_buyuk_sayi


sonuc = en_buyuk(15, 27, 10)

print(f"En büyük sayı: {sonuc}")

sehirler = []

for i in range(5):
    sehir = input(f"{i + 1}. şehri girin: ")
    sehirler.append(sehir)

print("\nŞehirler:")

for i in range(len(sehirler)):
    print(f"{i + 1}. {sehirler[i]}")

urunler = ["Laptop", "Telefon", "Mouse", "Klavye"]

print(urunler)

urunler.remove("Mouse")

print(urunler)

ad = input("Adınız: ")
soyad = input("Soyadınız: ")
dogum_yili = int(input("Doğum yılınız: "))

yas = 2026 - dogum_yili

print(f"Merhaba {ad} {soyad}!")
print(f"Yaşınız: {yas}")

boy = float(input("Boyunuzu cm olarak girin: "))
kilo = float(input("Kilonuzu kg olarak girin: "))

boy = boy / 100

bmi = kilo / (boy ** 2)

print(f"BMI değeriniz: {bmi:.2f}")

not1 = float(input("1. ders notu: "))
not2 = float(input("2. ders notu: "))
not3 = float(input("3. ders notu: "))
not4 = float(input("4. ders notu: "))

ortalama = (not1 + not2 + not3 + not4) / 4

print(f"Ortalama: {ortalama:.2f}")
if ortalama >= 90:
    harf = "AA"
elif ortalama >= 85:
    harf = "BA"
elif ortalama >= 80:
    harf = "BB"
elif ortalama >= 70:
    harf = "CB"
elif ortalama >= 60:
    harf = "CC"
elif ortalama >= 50:
    harf = "DC"
elif ortalama >= 40:
    harf = "DD"
else:
    harf = "FF"

print(f"Harf notu: {harf}")
notlar = [not1, not2, not3, not4]

en_yuksek = max(notlar)
en_dusuk = min(notlar)

print(f"En yüksek not: {en_yuksek}")
print(f"En düşük not: {en_dusuk}")

urunler = [
    ["Laptop", 25000],
    ["Mouse", 500],
    ["Klavye", 1200],
    ["USB Kablo", 80],
    ["Kulaklık", 1500]
]

pahali_urunler = []

for urun in urunler:
    if urun[1] > 100:
        pahali_urunler.append(urun)

print("100 TL üzerindeki ürünler:")

for urun in pahali_urunler:
    print(f"{urun[0]} - {urun[1]} TL")

toplam = 600

if toplam > 500:
    indirim = toplam * 0.10
    yeni_toplam = toplam - indirim

    print("%10 indirim kazandınız!")
    print(f"İndirim: {indirim} TL")
    print(f"Ödenecek tutar: {yeni_toplam} TL")
else:
    print(f"Ödenecek tutar: {toplam} TL")