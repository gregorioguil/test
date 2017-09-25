#!/usr/bin/python
import json
from pymongo import MongoClient
import socket, threading, sys, select
from bson.json_util import loads

ip = "192.168.1.153"
port = 8888

def main():
	clientdb = MongoClient("192.168.1.153:27017")
	db = clientdb.test_database
	album= db.test_collection
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Aguardado server...")
	s.connect((ip,port))
	print("Conectado")
	while True:
		msg = ""
		while True:
			print("msg\n")

			resp = s.recv(1024).decode()
			#print("sdas"+resp)
			if resp.find("final") != -1:
				break;
			msg= msg + resp
			print("desads")
		print("Recebeu")
		data = loads(msg)
		album.insert_many(data)
		print("inseriu")
if __name__ == '__main__':
	main()
