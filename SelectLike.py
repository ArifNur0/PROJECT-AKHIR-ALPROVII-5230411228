import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

# Cari nama hewan yang diawali dengan karakter “B”
nama = 'B%' 
kursor.execute(f"SELECT * FROM HEWAN WHERE nama_hewan LIKE ?", (nama,))
baris_table = kursor.fetchall()

print("DATA HEWAN yang diawali dengan karakter “B”")
print("="*80)
print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID HEWAN","NAMA HEWAN" , "JENIS" , "ASAL" , "JUMLAH SAAT INI","TAHUN TERAKHIR DITEMUKAN"))
for baris in baris_table:
       print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0] , baris[1] , baris[2] , baris[3] , baris[4],baris[5]))
    
print("-"*80)

koneksi.commit()
koneksi.close()

