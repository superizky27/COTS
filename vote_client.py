import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://127.0.0.1:8080')

def voting():
	s = xmlrpc.client.ServerProxy('http://127.0.0.1:8080')
	print("Silahkan pilih kandidat:")
	print("(Masukkan angka 1 atau 2 sesuai pilihan anda)")
	print("pilihan anda: ")
	pil = input()

	if (pil == "1"):
		print(s.vote("candidate_1"))
	elif (pil == "2"):
		print(s.vote("candidate_2"))
	else:
		print("Silahkan Masukkan pilihan lain")
		voting()

def show():
	s = xmlrpc.client.ServerProxy('http://127.0.0.1:8080')
	print(s.querry())

voting()
show()

input("Press enter to exit")


#print(s.vote("candidate_2"))

#print(s.querry())

# Print list of available methods
print(s.system.listMethods())