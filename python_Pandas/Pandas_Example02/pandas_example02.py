# -*- coding: utf-8 -*-

!pip install pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1.
stok = pd.Series([300, 150, 80, 45],index  = ['Kalem','Defter','Silgi','Cetvel'])
print(stok["Kalem"])

en_az_stok_urun = stok.idxmin()
print(en_az_stok_urun)

toplam_stok = stok.sum()
print(toplam_stok)

#2.
veri = {
    'uye_adi': ['Ahmet', 'Elif', 'Mehmet', 'Zeynep', 'Can', 'Ayşe'],
    'paket_turu': ['Aylık', 'Yıllık', 'Aylık', 'Yıllık', 'Aylık', 'Yıllık'],
    'odenen_tutar': [500, 4800, 500, 4500, 550, 5000]
}

df = pd.DataFrame(veri)
print(df)

print(df.shape)

print(df.columns)

#3.
df_csv = pd.read_csv("satislar.csv")
print(df_csv)
df_excel = pd.read_excel("rapor.xlsx")
print(df_excel)

#4.
df = pd.DataFrame({    "siparis_no": [1001, 1002, 1003, 1004, 1005, 1006, 1007],    "kargo_suresi": [2, 5, 3, np.nan, 1, 4, 6],    "urun_adedi": [1, 3, 2, 5, 1, 2, 4],    "toplam_tutar": [150.0, 480.5, 220.0, 610.0, 90.0, 310.0, 720.0]})

df.head(3)

df.info()

df.tail(2)

df.describe()

#5.
print(df[['siparis_no','toplam_tutar']])

df.loc[0:3]

print(df.iloc[0:4, -2:])

#6.
filtre_300 = df[df['toplam_tutar'] > 300]
print(filtre_300)

filtre_kosullu = df[(df['urun_adedi'] > 2) & (df['toplam_tutar'] > 200)]
print(filtre_kosullu)

df['birim_fiyat'] = df['toplam_tutar'] / df['urun_adedi']
print(df)

df['kargo_durumu'] = df['kargo_suresi'].apply(lambda x: "Yavaş" if x > 3 else "Hızlı")
print(df)

#7.
df_sirali = df.sort_values(by='toplam_tutar', ascending=False)
print(df_sirali)

df_cok_sutunlu_sirali = df.sort_values(by=['urun_adedi', 'kargo_suresi'], ascending=[True, True])
print(df_cok_sutunlu_sirali)

#8.
eksik_sayisi = df['kargo_suresi'].isna().sum()
print(eksik_sayisi)

df_dolu = df.copy()
df_dolu['kargo_suresi'] = df_dolu['kargo_suresi'].fillna(df_dolu['kargo_suresi'].median())
print(df_dolu)

df_temiz = df.dropna()
print(df_temiz)
print("Orijinal df boyutu:", df.shape)
print("df_temiz boyutu:", df_temiz.shape)

#9.
musteriler = pd.DataFrame({    "musteri_id": [1, 2, 3, 4],    "ad": ["Baran", "Ceylin", "Emre", "Fulya"]})
siparisler = pd.DataFrame({    "musteri_id": [1, 2, 5],    "urun": ["Kulaklık", "Şarj Kablosu", "Powerbank"],    "tutar": [450, 90, 320]})

df_inner = pd.merge(musteriler, siparisler, on='musteri_id', how='inner')
print(df_inner)

df_left = pd.merge(musteriler, siparisler, on='musteri_id', how='left')
print(df_left)

df_outer = pd.merge(musteriler, siparisler, on='musteri_id', how='outer')
print(df_outer)

#10.
hafta1 = pd.DataFrame({"gun": ["Pzt", "Sal"], "adet": [20, 35]})
hafta2 = pd.DataFrame({"gun": ["Çar", "Per"], "adet": [28, 40]})

print("hafta1:")
print(hafta1)
print("\nhafta2:")
print(hafta2)

df_birlesik = pd.concat([hafta1, hafta2], ignore_index=True)
print(df_birlesik)

gelir = pd.DataFrame({"toplam_gelir": [1000, 1750]})

df_yanyana = pd.concat([hafta1, gelir], axis=1)
print(df_yanyana)

