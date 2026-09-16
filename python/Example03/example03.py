# -*- coding: utf-8 -*-
class Araba:
    def __init__(self, marka, model, hiz):
        self.marka = marka
        self.model = model
        self.hiz = hiz

    def hizlandir(self, artis):
        self.hiz += artis

    def bilgi_goster(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Hız: {self.hiz} km/s")


araba1 = Araba("BMW", "320i", 100)

araba1.bilgi_goster()

araba1.hizlandir(78)

print("Hızlandırıldı:")
araba1.bilgi_goster()

class Dikdortgen:
    def __init__(self, uzunluk, genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik

    def alan_hesapla(self):
        return self.uzunluk * self.genislik

    def cevre_hesapla(self):
        return 2 * (self.uzunluk + self.genislik)


dikdortgen1 = Dikdortgen(10, 5)

print(f"Alan: {dikdortgen1.alan_hesapla()}")
print(f"Çevre: {dikdortgen1.cevre_hesapla()}")

class Kitap:
    def __init__(self, ad, yazar, sayfa_sayisi):
        self.ad = ad
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi

    def ozet(self):
        return f"{self.ad} - {self.yazar} ({self.sayfa_sayisi} sayfa)"


kitap1 = Kitap("Demir Ökçe", "Jack London", 340)

print(kitap1.ozet())