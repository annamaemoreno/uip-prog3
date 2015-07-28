import socket

dip = input("DIRECCION IP: ")
inicio = int(input("ESCRIBA EL PUERTO INICIAL:"))
final= int(input("ESCRIBA EL PUERTO FINAL:"))

conexion = socket.socket()
for i in range(beginnig,final+1):
	try:
		conexion.connect( (sip, i) )
		print ("Port : %s open." % i)
	except:
			print ("Port : %s Close." % i)
conexion.close()