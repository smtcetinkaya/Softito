CREATE TABLE oyuncaklar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isim TEXT NOT NULL,
    cesit TEXT,
    fiyat NUMERIC CHECK (fiyat > 0),
    renk TEXT DEFAULT 'kırmızı'
);

INSERT INTO oyuncaklar (isim, cesit, fiyat) VALUES ('Şimşek', 'araba', 50);

INSERT INTO oyuncaklar (isim, cesit, fiyat, renk) VALUES
    ('Ayıcık', 'peluş', 80, 'kahverengi'),
    ('Kale Seti', 'lego', 150, 'gri'),
    ('Zıpzıp', 'top', 20, 'sarı'),
    ('Barbi', 'bebek', 90, 'pembe');

-- Tüm oyuncaklar
SELECT * FROM oyuncaklar;

-- 80 ve üstü, sadece isim ve fiyat
SELECT isim, fiyat FROM oyuncaklar WHERE fiyat >= 80;

-- En pahalı 2 oyuncak
SELECT * FROM oyuncaklar ORDER BY fiyat DESC LIMIT 2;

-- Z ile başlayanlar
SELECT * FROM oyuncaklar WHERE isim LIKE 'Z%';

-- Sadece araba ve top
SELECT * FROM oyuncaklar WHERE cesit IN ('araba', 'top');

-- 20-60 lira arası
SELECT * FROM oyuncaklar WHERE fiyat BETWEEN 20 AND 60;

-- Şimşek'in rengini mavi yap
UPDATE oyuncaklar SET renk = 'mavi' WHERE isim = 'Şimşek';

-- Zıpzıp'ı sil
DELETE FROM oyuncaklar WHERE isim = 'Zıpzıp';

-- Yeni sütun ekle
ALTER TABLE oyuncaklar ADD COLUMN kimin TEXT;

-- Kale Seti'nin sahibini Ali yap
UPDATE oyuncaklar SET kimin = 'Ali' WHERE isim = 'Kale Seti';

-- cesit sütununun adını tur olarak değiştir
ALTER TABLE oyuncaklar RENAME COLUMN cesit TO tur;