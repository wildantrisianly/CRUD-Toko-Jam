from tabulate import tabulate

tabel_jam_tangan = [
    {"kode": "J001", "nama": "Rolex Submariner", "kategori": "Pria", "stok": 4, "harga": 1500000, "tahun": 2020},
    {"kode": "J002", "nama": "Omega Seamaster", "kategori": "Pria", "stok": 3, "harga": 900000, "tahun": 2021},
    {"kode": "J003", "nama": "Cartier Tank", "kategori": "Wanita", "stok": 5, "harga": 250000, "tahun": 2019},
    {"kode": "J004", "nama": "Patek Philippe Nautilus", "kategori": "Pria", "stok": 7, "harga": 2500000, "tahun": 2022},
    {"kode": "J005", "nama": "Audemars Piguet Royal Oak", "kategori": "Unisex", "stok": 1, "harga": 300000, "tahun": 2023},
    {"kode": "J006", "nama": "Chanel J12", "kategori": "Wanita", "stok": 8, "harga": 95000, "tahun": 2021},
    {"kode": "J007", "nama": "Bulgari Serpenti", "kategori": "Wanita", "stok": 6, "harga": 130000, "tahun": 2022},
    {"kode": "J008", "nama": "Richard Mille RM 07-01", "kategori": "Unisex", "stok": 6, "harga": 350000, "tahun": 2023},
    {"kode": "J009", "nama": "Rolex Submariner 'Green Ice'", "kategori": "Pria", "stok": 7, "harga": 500000, "tahun": 2025},
    {"kode": "J010", "nama": "Patek Phillipe Nautilus 5811 Rose Gold Blue Dial", "kategori": "Pria", "stok": 5, "harga": 100000, "tahun": 2025},
    {"kode": "J011", "nama": "Cartier 'Reflection de Cartier'", "kategori": "Wanita", "stok": 5, "harga": 500000, "tahun": 2024}
]

def tampilkan_jam(jam_list):
    headers = ["Kode", "Nama", "Kategori", "Stok", "Harga", "Tahun"]
    rows = []
    for jam in jam_list:
        rows.append([
            jam["kode"],
            jam["nama"],
            jam["kategori"],
            jam["stok"],
            jam["harga"],
            jam["tahun"]
        ])
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

# untuk validasi input angka
def is_integer(input_str):
    return input_str.isdigit() 

