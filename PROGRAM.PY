# List untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi untuk menambah data mahasiswa
def tambah():
    print("\n-- Tambah Data Mahasiswa --")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    nilai_uts = float(input("Masukkan Nilai UTS: "))
    nilai_uas = float(input("Masukkan Nilai UAS: "))
    nilai_tugas = float(input("Masukkan Nilai Tugas: "))
    nilai_akhir = (nilai_uts + nilai_uas + nilai_tugas) / 3
    data_mahasiswa.append({
        "nim": nim,
        "nama": nama,
        "nilai_uts": nilai_uts,
        "nilai_uas": nilai_uas,
        "nilai_tugas": nilai_tugas,
        "nilai_akhir": nilai_akhir
    })
    print(f"Data mahasiswa {nama} berhasil ditambahkan.\n")

# Fungsi untuk menampilkan semua data mahasiswa
def tampilkan():
    print("\n-- Daftar Data Mahasiswa --")
    if len(data_mahasiswa) == 0:
        print("Belum ada data yang tersedia.\n")
    else:
        print("{:<10} {:<20} {:<10} {:<10} {:<10} {:<10}".format(
            "NIM", "Nama", "UTS", "UAS", "Tugas", "Akhir"))
        print("-" * 70)
        for mahasiswa in data_mahasiswa:
            print("{:<10} {:<20} {:<10} {:<10} {:<10} {:<10.2f}".format(
                mahasiswa['nim'], mahasiswa['nama'], 
                mahasiswa['nilai_uts'], mahasiswa['nilai_uas'], 
                mahasiswa['nilai_tugas'], mahasiswa['nilai_akhir']))
        print()

# Fungsi untuk menghapus data mahasiswa berdasarkan nama
def hapus(nama):
    print("\n-- Hapus Data Mahasiswa --")
    global data_mahasiswa
    data_mahasiswa = [m for m in data_mahasiswa if m['nama'].lower() != nama.lower()]
    print(f"Data mahasiswa dengan nama {nama} telah dihapus.\n")

# Fungsi untuk mengubah data mahasiswa berdasarkan nama
def ubah(nama):
    print("\n-- Ubah Data Mahasiswa --")
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nama'].lower() == nama.lower():
            print(f"Data ditemukan: {mahasiswa}")
            mahasiswa['nim'] = input("Masukkan NIM baru: ")
            mahasiswa['nama'] = input("Masukkan Nama baru: ")
            mahasiswa['nilai_uts'] = float(input("Masukkan Nilai UTS baru: "))
            mahasiswa['nilai_uas'] = float(input("Masukkan Nilai UAS baru: "))
            mahasiswa['nilai_tugas'] = float(input("Masukkan Nilai Tugas baru: "))
            mahasiswa['nilai_akhir'] = (mahasiswa['nilai_uts'] + mahasiswa['nilai_uas'] + mahasiswa['nilai_tugas']) / 3
            print(f"Data mahasiswa {nama} berhasil diubah.\n")
            return
    print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.\n")

# Menu utama
while True:
    print("Menu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1/2/3/4/5): ")
    
    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
        hapus(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama mahasiswa yang akan diubah: ")
        ubah(nama)
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")
