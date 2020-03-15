import xmlrpc.client
import os
import getpass


s = xmlrpc.client.ServerProxy('http://127.0.0.1:8080')
user = "admin"
pw = "admin"

def menu1(s):
	os.system('cls')
	film1 = s.show1()
	print("Judul Film: ", film1["Judul"])
	print("Jam Tayang: ", film1["Jam"]," Studio: ", film1["Studio"])
	print("Harga Tiket: ", film1["Harga"])
	print("Sisa Tiket: ", film1["Sisa"])
	print("=================")

	film2 = s.show2()
	print("Judul Film: ", film2["Judul"])
	print("Jam Tayang: ", film2["Jam"]," Studio: ", film2["Studio"])
	print("Harga Tiket: ", film2["Harga"])
	print("Sisa Tiket: ", film2["Sisa"])
	print("=================")

	film3 = s.show3()
	print("Judul Film: ", film3["Judul"])
	print("Jam Tayang: ", film3["Jam"]," Studio: ", film3["Studio"])
	print("Harga Tiket: ", film3["Harga"])
	print("Sisa Tiket: ", film3["Sisa"])
	print("=================")

	film4 = s.show4()
	print("Judul Film: ", film4["Judul"])
	print("Jam Tayang: ", film4["Jam"]," Studio: ", film4["Studio"])
	print("Harga Tiket: ", film4["Harga"])
	print("Sisa Tiket: ", film4["Sisa"])
	print("=================")

	film5 = s.show5()
	print("Judul Film: ", film5["Judul"])
	print("Jam Tayang: ", film5["Jam"]," Studio: ", film5["Studio"])
	print("Harga Tiket: ", film5["Harga"])
	print("Sisa Tiket: ", film5["Sisa"])
	print("=================")

	film6 = s.show6()
	print("Judul Film: ", film6["Judul"])
	print("Jam Tayang: ", film6["Jam"]," Studio: ", film6["Studio"])
	print("Harga Tiket: ", film6["Harga"])
	print("Sisa Tiket: ", film6["Sisa"])
	print("=================")

	input("Press enter to Go back to main menu ;)")
	main()

def menu2(s):
	os.system('cls')
	print("Silahkan pilih film yang ingin anda Pesan :D")
	film1 = s.show1()
	print("1: ", film1["Judul"], "\t\t\t\tJam: ", film1["Jam"])
	film2 = s.show2()
	print("2: ", film2["Judul"], "\t\t\tJam: ", film2["Jam"])
	film3 = s.show3()
	print("3: ", film3["Judul"], "\t\tJam: ", film3["Jam"])
	film4 = s.show4()
	print("4: ", film4["Judul"], "\tJam: ", film4["Jam"])
	film5 = s.show5()
	print("5: ", film5["Judul"], "\t\t\t\tJam: ", film5["Jam"])
	film6 = s.show6()
	print("5: ", film6["Judul"], "\t\t\t\tJam: ", film6["Jam"])

	movchose = int(input("Film yang ingin anda Pesan:	"))
	jumlahtiket = int(input("Jumlah Tiket yang ingin anda pesan:	"))


	if (movchose == 1):
		s.pesan1(jumlahtiket)
		print("Berhasil Memesan sejumlah %s tiket, Silahkan melanjutkan pembayaran" % jumlahtiket)
	elif (movchose == 2):
		s.pesan2(jumlahtiket)
		print("Berhasil Memesan sejumlah %s tiket, Silahkan melanjutkan pembayaran" % jumlahtiket)
	elif (movchose == 3):
		s.pesan3(jumlahtiket)
		print("Berhasil Memesan sejumlah %s tiket, Silahkan melanjutkan pembayaran" % jumlahtiket)
	elif (movchose == 4):
		s.pesan4(jumlahtiket)
		print("Berhasil Memesan sejumlah %s tiket, Silahkan melanjutkan pembayaran" % jumlahtiket)
	elif (movchose == 5):
		s.pesan5(jumlahtiket)
		print("Berhasil Memesan sejumlah %s tiket, Silahkan melanjutkan pembayaran" % jumlahtiket)
	elif (movchose == 6):
		s.pesan6(jumlahtiket)
		print("Berhasil Memesan sejumlah %s tiket, Silahkan melanjutkan pembayaran" % jumlahtiket)
	else :
		print("Maaf silahkan masukkan yang benar")
		input("")
		menu2(s)

	input("Press enter to Go back to main menu ;)")
	main()

