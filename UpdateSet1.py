import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()
# Update jumlah saat ini dari hewan ‘Orangutan’ menjadi 900
Id_hewan = 1
jumlah_baru = 900
kursor.execute(f'''
               UPDATE HEWAN SET Jumlah_skrg = {jumlah_baru} WHERE Id_hewan = {Id_hewan}
''')

koneksi.commit()

if kursor.rowcount> 0:
    print(f"DATA  DENGAN ID {Id_hewan} BERHASIL DIUBAH")

else:
    print(f"TIDAK ADA DATA HEWAN DENGAN ID{Id_hewan}")

koneksi.close()
