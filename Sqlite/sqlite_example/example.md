Tablo Tasarımı ve Kısıtlar
SQLite'ta yabancı anahtar denetimi varsayılan olarak kapalıdır. Bunu açan komutu yazınız.
uyeler tablosunu oluşturunuz: otomatik artan id, boş bırakılamayan ad, 13'ten büyük olması zorunlu yas, varsayılan değeri 'Erzincan' olan sehir ve kayıt anını tutan kayit sütunları olsun.
kitaplar tablosunu oluşturunuz. Kitap adı hem boş olamasın hem de tekrar edemesin.
odunc tablosunu oluşturunuz. uye_id ve kitap_id birlikte birincil anahtar olsun; üye silindiğinde ödünç kayıtları da silinsin.
(Tartışma) Bir kitap silinmeye çalışılırsa ne olur? kitap_id için neden ON DELETE CASCADE tercih edilmemiş olabilir?

Veri Ekleme
kitaplar tablosuna 5 kitap ekleyiniz.
uyeler tablosuna en az 10 üye ekleyiniz; bazılarında sehir belirtmeyip varsayılan değeri gözlemleyiniz.
Yaşı 10 olan bir üye eklemeyi deneyiniz. Hatayı açıklayınız.
odunc tablosuna olmayan bir uye_id (ör. 99) ile kayıt eklemeyi deneyiniz. Neden başarısız oldu?
Her üyeye en az iki kitap için ödünç kaydı giriniz (gun değerleri 3–45 arasında değişsin).

JOIN
Üye adı, kitap adı ve gün sayısını tek tabloda gösteren sorguyu yazınız.
Aynı sorguya, 30 günden uzun tutulan kitapları getirecek koşul ekleyiniz.
Sadece Erzincan'daki üyelerin ödünç aldığı kitapları listeleyiniz.
(İleri) Hiç kitap almamış üyeleri de listede göstermek için hangi JOIN türü gerekir? Yazınız.

Gruplama ve Toplama Fonksiyonları
Her üyenin ortalama tutma süresini, aldığı kitap sayısını ve en uzun tutma süresini hesaplayınız.
Bu listeyi ortalaması 20 günün üzerinde olan üyelerle sınırlandırınız. WHERE yerine neden HAVING kullanıldığını açıklayınız.
Her kitabın kaç kez ödünç alındığını kitap adıyla gösteriniz.
Hangi şehirden kaç üye olduğunu çoktan aza sıralayınız.

Alt Sorgu
En az bir kitabı 30 günden uzun tutmuş üyelerin adlarını alt sorguyla listeleyiniz.
Hiç ödünç alınmamış kitapları NOT IN ile bulunuz.
Genel ortalamanın üzerinde süre tutulan tüm kayıtları listeleyiniz.

CASE
Her ödünç kaydı için durum üretiniz: 30 günden fazla 'Gecikmiş', 15–30 arası 'Uyarı', diğerleri 'Normal'.
Üyeleri yaşına göre 'Genç' (≤18) veya 'Yetişkin' olarak etiketleyiniz.
(İleri) Her durumdan kaç kayıt olduğunu sayınız (CASE + GROUP BY).

Index
uyeler.ad sütununda bir index oluşturunuz. Hangi sorguları hızlandırır?
uyeler tablosuna ALTER TABLE ile eposta sütunu ekleyip bu sütunda UNIQUE index oluşturunuz.
İki üyeye aynı e-postayı vermeyi deneyiniz. Sonucu açıklayınız.