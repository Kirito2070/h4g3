import os

# Dosya adı
dosya_adi = "araclar.txt"

# Varsayılan araç verilerini dosyaya yaz
if not os.path.exists(dosya_adi):  # Eğer dosya yoksa oluştur
    with open(dosya_adi, "w") as dosya:
        dosya.write("BMW X5|SUV\n")
        dosya.write("Toyota Corolla|Sedan\n")
        dosya.write("Ford F-150|Pickup\n")
        dosya.write("Honda Civic|Hatchback\n")

# Menü çerçevesi
def cizgi():
    print("=" * 40)

# Dosyayı oku ve ekrana yazdır
def dosyayi_oku():
    with open(dosya_adi, "r") as dosya:
        araclar = dosya.readlines()

    cizgi()
    print("🚗  MEVCUT ARAÇ LİSTESİ  🚗".center(40))
    cizgi()
    
    for arac in araclar:
        b = arac.strip().split("|")
        print(f"📌 Araç: {b[0].ljust(20)} Türü: {b[1]}")
    
    cizgi()

# Dosyaya yeni araç ekleme fonksiyonu
def yeni_arac_ekle():
    arac_adi = input("📝 Araç modelini girin: ")
    arac_turu = input("🚘 Araç türünü girin: ")

    with open(dosya_adi, "a") as dosya:
        dosya.write(f"{arac_adi}|{arac_turu}\n")

    print(f"✅ {arac_adi} başarıyla eklendi!")

# Araç arama fonksiyonu
def arac_ara():
    aranan = input("🔍 Aramak istediğiniz aracın adını girin: ").lower()
    
    with open(dosya_adi, "r") as dosya:
        araclar = dosya.readlines()
    
    bulundu = False
    cizgi()
    print("🔎 ARAMA SONUÇLARI 🔎".center(40))
    cizgi()
    
    for arac in araclar:
        b = arac.strip().split("|")
        if aranan in b[0].lower():
            print(f"📌 Araç: {b[0].ljust(20)} Türü: {b[1]}")
            bulundu = True
    
    if not bulundu:
        print("🚫 Aradığınız araç bulunamadı!")

    cizgi()

# Araç silme fonksiyonu
def arac_sil():
    silinecek = input("🗑 Silmek istediğiniz aracın adını girin: ").lower()

    with open(dosya_adi, "r") as dosya:
        araclar = dosya.readlines()

    yeni_araclar = [arac for arac in araclar if silinecek not in arac.lower()]
    
    if len(yeni_araclar) == len(araclar):
        print("🚫 Araç bulunamadı, silinemedi!")
    else:
        with open(dosya_adi, "w") as dosya:
            dosya.writelines(yeni_araclar)
        print(f"✅ {silinecek.capitalize()} başarıyla silindi!")

# Ana menü
while True:
    cizgi()
    print("🚗  ARAÇ YÖNETİM SİSTEMİ  🚗".center(40))
    cizgi()
    print("1️⃣  Araçları Listele")
    print("2️⃣  Yeni Araç Ekle")
    print("3️⃣  Araç Ara")
    print("4️⃣  Araç Sil")
    print("5️⃣  Çıkış")
    cizgi()

    secim = input("🎯 Seçiminizi yapın: ")

    if secim == "1":
        dosyayi_oku()
    elif secim == "2":
        yeni_arac_ekle()
    elif secim == "3":
        arac_ara()
    elif secim == "4":
        arac_sil()
    elif secim == "5":
        print("👋 Programdan çıkılıyor... Güle güle!")
        break
    else:
        print("🚫 Geçersiz seçim, tekrar deneyin!")