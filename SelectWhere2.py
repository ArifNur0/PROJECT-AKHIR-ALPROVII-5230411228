import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

#Tampilkan data berdasarkan parameter mamalia)
kursor.execute("SELECT * FROM HEWAN WHERE Jumlah_Skrg <= 1000 ")
baris_tabel = kursor.fetchall()

#BUAT TABEL PEGAWAI
print("DATA HEWAN jumlahnya kurang dari sama dengan 1000 ekor saja.")
print("="*80)
print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID HEWAN","NAMA HEWAN" , "JENIS" , "ASAL" , "JUMLAH SAAT INI","TAHUN TERAKHIR DITEMUKAN"))

for baris in baris_tabel:
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0] , baris[1] , baris[2] , baris[3] , baris[4],baris[5]))
    
print("-"*80)

koneksi.commit()
koneksi.close()