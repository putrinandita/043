from database import setup
from fitur_buku import tambah_buku, tampilkan_semua_buku
from fitur_pencarian import cari_buku_kategori

def menu():
    setup()  # pastikan DB siap
    while True:
        print("=== Sistem Perpustakaan Digital ===")
        print("1. Tambah Buku")
        print("2. Tampilkan Semua Buku")
        print("3. Cari Buku berdasarkan Kategori")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            tampilkan_semua_buku()
        elif pilihan == "3":
            cari_buku_kategori()
        elif pilihan == "0":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid!\n")

if __name__ == "__main__":
    menu()
