import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

koneksi.execute('''
                INSERT INTO HEWAN (nama_hewan,Jenis_Hewan,Asal,Jumlah_skrg,  tahun_ditemukan)
                VALUES('Orangutan','mamalia','Sumatera',14000,2021)
                ''')

koneksi.execute('''
                INSERT INTO HEWAN (nama_hewan,Jenis_Hewan,Asal,Jumlah_skrg,  tahun_ditemukan)
                VALUES('Harimau Sumatera','mamalia','Sumatera',400,2020)
                ''')

koneksi.execute('''
                INSERT INTO HEWAN (nama_hewan,Jenis_Hewan,Asal,Jumlah_skrg,  tahun_ditemukan)
                VALUES('Komodo','reptil','Nusa Tenggara',3000,2019)
                ''')

koneksi.execute('''
                INSERT INTO HEWAN (nama_hewan,Jenis_Hewan,Asal,Jumlah_skrg,  tahun_ditemukan)
                VALUES('Anoa','mamalia','Sulawesi',5000,2022)
                ''')

koneksi.execute('''
                INSERT INTO HEWAN (nama_hewan,Jenis_Hewan,Asal,Jumlah_skrg,  tahun_ditemukan)
                VALUES('Badak Jawa','mamalia','Jawa',72,2021)
                ''')

koneksi.execute('''
                INSERT INTO HEWAN (nama_hewan,Jenis_Hewan,Asal,Jumlah_skrg,  tahun_ditemukan)
                VALUES('Kuskus','mamalia','papua',50,2020)
                ''')

koneksi.execute('''
                INSERT INTO HEWAN (nama_hewan,Jenis_Hewan,Asal,Jumlah_skrg,  tahun_ditemukan)
                VALUES('Trenggiling','mamalia','Sumatera',90,2022)
                ''')

koneksi.execute('''
                INSERT INTO HEWAN (nama_hewan,Jenis_Hewan,Asal,Jumlah_skrg,  tahun_ditemukan)
                VALUES('Burung Cendrawasih','burung','papua',45,2021)
                ''')

koneksi.execute('''
                INSERT INTO HEWAN (nama_hewan,Jenis_Hewan,Asal,Jumlah_skrg,  tahun_ditemukan)
                VALUES('Penyu Hijau','reptil','Nusa Tenggara Timur',20,2022)
                ''')

koneksi.execute('''
                INSERT INTO HEWAN (nama_hewan,Jenis_Hewan,Asal,Jumlah_skrg,  tahun_ditemukan)
                VALUES('Gajah Sumatera','mamalia','Sumatera',2500,2023)
                ''')



koneksi.commit()
koneksi.close()