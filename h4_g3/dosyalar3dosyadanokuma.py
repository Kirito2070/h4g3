# rehber.txt dosyasına veri yazma
with open("rehber.txt", "a") as dosya:
    dosya.write("Musa|887\n")
    dosya.write("Deniz|745\n")

# rehber.txt dosyasını okuma ve ekrana yazdırma
with open("rehber.txt", "r") as d:
    okunan = d.readlines()  # Satırları liste olarak okur

for a in okunan:
    b = a.strip().split("|")  # Satır sonundaki boşlukları temizleyip "|" karakterine göre böler
    print(f"Adı:\t{b[0]}, \tNumarası:\t{int(b[1])}")  # Formatlı çıktı