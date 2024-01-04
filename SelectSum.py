import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

kursor.execute("SELECT SUM(JUmlah_skrg) FROM HEWAN")
#Jumlahkan total populasi hewan langka saat ini (Jumlah Saat Ini).
total_langka = kursor.fetchone()[0]
print(f"total populasi hewan langka saat ini {total_langka}")



koneksi.commit()
koneksi.close()