#tampilkan jam
def menu_tampilkan_jam():
    while True:
        print("\nSub Menu Tampilkan Jam Tangan:")
        print("1. Tampilkan Semua Jam")
        print("2. Tampilkan Jam Tertentu")
        print("3. Kembali ke Menu Utama")
        
        pilihan = input("Masukkan pilihan (1-3): ")
        
        if pilihan == "1":
            tampilkan_jam(tabel_jam_tangan)
            
        elif pilihan == "2":
            print("\nFilter berdasarkan:")
            print("1. Kode")
            print("2. Nama")
            print("3. Kategori")
            print("4. Tahun")
            print("5. Harga")
            
            filter_pilihan = input("Pilih filter (1-5): ")
            
            if filter_pilihan == "1":
                kode = input("Masukkan kode jam: ").upper()
                hasil = [jam for jam in tabel_jam_tangan if jam["kode"] == kode] #menggunakan list comprehension
                
            elif filter_pilihan == "2":
                nama = input("Masukkan nama jam: ").lower() 
                hasil = [jam for jam in tabel_jam_tangan if nama in jam["nama"].lower()] #memakai in lagi agar bisa partial search
                
            elif filter_pilihan == "3":
                kategori = input("Masukkan kategori (Pria/Wanita/Unisex): ").capitalize() #agar huruf pertama capital
                hasil = [jam for jam in tabel_jam_tangan if jam["kategori"] == kategori]
                
            elif filter_pilihan == "4":
                while True:
                    tahun = input("Masukkan tahun (4 digit): ")
                    if is_integer(tahun) and len(tahun) == 4: #agar panjangnya 4 digit
                        hasil = [jam for jam in tabel_jam_tangan if jam["tahun"] == int(tahun)]
                        break
                    else:
                        print("Tahun harus berupa 4 digit angka! Silakan coba lagi.")
                
            elif filter_pilihan == "5":
                while True:
                    harga = input("Masukkan harga: ")
                    if is_integer(harga):
                        hasil = [jam for jam in tabel_jam_tangan if jam["harga"] == int(harga)]
                        break
                    else:
                        print("Harga harus berupa angka! Silakan coba lagi.")
                
            else:
                print("Pilihan filter tidak valid!")
                continue
            
            if len(hasil) == 0:  # Changed from 'if not hasil'
                print("\nTidak tersedia jam dengan kriteria tersebut")
            else:
                tampilkan_jam(hasil)
                
        elif pilihan == "3":
            break
            
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Penambahan Jam 
def tambah_jam():
    print("\nTambah Jam Tangan Baru")
    while True:
        kode = input("Masukkan kode jam (format JXXX): ").strip().upper() #memakai strip agar menghilangkan spasi diawal dan akhir
        if len(kode) != 4 or not kode.startswith("J") or not kode[1:].isdigit(): #stringslicing 3 digit terakhir 
            print("Format kode tidak valid. Harus J diikuti 3 angka (contoh: J001)")
            continue
            
        if any(jam["kode"] == kode for jam in tabel_jam_tangan): #menggunakan any agar lebih ringkas
            print("Kode jam sudah ada. Silakan gunakan kode lain.")
            continue
            
        break
    
    nama = input("Masukkan nama jam: ").strip().title() # menggunakan .title agar kapitalisasi tiap awal kata
    
    while True:
        tahun = input("Masukkan tahun produksi: ")
        if not is_integer(tahun):
            print("Tahun harus berupa angka")
            continue
        tahun = int(tahun)
        if tahun < 1900 or tahun > 2025:
            print("Tahun harus antara 1900 sampai 2025")
            continue
            
        # Cek apakah sudah ada jam dengan nama dan tahun yang sama
        if any(jam["nama"].lower() == nama.lower() and jam["tahun"] == tahun for jam in tabel_jam_tangan):
            print(f"Jam dengan nama '{nama}' dan tahun {tahun} sudah ada.")
            print("Silakan masukkan tahun produksi yang berbeda untuk jam dengan nama yang sama.")
            continue
        break
    
    while True:
        kategori = input("Masukkan kategori (Pria/Wanita/Unisex): ").strip().capitalize()
        if kategori not in ["Pria", "Wanita", "Unisex"]:
            print("Kategori harus Pria, Wanita, atau Unisex")
            continue
        break
    
    while True:
        stok = input("Masukkan stok: ")
        if not is_integer(stok):
            print("Stok harus berupa angka positif")
            continue
        stok = int(stok)
        if stok < 0:
            print("Stok tidak boleh negatif")
            continue
        break
    
    while True:
        harga = input("Masukkan harga: ")
        if not is_integer(harga):
            print("Harga harus berupa angka positif")
            continue
        harga = int(harga)
        if harga <= 0:
            print("Harga harus lebih dari 0")
            continue
        break
    
    jam_baru = {
        "kode": kode,
        "nama": nama,
        "kategori": kategori,
        "stok": stok,
        "harga": harga,
        "tahun": tahun
    }
    
    print("\nData jam yang akan ditambahkan:")
    tampilkan_jam([jam_baru])
    
    while True:  
        konfirmasi = input("Apakah Data akan disimpan? (Y/N): ").strip().upper()
        if konfirmasi == "Y":
            tabel_jam_tangan.append(jam_baru)
            print("Data jam berhasil ditambahkan!")
            break
        elif konfirmasi == "N":
            print("Data jam tidak disimpan.")
            break
        else:
            print("Harap masukkan huruf 'Y' atau 'N' saja!")

