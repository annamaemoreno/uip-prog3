palabra = ['p', 'e', 'r', 's', 'o', 'n','a'] #palabra de nuestro ahorcado
cuerpo=['palo', 'palo arriba', 'palo abajo', 'cabeza', 'cuerpo', 'pierdas', 'manos']#partes ahorcado
ahorcado=[]
tam = len(palabra) # tamaño de la palabra 

validacion = 0 #CONTADORES
x  = 0 
a = 0 
linea= "" #VARIABLES    
let = ""

print ("\n\t\t--AHORCADO VERSION UIP--\n")

print(" LA PALABRA CONTIENE ",tam,"LETRAS...\n") 
while x < tam:
    ahorcado.append("_") 
    x = x+1
print(ahorcado) # palabra de arhorcado modelo oculto en _ _ _ 

x=0
temp =""
while x !=7: # controlador de los intentos
    
    let = input("\n Veamos tu suerte, inserta tu primera letra: ")
    
    if let  in palabra:   # busqueda de la letra correcta o si esta en la palabra asignada           

        posicion =palabra.index(let)  # asignacion de la letra encontrada      
        ahorcado[posicion]=let+" " # asignacion y almacenamito de la letra
        print("\n\t<-UH! vaya parece que le atinaste,nada mal para ser tu primera vez-> \n",ahorcado)
        
        if temp != let: # verificado para que no cuente si se repite la misma letra
            temp = let
            validacion += 1 # contador para la victoria  
    else:
        x += 1 # contador de los intentos realizados
        if x <7: # condicion de contrucion del AHORCADO
            print("\n\t<-:( ",cuerpo[x-1]," ):->" ,"Que haces? Esa letra no esta aqui sabes que vuelve a intertarlo JA! novato: ",str(7-x)," X_X ")
        else:
           print("\n\tAHORCADO\n PALABRA  ERA: ",palabra) 
    if validacion== tam: # bandera de verificacion de ganador del AHORCADO
        print("\n\t!!!HAS GANADO FELICIDADES JAJAJAJA, ya pero encerio entre tu y yo,se que revisaste la logica para ver cual era la palabra jajajaja que novato!!!\n")
        break; # salir al final despues de aver ganado ya 
else:
    print("\n\t--Se Acabo, vaya suerte la tuya pero desde que tocaste el teclado ya me habia imaginado este final jajajajaja--")
    
