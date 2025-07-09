from database import connect

def cari_buku_kategori():
    kategori = input("Masukkan kategori yang ingin dicari: ")

    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM buku WHERE kategori LIKE ?", ('%' + kategori + '%',))
    hasil = c.fetchall()
    conn.close()

    if hasil:
        print(f"\nBuku dengan kategori '{kategori}':")
        for b in hasil:
            print(f"- {b[1]} oleh {b[2]}")
    else:
        print(f"\nTidak ada buku ditemukan dalam kategori '{kategori}'.")
    print()
