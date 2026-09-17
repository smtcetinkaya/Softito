# -*- coding: utf-8 -*-

#pandas kurulumu
!pip install pandas

import pandas as pd

sayilar = pd.Series([10,20,30,40,50])
print(sayilar)

notlar = pd.Series([85,90,78], index = ['Ayşe','Fatma','Hayriye'])

print(notlar)

veri ={
    "isim" : ["Ayşe","Fatma","Hayriye"],
    "yas" : [23,25,30],
    "sehir" : ["Ankara","İstanbul","İzmir"]
}

df =pd.DataFrame(veri)
print(df)

df = pd.read_csv("/content/grocery_chain_data.csv")

df_new = pd.read_excel("/content/Superlig_Proje.xlsx")

df.head(2)

df_new.head(2)

df_new.tail(2)

df_new.shape

df_new.columns

df.info()

df.describe()

df=pd.read_csv("/content/data.csv")

df.head(2)

df.tail(2)

df.shape

df.columns

df.info()

df.describe()

print(df["wks"])

print(df[["wks","pk"]])

print(df.loc[0])
print(df.loc[0:2])

print(df.iloc[0])

print(df.iloc[0:3,0:2])

print(df[df["wks"]<100])

df["yeni sütun"] = df["wks"]*12

df

print(df.sort_values("wks"))

print(df.sort_values("t10", ascending= False))

df.info()

print(df.isnull().sum())

df2= df.fillna(0)

df2.isnull().sum()

df3 = df.dropna()

df3.shape

df.shape

ogrenciler  = pd.DataFrame({
    "ogrenci_id":[1,2,3],
    "isim" : ["Ayşe","Fatma","Hayriye"],
    "ogrenci_no" :[221,796,207]
})

notlar = pd.DataFrame({
    "ogrenci_id" :[1,2,3],
    "ders" : ["Matematik","Fizik","Kimya"],
    "not" : [85,90,78],
    "dönem" : [1,1,2]
})

#sadece ortak alanlara göre
df_merge = pd.merge(ogrenciler,notlar, on="ogrenci_id" , how= "inner")

df_merge

df_left = pd.merge(ogrenciler,notlar, on="ogrenci_id" , how= "left")

df_left

df_outer = pd.merge(ogrenciler,notlar, on="ogrenci_id" , how= "outer")

df_outer

df= pd.DataFrame({
    "departman" : ["satış", "IT","satış", "IT","IK"],
    "isim" : ["Ayşe","Fatma","Hayriye","Tripcan","Zıpırcan"],
    "maas" : [15000,20000,232320,3543535,123124510]
})

#departmana göre ortalama maaaş
print(df.groupby("departman")["maas"].mean())

print(df.groupby("departman")["maas"].sum())

print(df.groupby("departman")["isim"].count())