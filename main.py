import mutante

def main():
    """
    Archivo inicial, recibe por consola una cadena de texto como la siguiente
    ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
    emplea dos funciones:
       isAdn(dna) que verifica la sintaxis de la cadena
       isMutant(dna) que verifica la condicion de mutante
    """
    
    print("**Liga Magneto**  ************************  **Liga Magneto**")
    print("**Liga Magneto**  ingresa la cadena de ADN  **Liga Magneto**")
    print("**Liga Magneto**  ************************  **Liga Magneto**")
    print("**Liga Magneto**                            **Liga Magneto**")
    print("**Liga Magneto**  *********ejemplo********  **Liga Magneto**")
    print("*                                                          *")
    print(' ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]    ')
    
    dna1 = input()
    #limpiamos el string antes de hacerlo lista
    dna1 = dna1.replace("\"","")
    dna1 = dna1.replace("[","")
    dna1 = dna1.replace("]","")
    #hacemos el string una lista
    dna = dna1.split(",")
    
    if mutante.isAdn(dna):
        print(mutante.isMutant(dna))

if __name__=="__main__":
    main()
