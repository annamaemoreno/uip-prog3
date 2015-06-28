import os

lista_super=[]
opcion=1
while opcion!='4':
	print('1-agregar\n2-eliminar\n3-ver\n4-salir')
	opcion=input()
	if opcion=='1':
		agr=input()
		lista_super.append(agr)
	elif opcion=='2':
		eli=input()
		try:
			lista_super.remove(str(eli))
		except ValueError:
			print('no esta en la lista')
	elif opcion=='3':
		print(lista_super)
		e=input()
	os.system('CLS')