# mutantePython

_Este programa de prueba ha sido desarrollada en **Python** para resolver un reto de clasificación de ADN mutante y no mutante =)_


Para usar esta servicio, envía la cadena ADN en formato texto. Ejemplo:
```
["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
```

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋
**Tener una versión de Python instalada > 3.5**

### Instalación 🔧

clona el proyecto en tu entorno virtual de Python

```
git clone https://github.com/amaury84/mutantePython
```

## Ejecutando las pruebas ⚙️

_Una vez clonado el proyecto, puedes ejecutar el script main.py el cual te pedirá por teclado la cadena ADN_

### Iniciando el script main.py para levantar la API de forma local 🔩
```
python main.py
```

_Cuando se envía una cadena de ADN en formato JSON, hay dos métodos que verifican la cadena_

* _El primero, **mutante.isAdn(dna)** devuelve True si la cadena tiene una sintaxis correcta._
 _Cuando devuelve un False, retorna un mensaje para verificar la sintaxis de la cadena ADN_

* _El segundo, **mutante.isMutant(dna)** devuelve True si la cadena pertenece a un mutante._
_Devuelve un False si la cadena no pertenece a un mutante._
```
#código ejemplo del método main.py

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
```

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Amaury Méndez** - *Trabajo Inicial* - [amaury84](https://github.com/amaury84)
