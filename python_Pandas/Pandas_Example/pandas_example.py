# -*- coding: utf-8 -*-
!pip install pandas

import pandas as pd

pd.show_versions()

sayilar = pd.Series([20,34,45,56])
print(sayilar)

sehirler = pd.Series([415622,239625,455074,768087],index=["Düzce","Erzincan","Giresun","Ordu"])
print(sehirler)
print(sehirler["Ordu"])
print(sehirler.sum())

urunler = pd.DataFrame({
    "urun": ["Kalem", "Defter", "Silgi", "Cetvel", "Çanta"],
    "fiyat": [10, 25, 5, 15, 350],
    "stok": [120, 80, 200, 60, 30]
})
print(urunler)
urunler.info()

ogrenciler = pd.DataFrame({
    "isim": ["Ahmet", "Ayşe", "Mehmet", "Zeynep", "Elif", "Can"],
    "yas": [21, 22, 20, 23, 19, 24],
    "bolum": ["Bilgisayar Müh.", "Elektrik Müh.", "Matematik",
              "Fizik", "Kimya", "Bilgisayar Müh."]
})
print(ogrenciler)
ogrenciler.info()

#index false olursa index numaraları yazılır
ogrenciler.to_csv("ogrenciler.csv", index=False)
df = pd.read_csv("/content/ogrenciler.csv")
print(df)

#index false olmadığından isimsiz bir index sütunu eklendi
ogrenciler.to_csv("ogrenciler.csv")
df = pd.read_csv("/content/ogrenciler.csv")
print(df)

kisiler = pd.DataFrame({
    "isim": ["Ahmet", "Ayşe", "Mehmet", "Zeynep", "Elif",
             "Can", "Deniz", "Ela"],
    "yas": [21, 22, 20, 23, 19, 24, 30, 27],
    "maas": [18000, 22000, 15500, 27000, 19500, 31000, 45000, 28500],
    "sehir": ["İstanbul", "Ankara", "İzmir", "İstanbul",
              "Bursa", "Ankara", "İstanbul", "İzmir"]
})
print(kisiler.head(3))
print(kisiler.tail(2))
kisiler.info()
print(kisiler.shape)
kisiler.describe()
kisiler['yas'].describe()

kisiler["isim"]

kisiler[["isim","yas"]]

kisiler.loc[0:2]

kisiler.iloc[1,1]

print("7a) Yaşı 25'ten büyük olanlar:\n", kisiler[kisiler["yas"] > 25], sep="")

print("\n7b) Maaşı 20000-30000 arasında olanlar:\n",
      kisiler[(kisiler["maas"] >= 20000) & (kisiler["maas"] <= 30000)], sep="")

print("\n7c) İstanbul'da yaşayanlar:\n",
      kisiler[kisiler["sehir"] == "İstanbul"], sep="")

print("\n7d) Yaşı 20'den küçük VEYA 40'tan büyük olanlar:\n",
      kisiler[(kisiler["yas"] < 20) | (kisiler["yas"] > 40)], sep="")

kisiler["dogum_yili"] = 2026 - kisiler["yas"]
print("8a) 'dogum_yili' sütunu eklendi:\n", kisiler[["isim", "yas", "dogum_yili"]], sep="")

kisiler["maas"] = kisiler["maas"] * 1.10
print("\n8b) Maaşlar %10 artırıldı:\n", kisiler[["isim", "maas"]], sep="")

kisiler["yas_grubu"] = kisiler["yas"].apply(lambda y: "Yetişkin" if y > 18 else "Çocuk")
print("\n8c) apply()+lambda ile 'yas_grubu' sütunu:\n",
      kisiler[["isim", "yas", "yas_grubu"]], sep="")

notlar = pd.DataFrame({
    "isim": ["Ahmet", "Ayşe", "Mehmet", "Zeynep", "Elif", "Can"],
    "yas": [21, 22, 20, 23, 19, 24],
    "matematik": [80, 65, 90, 55, 72, 40],
    "fizik": [70, 75, 85, 60, 68, 50],
    "kimya": [88, 60, 95, 50, 74, 45],
    "sehir": ["İstanbul", "Ankara", "İzmir", "Bursa", "İstanbul", "Ankara"]
})

notlar["ortalama"] = notlar[["matematik", "fizik", "kimya"]].mean(axis=1)
print("BONUS a) Notlar ve ortalama:\n", notlar, sep="")

basarili = notlar[notlar["ortalama"] > 70].sort_values("yas")
print("\nBONUS b) Ortalaması 70'in üzerinde olanlar (yaşa göre sıralı):\n",
      basarili, sep="")