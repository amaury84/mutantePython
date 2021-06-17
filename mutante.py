def isMutant(dna):
    """
    devuelve True si la cadena ADN es mutante
    """
    letrasIguales = 0 
    secuencia = 0
    cadenaMutante = []
    #Búsqueda por filas
    for f in range(len(dna)):   #recorre filas
        for c in range(len(dna)-1): #recorre columnas
            
            if dna[f][c] == dna[f][c+1]:                
                letrasIguales += 1
                cadenaMutante.append(dna[f][c])
                if letrasIguales == 3:                    
                    cadenaMutante.append(dna[f][c+1])
                    secuencia += 1                    
            else:
                letrasIguales = 0
                
    #Búsqueda por columnas                
    for c in range(len(dna)):   #recorre columnas
        for f in range(len(dna)-1): #recorre filas
            
            if dna[f][c] == dna[f+1][c]:                
                letrasIguales += 1
                cadenaMutante.append(dna[f][c])
                if letrasIguales == 3:                    
                    cadenaMutante.append(dna[f+1][c])
                    secuencia += 1                    
            else:
                letrasIguales = 0
                
    #Búsqueda oblicua                 
    for f in range(len(dna)-1):           
            c = f
           # print(dna[f][c],f,c)
            if dna[f][c] == dna[f+1][c+1]:                
                letrasIguales += 1
                cadenaMutante.append(dna[f][c])
                if letrasIguales == 3:                    
                    cadenaMutante.append(dna[f+1][c+1])
                    secuencia += 1                    
            else:
                letrasIguales = 0
                
    #Búsqueda oblicua en spin
    for k in range(6):
        print("__")
        for j in range(k+1):            
            print("mira ",k-j,j)
            
    print(cadenaMutante)
    if secuencia > 1:
        print(secuencia)
        return True
    else:
    	return False

if __name__=="__main__":
    print("solo para debug")
    dna=["ATGCGA",
         "CAGTGC",
         "TTATGT",
         "AGAAGG",
         "CCCCTA",
         "TCACTG"]
    print(isMutant(dna))
