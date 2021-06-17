import mutante

def main():
    #dna1=["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
    print("**Magneto**  ingresa la cadena de ADN  **Magneto**")
    
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
