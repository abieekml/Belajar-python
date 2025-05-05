def cari_kata_terpanjang():
    # Mendapatkan input dari pengguna
    kalimat = input("Masukkan sebuah kalimat: ")
    
    # Memecah kalimat menjadi kata-kata
    kata = kalimat.split()
    
    if not kata:
        return "Kalimat kosong."
        
    # Mencari kata terpanjang
    kata_terpanjang = max(kata, key=len)
    
    return f"Kata terpanjang adalah '{kata_terpanjang}' dengan {len(kata_terpanjang)} karakter."
    
# Menjalankan fungsi
print(cari_kata_terpanjang())