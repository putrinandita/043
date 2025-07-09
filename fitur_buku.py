from database import connect

def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    kategori = input("Masukkan kategori: ")

    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO buku (judul, penulis, kategori) VALUES (?, ?, ?)", 
              (judul, penulis, kategori))
    conn.commit()
    conn.close()
    print("✅ Buku berhasil ditambahkan.\n")

def tampilkan_semua_buku():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM buku")
    buku = c.fetchall()
    conn.close()

    print("\n📚 Daftar Buku:")
    for b in buku:
        print(f"- {b[1]} oleh {b[2]} [{b[3]}]")
    print()
