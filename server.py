from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading

# Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(("127.0.0.1", 8080),
                    requestHandler=RequestHandler) as server:
	server.register_introspection_functions()

	filmtayang = {
		"film1" : {
	  	'Judul' : 'Parasite',
		'Harga' : 'Rp. 40.000',
		'Sisa' : 10,
		'Studio' : 1,
		'Jam' : '12:30'
		},

		"film2" : {
		'Judul' : 'Avengers: End Game',
	  	'Harga' : 'Rp. 40.000',
	  	'Sisa' : 34,
	  	'Studio' : 2,
	  	'Jam' : '14:30'
	 	},

	 	"film3" : {
	  	'Judul' : 'Weathering with You',
	  	'Harga' : 'Rp. 40.000',
	  	'Sisa' : 25,
	  	'Studio' : 1,
	  	'Jam' : '14:00'
	 	},

	 	"film4" : {
	  	'Judul' : 'Code Geass: Fukatsu no Lelouch',
	  	'Harga' : 'Rp. 40.000',
	  	'Sisa' : 22,
	  	'Studio' : 2,
	  	'Jam' : '13:30'
	 	},

	 	"film5" : {
	  	'Judul' : 'Parasite',
	  	'Harga' : 'Rp. 40.000',
	  	'Sisa' : 8,
	  	'Studio' : 1,
	  	'Jam' : '19:00'
	 	},

	 	"film6" : {
	  	'Judul' : 'Parasite',
	  	'Harga' : 'Rp. 40.000',
	  	'Sisa' : 5,
	  	'Studio' : 2,
	  	'Jam' : '20:30'
	 	}
	}

	lock = threading.Lock()

	def tampilfilm():
		temp = []
		lock.acquire()
		for x,y in filmtayang.items():
			print("========================")
			print("Judul Film: ", y["Judul"])
			print("Harga Tiket: ", y["Harga"])
			print("Sisa Tiket", y["Sisa"])
			print("Studio", y["Studio"])
			print("Jam Tayang", y["Jam"])
			print("========================")

			temp.append(y)
		lock.release()
		return y
	server.register_function(tampilfilm, 'show')

	print ("Server Bioskop berjalan...")
	#Run the server's main loop
	server.serve_forever()