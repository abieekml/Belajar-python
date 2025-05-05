def cari_minmax():
    # Mendapatkan input dari pengguna
    input_str = input("Masukkan urutan bilangan bulat yang dipisahkan spasi: ")
    
    # Mengkonversi string input menjadi daftar bilangan bulat
    try:
        angka = [int(num) for num in input_str.strip().split()]
        
        if not angka:
            return "Urutan kosong."
            
        # Mencari nilai minimum dan maksimum
        nilai_min = min(angka)
        nilai_max = max(angka)
        
        return f"Nilai minimum: {nilai_min}\nNilai maksimum: {nilai_max}"
    
    except ValueError:
        return "Input tidak valid. Harap masukkan hanya bilangan bulat yang dipisahkan spasi."
    
# Menjalankan fungsi
print(cari_minmax())