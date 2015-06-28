import os
telefono={}
opcion=1
while opcion!='5':
	print('1-imprimir numero y nombre\n2-agregar numero\n3-quitar numero\n4-buscar numero\n5-salir')
	opcion=input()
	if opcion=='1':
		print(telefono)
		e=input()
	elif opcion=='2':
		print('nombre de la persona:')
		nombre=input()
		print('numero de telefono:')
		numero=input()
		telefono[nombre]=numero
		print(nombre+' ha sido agregado')
		e=input()
	elif opcion=='3':
		print('escriba el nombre de la persona')
		eli=input()
		try:
			del telefono[eli]
			print(str(eli)+' fue eliminado')
		except KeyError:
			print('no esta en el diccionario')
		e=input()
	elif opcion=='4':
		print('escriba el nombre de la persona')
		buscar=input()
		try:
			print('el numero de '+buscar+' es '+str(telefono[buscar]))
		except KeyError:
			print(buscar+ 'no esta en el diccionario')
		e=input()
	os.system('CLS')