# Update jam tangan
def update_jam():
    print("\nUpdate Data Jam Tangan")
    tampilkan_jam(tabel_jam_tangan)
    
    while True:
        kode_lama = input("\nMasukkan kode jam yang akan diupdate: ").strip().upper()
        
        jam_diupdate = ""  
        index_jam = -1
        for i, jam in enumerate(tabel_jam_tangan):
            if jam["kode"] == kode_lama:
                jam_diupdate = jam
                index_jam = i
                break
        
        if jam_diupdate == "": 
            print("Kode jam tidak ditemukan. Silakan coba lagi.")
            continue
            
        print("\nData jam yang akan diupdate:")
        tampilkan_jam([jam_diupdate])
        
        print("\nMasukkan data baru (tekan 'enter' untuk tidak mengubah):")
        
        # Input kode baru dengan validasi
        while True:
            kode_baru = input(f"Kode ({jam_diupdate['kode']}): ").strip().upper()
            if not kode_baru:  # Jika dikosongkan, gunakan kode lama
                kode_baru = kode_lama
                break
            if len(kode_baru) != 4 or not kode_baru.startswith("J") or not kode_baru[1:].isdigit():
                print("Format kode tidak valid. Harus J diikuti 3 angka (contoh: J001)")
                continue
            if kode_baru != kode_lama and any(jam["kode"] == kode_baru for jam in tabel_jam_tangan):
                print("Kode jam sudah digunakan. Silakan gunakan kode lain.")
                continue
            break
        
        nama = input(f"Nama ({jam_diupdate['nama']}): ").strip()
        if not nama:
            nama = jam_diupdate["nama"]
            
        while True:
            kategori = input(f"Kategori ({jam_diupdate['kategori']} - Pria/Wanita/Unisex): ").strip().capitalize()
            if not kategori:
                kategori = jam_diupdate["kategori"]
                break
            if kategori not in ["Pria", "Wanita", "Unisex"]:
                print("Kategori harus Pria, Wanita, atau Unisex")
                continue
            break
        
        while True:
            stok = input(f"Stok ({jam_diupdate['stok']}): ").strip()
            if not stok:
                stok = jam_diupdate["stok"]
                break
            if not is_integer(stok):
                print("Stok harus berupa angka positif")
                continue
            stok = int(stok)
            if stok < 0:
                print("Stok tidak boleh negatif")
                continue
            break
        
        while True:
            harga = input(f"Harga ({jam_diupdate['harga']}): ").strip()
            if not harga:
                harga = jam_diupdate["harga"]
                break
            if not is_integer(harga):
                print("Harga harus berupa angka positif")
                continue
            harga = int(harga)
            if harga <= 0:
                print("Harga harus lebih dari 0")
                continue
            break
        
        while True:
            tahun = input(f"Tahun ({jam_diupdate['tahun']}): ").strip()
            if not tahun:
                tahun = jam_diupdate["tahun"]
                break
            if not is_integer(tahun):
                print("Tahun harus berupa angka")
                continue
            tahun = int(tahun)
            if tahun < 1900 or tahun > 2025:
                print("Tahun harus antara 1900 sampai 2025")
                continue
            break
        
        # Buat dictionary baru dengan data yang diupdate
        jam_updated = {
            "kode": kode_baru,
            "nama": nama,
            "kategori": kategori,
            "stok": stok,
            "harga": harga,
            "tahun": tahun
        }
        
        print("\nData jam setelah update:")
        tampilkan_jam([jam_updated])

        while True:
            konfirmasi = input("Apakah Data akan disimpan? (Y/N): ").strip().upper()
            if konfirmasi == "Y":
                tabel_jam_tangan[index_jam] = jam_updated
                print("Data jam berhasil diupdate!")
                break
            elif konfirmasi == "N":
                print("Perubahan data jam dibatalkan.")
                break
            else:
                print("Harap masukkan Y/N saja!")
        break
        

# hapus jam        
def hapus_jam(): 
    print("\nHapus Data Jam Tangan")
    tampilkan_jam(tabel_jam_tangan)
    
    while True:
        kode = input("\nMasukkan kode jam yang akan dihapus: ").strip().upper()
        
        jam_dihapus = ""  
        index_jam = -1
        for i, jam in enumerate(tabel_jam_tangan):
            if jam["kode"] == kode:
                jam_dihapus = jam
                index_jam = i
                break
        
        if jam_dihapus == "":  
            print("Kode jam tidak ditemukan. Silakan coba lagi.")
            continue
            
        print("\nData jam yang akan dihapus:")
        tampilkan_jam([jam_dihapus])
        
        while True: 
            konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (Y/N): ").strip().upper()
            if konfirmasi == "Y":
                del tabel_jam_tangan[index_jam]
                print("Data jam berhasil dihapus!")
                break
            elif konfirmasi == "N":
                print("Penghapusan data dibatalkan.")
                break
            else:
                print("Harap masukkan huruf 'Y' atau 'N' saja!")
        break

