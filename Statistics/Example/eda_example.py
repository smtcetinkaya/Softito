# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Grafik stili ve renk paleti standardizasyonu
sns.set_style("whitegrid")
sns.set_palette("Set2")
plt.rcParams["figure.figsize"] = (10, 6)

# Tekrarlanabilirlik için rastgelelik sabitleniyor
np.random.seed(42)

# Pandas'ta tüm sütun/satırların ve ondalık sayıların okunabilir gösterimi
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.float_format", lambda x: "%.2f" % x)

print("Kütüphaneler ve ayarlar hazır.")

"""## 2. Örnek (Sentetik) Veri Setinin Oluşturulması
- 1000 müşteriden oluşan örnek veri seti nasıl üretilir?
- Şehir isimlerinde kasıtlı yazım farklılıkları nasıl eklenir?
"""

n = 1000

df = pd.DataFrame({
    "musteri_id": range(1, n + 1),
    "yas": np.random.normal(38, 12, n).round(0),
    "gelir": np.random.lognormal(mean=10.5, sigma=0.6, size=n).round(2),
    "sehir": np.random.choice(
        ["İstanbul", "Ankara", "İzmir", "Bursa", "istanbul", "ANKARA"],  # kasıtlı tutarsız yazım
        size=n, p=[0.35, 0.2, 0.15, 0.1, 0.1, 0.1]
    ),
    "abonelik_tipi": np.random.choice(["Temel", "Standart", "Premium"], size=n, p=[0.5, 0.35, 0.15]),
    "kayit_tarihi": pd.date_range("2022-01-01", periods=n, freq="7h"),
    "aylik_harcama": np.random.gamma(shape=2, scale=150, size=n).round(2),
    "memnuniyet_puani": np.random.choice([1, 2, 3, 4, 5], size=n, p=[0.05, 0.1, 0.2, 0.35, 0.3]),
    "churn": np.random.choice([0, 1], size=n, p=[0.8, 0.2]),
})

df.head()

"""## 3. Kasıtlı "Kirli Veri" Enjeksiyonu
- Eksik değerler (gelir, yaş, memnuniyet puanı) nasıl eklenir?
- Gelirde aşırı uç değerler (outlier) nasıl oluşturulur?
- Yaşa mantıksız değerler (-5, 150) nasıl eklenir?
- Kasıtlı yinelenen (duplicate) satırlar nasıl eklenir?
"""

# Eksik değerler
df.loc[df.sample(frac=0.08, random_state=1).index, "gelir"] = np.nan
df.loc[df.sample(frac=0.05, random_state=2).index, "yas"] = np.nan
df.loc[df.sample(frac=0.03, random_state=3).index, "memnuniyet_puani"] = np.nan

# Gelirde uç değerler (outlier)
outlier_idx = df.sample(frac=0.01, random_state=4).index
df.loc[outlier_idx, "gelir"] = df["gelir"].max() * np.random.uniform(3, 6, len(outlier_idx))

# Yaşta mantık dışı değerler
df.loc[df.sample(frac=0.005, random_state=5).index, "yas"] = -5
df.loc[df.sample(frac=0.005, random_state=6).index, "yas"] = 150

# Kasıtlı yinelenen satırlar
df = pd.concat([df, df.sample(5, random_state=7)], ignore_index=True)

print(f"Veri Seti: {df.shape[0]} satır, {df.shape[1]} sütun")

"""## 4. Veri Setine Genel Bakış
- Veri setinin boyutu (satır/sütun sayısı) nasıl kontrol edilir?
- Sütun veri tipleri ve dolu/boş hücre sayıları (`.info()`) nasıl incelenir?
- İlk, son ve rastgele seçilmiş satırlar nasıl görüntülenir?
"""

# Boyut kontrolü
print(f"Veri Seti: {df.shape[0]} satır, {df.shape[1]} sütun")
df.shape

# Sütun tipleri ve dolu/boş hücre sayıları
df.info()

# İlk satırlar
df.head()

# Son satırlar
df.tail()

# Rastgele seçilmiş satırlar
df.sample(5, random_state=1)

"""## 5. Eksik Değer Analizi
- Her sütundaki eksik değer sayısı, benzersiz değer sayısı ve eksik değer yüzdesi nasıl özetlenir?
- Eksik değerlerin dağılımı bir ısı haritası (heatmap) ile nasıl görselleştirilir?
"""

