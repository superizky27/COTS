import xmlrpc.client


s = xmlrpc.client.ServerProxy('http://127.0.0.1:8080')

print("1 Daftar Film dan Jam Tayang")
print("2 Pesan Tiket Bioskop")
print("3 Harga Tiket")
print("4 Sisa Tiket yang Tersedia")

print("==========")
print("5 Admin")
print("Ubah jam Tayang")
print("Ubah Harga Tiket")

print(s.show())

'''
buat tampilan untuk daftar film yang sedang tayang, 
pemesanan tiket bioskop, 
melihat harga tiket,
dan melihat sisa tiket yang tersedia, 
serta mengubah daftar film dan harga tiket yang sedang tayang.
'''