# Pembelian jam
def beli_jam():
    print("\nMenu Pembelian Jam Tangan")
    tampilkan_jam(tabel_jam_tangan)
    
    keranjang = []
    total_harga = 0
    
    while True:
        kode = input("\nMasukkan kode jam yang ingin dibeli (tekan Enter untuk selesai): ").strip().upper()
        if not kode:
            break
        
        jam_dibeli = ""  
        for jam in tabel_jam_tangan:
            if jam["kode"] == kode:
                jam_dibeli = jam
                break
        
        if jam_dibeli == "":  
            print("Kode jam tidak ditemukan. Silakan coba lagi.")
            continue
        
        print(f"\nAnda memilih: {jam_dibeli['nama']} (Stok: {jam_dibeli['stok']})")
        
        while True:
            jumlah = input("Masukkan jumlah yang ingin dibeli: ")
            if not is_integer(jumlah):
                print("Jumlah harus berupa angka positif")
                continue
            jumlah = int(jumlah)
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0")
                continue
            if jumlah > jam_dibeli["stok"]:
                print(f"Stok tidak mencukupi. Stok tersedia: {jam_dibeli['stok']}")
                continue
            break
        
        subtotal = jam_dibeli["harga"] * jumlah
        keranjang.append({
            "kode": jam_dibeli["kode"],
            "nama": jam_dibeli["nama"],
            "harga": jam_dibeli["harga"],
            "jumlah": jumlah,
            "subtotal": subtotal
        })
        total_harga += subtotal
        
        print(f"{jam_dibeli['nama']} ({jumlah}x) ditambahkan ke keranjang.")
    
    if len(keranjang) == 0:  # Changed from 'if not keranjang'
        print("Tidak ada jam yang dibeli.")
        return
    
    print("\n=== Struk Pembelian ===")
    headers = ["No", "Nama", "Harga", "Jumlah", "Subtotal"]
    rows = []
    for i, item in enumerate(keranjang, 1):
        rows.append([
            i,
            item["nama"],
            f"Rp.{item['harga']}",
            item["jumlah"],
            f"Rp.{item['subtotal']}"
        ])
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
    print("-" * 50)
    print(f"Total Harga: Rp.{total_harga}")
    
    while True:
        konfirmasi = input("\nApakah Anda yakin ingin melanjutkan pembelian? (Y/N): ").strip().upper()
        if konfirmasi == "Y":
            # Proses pembayaran
            while True:
                uang_dibayar = input(f"\nMasukkan jumlah uang yang dibayarkan (Total: Rp.{total_harga}): Rp.")
                if not is_integer(uang_dibayar):
                    print("Masukkan harus berupa angka!")
                    continue
                
                uang_dibayar = int(uang_dibayar)
                
                if uang_dibayar < total_harga:
                    kurang = total_harga - uang_dibayar
                    print(f"\nUang Anda kurang sebesar Rp.{kurang}")
                    print("Silakan masukkan jumlah uang yang cukup.")
                    continue
                break
            
            # Update stok dan tampilkan struk
            for item in keranjang:
                for jam in tabel_jam_tangan:
                    if jam["kode"] == item["kode"]:
                        jam["stok"] -= item["jumlah"]
                        break
            
            print("\n=== Struk Pembayaran ===")
            print(f"Total Harga: Rp.{total_harga}")
            print(f"Uang Dibayar: Rp.{uang_dibayar}")
            
            if uang_dibayar > total_harga:
                kembalian = uang_dibayar - total_harga
                print(f"Kembalian: Rp.{kembalian}")
            
            print("\nTerima kasih telah berbelanja di Toko Jam Wild!")
            break
            
        elif konfirmasi == "N":
            print("\nPembelian dibatalkan.")
            break
        else:
            print("Harap masukkan huruf 'Y' atau 'N' saja!")

# Kode utama program
print("\n=== SELAMAT DATANG DI TOKO JAM WILD ===")

while True:
    print("\n=== MENU UTAMA ===")
    print("1. Menampilkan Daftar Jam Tangan")
    print("2. Menambah Jam Tangan Baru")
    print("3. Update Data Jam Tangan")
    print("4. Hapus Data Jam Tangan")
    print("5. Membeli Jam Tangan")
    print("6. Keluar Program")
    
    pilihan = input("Masukkan pilihan menu (1-6): ")
    
    if pilihan == "1":
        menu_tampilkan_jam()
    elif pilihan == "2":
        while True:
            print("\nSub Menu Tambah Jam Tangan:")
            print("1. Tambah jam tangan")
            print("2. Kembali ke menu utama")
            sub_pilihan = input("Masukkan pilihan (1-2): ")
            if sub_pilihan == "1":
                tambah_jam()
            elif sub_pilihan == "2":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    elif pilihan == "3":
        while True:
            print("\nSub Menu Update Jam Tangan:")
            print("1. Update data jam tangan")
            print("2. Kembali ke menu utama")
            sub_pilihan = input("Masukkan pilihan (1-2): ")
            if sub_pilihan == "1":
                update_jam()
            elif sub_pilihan == "2":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    elif pilihan == "4":
        while True:
            print("\nSub Menu Hapus Jam Tangan:")
            print("1. Hapus data jam tangan")
            print("2. Kembali ke menu utama")
            sub_pilihan = input("Masukkan pilihan (1-2): ")
            if sub_pilihan == "1":
                hapus_jam()
            elif sub_pilihan == "2":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    elif pilihan == "5":
        beli_jam()
    elif pilihan == "6":
        print("\nTerima kasih sudah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")