print("\n---- Sütun Özeti ----")
ozet = pd.DataFrame({
    "dtype": df.dtypes,
    "eksik_deger": df.isnull().sum(),
    "unique_deger": df.nunique(),
    "eksik_deger_yuzdesi": (df.isnull().mean() * 100).round(2),
})
print(ozet)

# Eksik değerlerin heatmap ile görselleştirilmesi
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis", yticklabels=False)
plt.title("Eksik Değerler")
plt.tight_layout()
plt.savefig("eksik_degerler.png", dpi=300)
plt.show()

"""## 6. Yinelenen Kayıtların Tespiti
- Veri setinde kaç adet birebir aynı (duplicate) satır bulunuyor?
"""

n_dup = df.duplicated().sum()
print(f"Birebir aynı (duplicate) satır sayısı: {n_dup}")
n_dup

"""## 7. Kategorik Veri Temizliği
- "Şehir" sütunundaki tutarsız yazımların dağılımı nasıl görüntülenir?
- Şehir isimleri küçük harfe çevrilip boşluklardan nasıl arındırılır?
"""

# Temizlik öncesi tutarsız yazımların dağılımı
print(df["sehir"].value_counts())

# Küçük harfe çevirme ve baştaki/sondaki boşluklardan arındırma
df["sehir"] = df["sehir"].str.lower().str.strip()

print("Temizlik sonrası:")
print(df["sehir"].value_counts())

"""## 8. Mantık Dışı (Anomali) Değerlerin Tespiti
- 0'ın altında veya 100'ün üzerinde olan, gerçekçi olmayan yaş değerlerine sahip müşteriler nasıl bulunur?
"""

anomali_yas = df[(df["yas"] < 0) | (df["yas"] > 100)][["musteri_id", "yas"]]
print(anomali_yas)
anomali_yas

"""## 9. Betimsel İstatistikler
- Sayısal sütunların temel istatistiksel özeti (ortalama, medyan, std, min/max vb.) nasıl elde edilir?
- Çarpıklık (skewness) ve basıklık (kurtosis) değerleri nasıl hesaplanır?
"""

df.describe()

print("\n---- Çarpıklık / Basıklık ----")

sayisal_sutunlar = df.select_dtypes(include=[np.number]).columns.tolist()
sayisal_sutunlar.remove("musteri_id")

for col in sayisal_sutunlar:
    print(f"{col:20s} skew: {df[col].skew():6.2f}   kurt: {df[col].kurt():6.2f}")

"""## 10. Dağılım Görselleştirmeleri
- Sayısal değişkenlerin dağılımları histogram ve yoğunluk eğrisi (KDE) ile nasıl gösterilir?
- Aykırı değerler kutu grafiği (boxplot) ile nasıl görselleştirilir?
"""

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
for ax, col in zip(axes.flatten(), sayisal_sutunlar):
    sns.histplot(df[col], ax=ax, kde=True, bins=30)
    ax.set_title(col)
# Kullanılmayan eksenleri gizle
for ax in axes.flatten()[len(sayisal_sutunlar):]:
    ax.set_visible(False)
plt.tight_layout()
plt.savefig("histogramlar.png", dpi=300)
plt.show()

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
for ax, col in zip(axes.flatten(), sayisal_sutunlar):
    sns.boxplot(y=df[col], ax=ax)
    ax.set_title(col)
for ax in axes.flatten()[len(sayisal_sutunlar):]:
    ax.set_visible(False)
plt.tight_layout()
plt.savefig("boxplot.png", dpi=300)
plt.show()

"""## 11. Kategorik Değişken Analizi
- Kategorik sütunların (şehir, abonelik tipi, memnuniyet puanı, churn) yüzdesel dağılımı nasıl hesaplanır?
"""

kategorik_sutunlar = ["sehir", "abonelik_tipi", "memnuniyet_puani", "churn"]
for col in kategorik_sutunlar:
    print(f"\n---- {col} ----")
    print((df[col].value_counts(dropna=False, normalize=True) * 100).round(2))

"""## 12. Korelasyon Analizi
- Sayısal değişkenler arasındaki korelasyon matrisi nasıl hesaplanır?
- Korelasyon matrisi bir ısı haritası ile nasıl görselleştirilir?
"""

korelasyon = df[sayisal_sutunlar].corr(numeric_only=True)
print("---- Korelasyon Matrisi ----")
print(korelasyon.round(2))
korelasyon

plt.figure(figsize=(10, 6))
sns.heatmap(korelasyon, annot=True, cmap="coolwarm")
plt.title("Korelasyon Matrisi")
plt.tight_layout()
plt.savefig("korelasyon_matrisi.png", dpi=300)
plt.show()