#11.
df_calisan = pd.DataFrame({    "sube": ["Kadıköy", "Beşiktaş", "Kadıköy", "Şişli", "Beşiktaş"],    "ad": ["Baran", "Ceylin", "Emre", "Fulya", "Gökhan"],    "satis": [12000, 18500, 9500, 21000, 16000]})
toplam_satis = df_calisan["satis"].sum()
print(toplam_satis)
ortalama_satis = df_calisan.groupby("sube")["satis"].mean()
print(ortalama_satis)

istatistikler = df_calisan.groupby("sube")["satis"].agg(["sum", "mean", "count"])
print(istatistikler)

#12.
df_satis = pd.DataFrame({    "sehir": ["Bursa", "Adana", "Antalya", "Bursa", "Adana"],    "kategori": ["Elektronik", "Giyim", "Elektronik", "Giyim", "Elektronik"],    "satis": [5000, 3200, 4100, 2800, 3900]})
pivot1 = df_satis.pivot_table(index="sehir", columns="kategori", values="satis")
print(pivot1)

pivot2 = df_satis.pivot_table(index="sehir", columns="kategori", values="satis",
                                aggfunc="sum", fill_value=0)
print(pivot2)

#13.
df_kullanici = pd.DataFrame({"kullanici_adi": ["baran23", "CEYLIN_K", "emre.y"]})

df_kullanici["kullanici_adi_kucuk"] = df_kullanici["kullanici_adi"].apply(str.lower)

df_kullanici["karakter_sayisi"] = df_kullanici["kullanici_adi"].apply(lambda x: len(x))

print(df_kullanici)

#14.
df_urun = pd.DataFrame({"urun_id": ["10", "11", "12"], "agirlik_kg": ["1.5", "0.75", "3.2"]})
df_urun.info()

df_urun["urun_id"] = df_urun["urun_id"].astype(int)
df_urun["agirlik_kg"] = df_urun["agirlik_kg"].astype(float)

df_urun.info()

#15.
df_gelir = pd.DataFrame({    "ceyrek": ["Ç1", "Ç2", "Ç3", "Ç4"],    "gelir": [42000, 55000, 48000, 61000],    "gider": [30000, 38000, 33000, 40000]})

#Çizgi grafik (marker="o")
df_gelir.set_index("ceyrek")["gelir"].plot(kind="line", marker="o")
plt.title("Çeyreklik Gelir")
plt.xlabel("Çeyrek")
plt.ylabel("Gelir (TL)")
plt.show()

#Bar grafik
df_gelir.set_index("ceyrek")["gelir"].plot(kind="bar", color="teal")
plt.title("Çeyreklik Gelir (Bar)")
plt.xlabel("Çeyrek")
plt.ylabel("Gelir (TL)")
plt.show()

#Pasta grafik
df_gelir.set_index("ceyrek")["gelir"].plot(kind="pie", autopct="%1.1f%%")
plt.title("Çeyreklere Göre Gelir Payı")
plt.ylabel("")  # pasta grafikte y ekseni etiketi genelde kaldırılır
plt.show()

#Scatter grafik (gelir vs gider)
df_gelir.plot(kind="scatter", x="gelir", y="gider")
plt.title("Gelir - Gider İlişkisi")
plt.xlabel("Gelir (TL)")
plt.ylabel("Gider (TL)")
plt.show()

#Bonus
df_kurs = pd.DataFrame({
    "kurs_adi": ["Python 101", "React Temelleri", "Figma ile UI", "SEO Uzmanlığı",
                 "Veri Bilimi", "Adobe XD", "Sosyal Medya Pazarlama", "Java Temelleri"],
    "kategori": ["Yazılım", "Yazılım", "Tasarım", "Pazarlama",
                 "Yazılım", "Tasarım", "Pazarlama", "Yazılım"],
    "satis_adedi": [65, 40, 55, 30, 90, 20, 75, 45]
})
print(df_kurs)

kategori_toplam = df_kurs.groupby("kategori")["satis_adedi"].sum()
print(kategori_toplam)

en_iyi_3 = df_kurs.sort_values(by="satis_adedi", ascending=False).head(3)
print(en_iyi_3)

kategori_toplam.plot(kind="bar", color=["orange", "purple", "steelblue"])
plt.title("Kategoriye Göre Toplam Satış")
plt.xlabel("Kategori")
plt.ylabel("Toplam Satış Adedi")
plt.xticks(rotation=0)
plt.show()

df_kurs["durum"] = df_kurs["satis_adedi"].apply(lambda x: "Popüler" if x > 50 else "Standart")
print(df_kurs)