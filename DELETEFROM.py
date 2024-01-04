import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()


# Menjalankan query DELETE
Jenis_Hewan = 10  
kursor.execute(f"DELETE FROM HEWAN WHERE Jenis_Hewan = ?", (Id_hewan,))
koneksi.commit()

# Menampilkan pesan setelah penghapusan berhasil
if kursor.rowcount > 0:
    print(f"Data dengan ID {Id_hewan} berhasil dihapus.")
else:
    print(f"Tidak ada data dengan ID {Id_hewan}.")


koneksi.close()