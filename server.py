from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading

# Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(("127.0.0.1", 8080),
                    requestHandler=RequestHandler,
                    allow_none=True) as server:
	server.register_introspection_functions()

	filmtayang = {
	}
	film1 = {
  	'Judul' : 'Parasite',
	'Harga' : 'Rp. 40.000',
	'Sisa' : 30,
	'Studio' : 1,
	'Jam' : '12:30'
	}

	film2 = {
	'Judul' : 'Avengers: End Game',
  	'Harga' : 'Rp. 40.000',
  	'Sisa' : 34,
  	'Studio' : 2,
  	'Jam' : '14:30'
 	}

	film3 = {
  	'Judul' : 'Weathering with You',
  	'Harga' : 'Rp. 40.000',
  	'Sisa' : 25,
  	'Studio' : 1,
  	'Jam' : '14:00'
 	}

	film4 = {
  	'Judul' : 'Code Geass: Fukatsu no Lelouch',
  	'Harga' : 'Rp. 40.000',
  	'Sisa' : 22,
  	'Studio' : 2,
  	'Jam' : '13:30'
 	}

	film5 = {
  	'Judul' : 'Parasite',
  	'Harga' : 'Rp. 40.000',
  	'Sisa' : 8,
  	'Studio' : 1,
  	'Jam' : '19:00'
 	}

	film6 = {
  	'Judul' : 'Parasite',
  	'Harga' : 'Rp. 40.000',
  	'Sisa' : 5,
  	'Studio' : 2,
  	'Jam' : '20:30'
 	}


	lock = threading.Lock()


	def showfilm1():
		lock.acquire()
		lock.release()
		return film1
	server.register_function(showfilm1, 'show1')

	def showfilm2():
		lock.acquire()
		lock.release()
		return film2
	server.register_function(showfilm2, 'show2')

	def showfilm3():
		lock.acquire()
		lock.release()
		return film3
	server.register_function(showfilm3, 'show3')

	def showfilm4():
		lock.acquire()
		lock.release()
		return film4
	server.register_function(showfilm4, 'show4')

	def showfilm5():
		lock.acquire()
		lock.release()
		return film5
	server.register_function(showfilm5, 'show5')

	def showfilm6():
		lock.acquire()
		lock.release()
		return film6
	server.register_function(showfilm6, 'show6')

	def pesanfilm1(tiket):
		film1["Sisa"] = film1["Sisa"]-tiket
	server.register_function(pesanfilm1, 'pesan1')

	def pesanfilm2(tiket):
		film2["Sisa"] = film2["Sisa"]-tiket
	server.register_function(pesanfilm2, 'pesan2')

	def pesanfilm3(tiket):
		film3["Sisa"] = film3["Sisa"]-tiket
	server.register_function(pesanfilm3, 'pesan3')

	def pesanfilm4(tiket):
		film4["Sisa"] = film4["Sisa"]-tiket
	server.register_function(pesanfilm4, 'pesan4')

	def pesanfilm5(tiket):
		film1["Sisa"] = film5["Sisa"]-tiket
	server.register_function(pesanfilm5, 'pesan5')

	def pesanfilm6(tiket):
		film6["Sisa"] = film6["Sisa"]-tiket
	server.register_function(pesanfilm6, 'pesan6')

	def editfilm1(judul, tiket):
		film1["Judul"] = judul
		film1['Sisa'] = tiket
	server.register_function(editfilm1, 'edit1')

	def editfilm2(judul, tiket):
		film2["Judul"] = judul
		film2['Sisa'] = tiket
	server.register_function(editfilm2, 'edit2')

	def editfilm3(judul, tiket):
		film3["Judul"] = judul
		film3['Sisa'] = tiket
	server.register_function(editfilm3, 'edit3')

	def editfilm4(judul, tiket):
		film4["Judul"] = judul
		film4['Sisa'] = tiket
	server.register_function(editfilm4, 'edit4')

	def editfilm5(judul, tiket):
		film5["Judul"] = judul
		film5['Sisa'] = tiket
	server.register_function(editfilm5, 'edit5')

	def editfilm6(judul, tiket):
		film6["Judul"] = judul
		film6['Sisa'] = tiket
	server.register_function(editfilm6, 'edit6')

	print("Server Database Running!")
	server.serve_forever()