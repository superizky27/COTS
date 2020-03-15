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

	}

	film1 = {
		'Judul' : 'Judul',
		'Harga' : 'Rp. 35.000',
		'Sisa tiket' : 20,
	}