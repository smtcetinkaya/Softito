PRAGMA foreign_keys = ON;

CREATE TABLE uyeler (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ad VARCHAR(30) NOT NULL,
  yas INTEGER CHECK (yas > 13),
  sehir TEXT DEFAULT 'Erzincan',
  kayit_tarihi TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE kitaplar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT NOT NULL UNIQUE
);

-- Odunc (Ödünç) Tablosu
CREATE TABLE odunc (
    uye_id INTEGER REFERENCES uyeler(id) ON DELETE CASCADE,
    kitap_id INTEGER REFERENCES kitaplar(id),
    PRIMARY KEY (uye_id, kitap_id)
);

INSERT INTO kitaplar (ad) VALUES
('Sefiller'),
('Suç ve Ceza'),
('1984'),
('Yüzüklerin Efendisi'),
('Simyacı');

-- Şehirleri belirtilen üyeler
INSERT INTO uyeler (ad, yas, sehir) VALUES 
('Ali Yılmaz', 20, 'Ankara'),
('Ayşe Kaya', 25, 'İstanbul'),
('Mehmet Demir', 18, 'İzmir');

-- Şehir belirtilmeyen üyeler (Şehirleri otomatik olarak 'Erzincan' olacak)
INSERT INTO uyeler (ad, yas) VALUES 
('Fatma Çelik', 16),
('Ahmet Can', 30),
('Zeynep Şahin', 22),
('Mustafa Koç', 19),
('Elif Öztürk', 27),
('Hasan Aydın', 15),
('Emine Özdemir', 40);

--Bu sorguyu çalıştırdığınızda SQLite CHECK constraint failed: uyeler hatası verir. Çünkü tabloyu oluştururken yas INTEGER CHECK (yas > 13) şeklinde bir kısıtlama koyduk.
INSERT INTO uyeler (ad, yas) VALUES ('Küçük Ayşe', 10);

--Bu id için bir üye olmadığından ilişki kuramaz. Ekle işlemi başarısız olur.
INSERT INTO odunc (uye_id, kitap_id) VALUES (99, 1);

-- Ödünç alınan süreyi (gün) tutmak için eksik kolonu ekliyoruz
ALTER TABLE odunc ADD COLUMN gun INTEGER;

-- 10 üyenin (id: 1-10 arası) her birine 2'şer adet kitap (id: 1-5 arası) tanımlıyoruz
INSERT INTO odunc (uye_id, kitap_id, gun) VALUES 
(1, 1, 5),  (1, 2, 12),
(2, 3, 40), (2, 4, 15),
(3, 1, 22), (3, 5, 8),
(4, 2, 35), (4, 4, 45),
(5, 3, 3),  (5, 5, 20),
(6, 1, 14), (6, 4, 30),
(7, 2, 10), (7, 3, 18),
(8, 1, 25), (8, 5, 42),
(9, 2, 7),  (9, 4, 33),
(10, 3, 21),(10, 5, 11);


--Üye adı, kitap adı ve gün sayısını tek tabloda gösteren sorguyu yazınız.
SELECT 
    uyeler.ad AS Uye_Adi, 
    kitaplar.ad AS Kitap_Adi, 
    odunc.gun AS Gun_Sayisi
FROM uyeler
JOIN odunc ON uyeler.id = odunc.uye_id
JOIN kitaplar ON odunc.kitap_id = kitaplar.id;

--Aynı sorguya, 30 günden uzun tutulan kitapları getirecek koşul ekleyiniz.
SELECT 
    uyeler.ad AS Uye_Adi, 
    kitaplar.ad AS Kitap_Adi, 
    odunc.gun AS Gun_Sayisi
FROM uyeler
JOIN odunc ON uyeler.id = odunc.uye_id
JOIN kitaplar ON odunc.kitap_id = kitaplar.id
WHERE odunc.gun > 30;

--Sadece Erzincan'daki üyelerin ödünç aldığı kitapları listeleyiniz.
SELECT 
    uyeler.ad AS Uye_Adi, 
    kitaplar.ad AS Kitap_Adi, 
    odunc.gun AS Gun_Sayisi
FROM uyeler
JOIN odunc ON uyeler.id = odunc.uye_id
JOIN kitaplar ON odunc.kitap_id = kitaplar.id
WHERE uyeler.sehir = 'Erzincan';

--(İleri) Hiç kitap almamış üyeleri de listede göstermek için hangi JOIN türü gerekir? Yazınız.
--Eğer bir üyenin ödünç tablosunda kaydı yoksa standart JOIN (INNER JOIN) bu üyeyi göstermez. Hiç kitap almamış üyeleri de listede (kitap adı ve gün kısmı boş/NULL olacak şekilde) görebilmek için LEFT JOIN (veya LEFT OUTER JOIN) kullanmamız gerekir.
--LEFT JOIN, "sol taraftaki (ilk yazılan) tablodaki tüm kayıtları getir, sağdaki tabloda eşleşme yoksa o kısımları boş bırak" anlamına gelir.
SELECT 
    uyeler.ad AS Uye_Adi, 
    kitaplar.ad AS Kitap_Adi, 
    odunc.gun AS Gun_Sayisi
FROM uyeler
LEFT JOIN odunc ON uyeler.id = odunc.uye_id
LEFT JOIN kitaplar ON odunc.kitap_id = kitaplar.id;


