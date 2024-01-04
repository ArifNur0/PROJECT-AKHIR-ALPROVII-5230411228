
import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

koneksi.execute(
    ''' 
    CREATE TABLE HEWAN (
        Id_hewan INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_hewan VARCHAR(50),
        Jenis_Hewan VARCHAR(50),
        Asal VARCHAR(50),
        Jumlah_skrg INTEGER(10),
        tahun_ditemukan  INTEGER(10)
    )
'''
)

koneksi.close()