def menu3(s, user, pw):
	os.system("cls")
	print("Silahkan login terlebih dahulu")
	username = input("Username: ")
	#pwd = input("Password: ")
	password = getpass.getpass()
	if (username!=user and password!=pw):
		print("Password anda salah")
		print("")
		menu3(s, user, pw)
	else :
		print("Benar, Selamat datang")
		print("==================")
		print("Menu Admin: ")
		
		film1 = s.show1()
		print("1: ", film1["Judul"])
		film2 = s.show2()
		print("2: ", film2["Judul"])
		film3 = s.show3()
		print("3: ", film3["Judul"])
		film4 = s.show4()
		print("4: ", film4["Judul"])
		film5 = s.show5()
		print("5: ", film5["Judul"])
		film6 = s.show6()
		print("6: ", film6["Judul"])
		print("=================")
		movchose = int(input("Pilih film"))
		if (movchose == 1):
			judul = input("Ubah judul (Kosongkan jika tidak ingin diubah)\t")
			tiket = input("Ubah sisa tiket yang tersedia(Kosongkan jika tidak ingin diubah)\t")
			if judul == "":
				judul = film1['Judul']
			if tiket == "":
				tiket = film1["Sisa"]
			s.edit1(judul, tiket)
			print("Edit berhasil, enter untuk kembali ke main menu")
			input("")
			main()
		elif (movchose == 2):
			judul = input("Ubah judul (Kosongkan jika tidak ingin diubah)\t")
			tiket = input("Ubah sisa tiket yang tersedia(Kosongkan jika tidak ingin diubah)\t")
			if judul == "":
				judul = film2['Judul']
			if tiket == "":
				tiket = film2["Sisa"]
			s.edit2(judul, tiket)
			print("Edit berhasil, enter untuk kembali ke main menu")
			input("")
			main()
		elif (movchose == 3):
			judul = input("Ubah judul (Kosongkan jika tidak ingin diubah)\t")
			tiket = input("Ubah sisa tiket yang tersedia(Kosongkan jika tidak ingin diubah)\t")
			if judul == "":
				judul = film3['Judul']
			if tiket == "":
				tiket = film3["Sisa"]
			s.edit3(judul, tiket)
			print("Edit berhasil, enter untuk kembali ke main menu")
			input("")
			main()
		elif (movchose == 4):
			judul = input("Ubah judul (Kosongkan jika tidak ingin diubah)\t")
			tiket = input("Ubah sisa tiket yang tersedia(Kosongkan jika tidak ingin diubah)\t")
			if judul == "":
				judul = film4['Judul']
			if tiket == "":
				tiket = film4["Sisa"]
			s.edit4(judul, tiket)
			print("Edit berhasil, enter untuk kembali ke main menu")
			input("")
			main()
		elif (movchose == 5):
			judul = input("Ubah judul (Kosongkan jika tidak ingin diubah)\t")
			tiket = input("Ubah sisa tiket yang tersedia(Kosongkan jika tidak ingin diubah)\t")
			if judul == "":
				judul = film5['Judul']
			if tiket == "":
				tiket = film5["Sisa"]
			s.edit5(judul, tiket)
			print("Edit berhasil, enter untuk kembali ke main menu")
			input("")
			main()
		elif (movchose == 6):
			judul = input("Ubah judul (Kosongkan jika tidak ingin diubah)\t")
			tiket = input("Ubah sisa tiket yang tersedia(Kosongkan jika tidak ingin diubah)\t")
			if judul == "":
				judul = film6['Judul']
			if tiket == "":
				tiket = film6["Sisa"]
			s.edit6(judul, tiket)
			print("Edit berhasil, enter untuk kembali ke main menu")
			input("")
			main()
		else :
			print("Engga ada bro")
			print("")
			menu3(s, user, pw)



def main():
	os.system('cls')
	menuSelect= ""
	print("1 Daftar Film dan Jam Tayang")
	print("2 Pesan Tiket Bioskop")
	print("==================")
	print("3 Admin")


	menuSelect=int(input("Masukkan pilihan anda: "))
	while menuSelect < 1 or menuSelect > 3:
	        print("The selection provided is invalid.")
	        menuSelect = int(input("\nPlease select one of the five options "))

	if menuSelect == 1:
	    menu1(s)
	elif menuSelect == 2:
		menu2(s)
	elif menuSelect == 3:
		menu3(s, user, pw)
	

	input("Press enter to exit ;)")

main()
'''
buat tampilan untuk daftar film yang sedang tayang, 
pemesanan tiket bioskop, 
melihat harga tiket,
dan melihat sisa tiket yang tersedia, 
serta mengubah daftar film dan harga tiket yang sedang tayang.
'''