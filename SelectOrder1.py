import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

#Urutkan nama hewan berdasarkan dari awal alphabetic.
kursor.execute("SELECT * FROM HEWAN ORDER BY nama_hewan ASC  ")
baris_tabel = kursor.fetchall()

#BUAT TABEL HEWAN
print("DATA HEWAN Urutkan nama hewan berdasarkan dari awal alphabetic.")
print("="*80)
print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID HEWAN","NAMA HEWAN" , "JENIS" , "ASAL" , "JUMLAH SAAT INI","TAHUN TERAKHIR DITEMUKAN"))

for baris in baris_tabel:
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0] , baris[1] , baris[2] , baris[3] , baris[4],baris[5]))
    
print("-"*80)
koneksi.commit()
koneksi.close()