--Her üyenin ortalama tutma süresini, aldığı kitap sayısını ve en uzun tutma süresini hesaplayınız.
SELECT 
    uyeler.ad AS Uye_Adi,
    AVG(odunc.gun) AS Ortalama_Sure,
    COUNT(odunc.kitap_id) AS Kitap_Sayisi,
    MAX(odunc.gun) AS En_Uzun_Sure
FROM uyeler
JOIN odunc ON uyeler.id = odunc.uye_id
GROUP BY uyeler.id, uyeler.ad;
--Bu listeyi ortalaması 20 günün üzerinde olan üyelerle sınırlandırınız. WHERE yerine neden HAVING kullanıldığını açıklayınız.
--Where gruplama işleminden önce filtreler.
SELECT 
    uyeler.ad AS Uye_Adi,
    AVG(odunc.gun) AS Ortalama_Sure,
    COUNT(odunc.kitap_id) AS Kitap_Sayisi,
    MAX(odunc.gun) AS En_Uzun_Sure
FROM uyeler
JOIN odunc ON uyeler.id = odunc.uye_id
GROUP BY uyeler.id, uyeler.ad
HAVING AVG(odunc.gun) > 20;

--Her kitabın kaç kez ödünç alındığını kitap adıyla gösteriniz.
SELECT 
    kitaplar.ad AS Kitap_Adi,
    COUNT(odunc.uye_id) AS Alinma_Sayisi
FROM kitaplar
LEFT JOIN odunc ON kitaplar.id = odunc.kitap_id
GROUP BY kitaplar.id, kitaplar.ad;

--Hangi şehirden kaç üye olduğunu çoktan aza sıralayınız.
SELECT 
    sehir,
    COUNT(id) AS Uye_Sayisi
FROM uyeler
GROUP BY sehir
ORDER BY Uye_Sayisi DESC;

--En az bir kitabı 30 günden uzun tutmuş üyelerin adlarını alt sorguyla listeleyiniz.
SELECT ad 
FROM uyeler 
WHERE id IN (
    SELECT uye_id 
    FROM odunc 
    WHERE gun > 30
);

--Hiç ödünç alınmamış kitapları NOT IN ile bulunuz.
SELECT ad AS Kitap_Adi 
FROM kitaplar 
WHERE id NOT IN (
    SELECT kitap_id 
    FROM odunc
);

--Genel ortalamanın üzerinde süre tutulan tüm kayıtları listeleyiniz.
SELECT 
    uyeler.ad AS Uye_Adi,
    kitaplar.ad AS Kitap_Adi,
    odunc.gun AS Tutma_Suresi
FROM odunc
JOIN uyeler ON odunc.uye_id = uyeler.id
JOIN kitaplar ON odunc.kitap_id = kitaplar.id
WHERE odunc.gun > (
    SELECT AVG(gun) FROM odunc
);

--Her ödünç kaydı için durum üretiniz: 30 günden fazla 'Gecikmiş', 15–30 arası 'Uyarı', diğerleri 'Normal'.
SELECT 
    uyeler.ad AS Uye_Adi,
    kitaplar.ad AS Kitap_Adi,
    odunc.gun AS Gun_Sayisi,
    CASE 
        WHEN odunc.gun > 30 THEN 'Gecikmiş'
        WHEN odunc.gun >= 15 THEN 'Uyarı'
        ELSE 'Normal'
    END AS Durum
FROM odunc
JOIN uyeler ON odunc.uye_id = uyeler.id
JOIN kitaplar ON odunc.kitap_id = kitaplar.id;

--Üyeleri yaşına göre 'Genç' (≤18) veya 'Yetişkin' olarak etiketleyiniz.
SELECT 
    ad AS Uye_Adi,
    yas AS Yas,
    CASE 
        WHEN yas <= 18 THEN 'Genç'
        ELSE 'Yetişkin'
    END AS Yas_Grubu
FROM uyeler;

--(İleri) Her durumdan kaç kayıt olduğunu sayınız (CASE + GROUP BY).
SELECT 
    CASE 
        WHEN gun > 30 THEN 'Gecikmiş'
        WHEN gun >= 15 THEN 'Uyarı'
        ELSE 'Normal'
    END AS Durum,
    COUNT(kitap_id) AS Kayit_Sayisi
FROM odunc
GROUP BY Durum;

--uyeler.ad sütununda bir index oluşturunuz. Hangi sorguları hızlandırır?
-- Bir üyenin ismi ile arama yapılıcaksa bu tarz aramaları hızlandırır.
CREATE INDEX idx_uyeler_ad ON uyeler(ad);

--uyeler tablosuna ALTER TABLE ile eposta sütunu ekleyip bu sütunda UNIQUE index oluşturunuz.
ALTER TABLE uyeler ADD COLUMN eposta TEXT;
CREATE UNIQUE INDEX idx_uyeler_eposta ON uyeler(eposta);

--İki üyeye aynı e-postayı vermeyi deneyiniz. Sonucu açıklayınız.
-- eposta benzersiz olması gerektiği için hata verir. işlem başarısız olur.
UPDATE uyeler SET eposta = 'ornek@eposta.com' WHERE id = 1;
UPDATE uyeler SET eposta = 'ornek@eposta.com' WHERE id = 2;