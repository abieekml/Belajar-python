from datetime import datetime

def tukar_uang():
    # meminta nama pengguna
    nama_pengguna = input("Masukkan Nama Anda: ")

    # mendapatkan tanggal saat ini 
    tanggal_transaksi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # meminta nominal uang yang ingin ditukar
    while True:
        try: 
            nominal = float(input("Masukkan Nominal Uang Yang Ingin Ditukar: "))
            if nominal <= 0:
                print("Nominal Harus Lebih Dari 0.")
            else:
                break
        except ValueError:
            print("Input Tidak Valid. Harap Masukkan Angka.")

    # meminta jenis mata uang asal
    while True:
        jenis_uang_asal = input("Masukkan Jenis Mata Uang Asal (IDR, USD, EUR): ").upper()
        if jenis_uang_asal in ["IDR", "USD", "EUR"]:
            break
        else:
            print("Jenis Mata Uang Tidak Valid. Harap Masukkan IDR, USD, atau EUR.")

    # menampilkan pilihan tujuan penukaran
    print()
    print("|==============================|")
    print("| Pilih Tujuan Penukaran:      |")
    print("|==============================|")
    print("|1. IDR (Rupiah Indonesia)     |")
    print("|2. USD (Dolar Amerika Serikat)|")
    print("|3. EUR (Euro)                 |")
    print("|==============================|")

    # meminta pilihan tujuan penukaran
    while True:
        try:
            pilihan_tujuan = int(input("Masukkan Nomor Pilihan Tujuan Penukaran (1/2/3): "))
            if 1 <= pilihan_tujuan <= 3:
                break
            else: 
                print("Pilihan Tidak Valid. Harap Masukkan Angka Antara 1 dan 3.")
        except ValueError:
            print("Input Tidak Valid. Harap Masukkan Angka.")
    
    # Menentukan jenis mata uang tujuan berdasarkan pilihan
    if pilihan_tujuan == 1:
        jenis_uang_tujuan = "IDR"
    elif pilihan_tujuan == 2:
        jenis_uang_tujuan = "USD"
    else:
        jenis_uang_tujuan = "EUR"

    # Jika mata uang asal dan tujuan sama
    if jenis_uang_asal == jenis_uang_tujuan:
        hasil_penukaran = nominal
        print("\nPeringatan: Mata uang asal dan tujuan sama!")
    else:
        # Menentukan nilai tukar (kurs) - nilai kurs ini hanya contoh
        kurs_idr_usd = 0.000065
        kurs_idr_eur = 0.000060
        kurs_usd_idr = 15500
        kurs_usd_eur = 0.92
        kurs_eur_idr = 16500
        kurs_eur_usd = 1.09

        # Melakukan perhitungan penukaran berdasarkan jenis mata uang asal dan tujuan
        hasil_penukaran = 0
        if jenis_uang_asal == "IDR":
            if jenis_uang_tujuan == "USD":
                hasil_penukaran = nominal * kurs_idr_usd
            elif jenis_uang_tujuan == "EUR":
                hasil_penukaran = nominal * kurs_idr_eur
        elif jenis_uang_asal == "USD":
            if jenis_uang_tujuan == "IDR":
                hasil_penukaran = nominal * kurs_usd_idr
            elif jenis_uang_tujuan == "EUR":
                hasil_penukaran = nominal * kurs_usd_eur
        elif jenis_uang_asal == "EUR":
            if jenis_uang_tujuan == "IDR":
                hasil_penukaran = nominal * kurs_eur_idr
            elif jenis_uang_tujuan == "USD":
                hasil_penukaran = nominal * kurs_eur_usd

    # Menampilkan hasil penukaran
    print("\n--- Hasil Penukaran ---")
    print(f"Nama Pengguna: {nama_pengguna}")
    print(f"Tanggal Transaksi: {tanggal_transaksi}")
    print(f"Nominal Uang: {nominal} {jenis_uang_asal}")
    print(f"Jenis Uang Tujuan: {jenis_uang_tujuan}")
    print(f"Hasil Penukaran: {hasil_penukaran:.2f} {jenis_uang_tujuan}")
    print("------------------------")

# Memanggil fungsi tukar_uang untuk menjalankan program
if __name__ == "__main__":
    tukar_uang()