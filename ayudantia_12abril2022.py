# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 23:33:29 2022

@author: flehu
"""

#%% aqui el usuario introduce valores para sumar y se entrega el promedio 
#arreglar errores


number = 1
lista = []
while number != 0:
    number = int(input("introduzca un valor, si desea terminar introduzca 0: "))
    lista.append(number)


suma = 0
for numero in lista:
    suma = suma + numero
promedio = suma/lista
print("el promedio de los numeros que introdujo es: ", promedio)

#%% funcion que imprime solo los numeros pares, cual es el problema?

def print_pares(lista):
    for i in range(len(lista)):
        if i%2==0:
            print(lista(i))

print_pares([1,2,3,4,5])

#%%los numeros perfectos son iguales a la suma de sus divisores
#'HACER UN PROGRAMA QUE ENCUENTRE TODOS LOS NUMEROS PERFECTOS MENORES QUE UN VALOR DADO, LOS IMPRIMA Y LOS CUENTE'




#%% considere la siguiente sucesion de nombres de niño, 

##CLASIFIQUELA POR INICIAL, en un diccionario que para cada letra del abecedario tenga una lista con los nombres que empiezan con esa letra


#considere las recomendaciones: 
#string.split(sep) ##entrega una lista con los substrings de string que se separan por sep
#limpie la lista de espacios indeseados
#escriba las letras en alguna variable para usarlas como referencia

#TAREA PA LA CASA: ordenelas por cantidad de letras
    
nombres = """

Hugo 

Martín 

Lucas 

Mateo 

Leo 

Daniel 

Alejandro 

Pablo 

Manuel

Álvaro 

Adrián 

David 

Mario 

Enzo 

Diego 

Marcos 

Izan

Javier 

Marco 

Álex 

Bruno 

Oliver 

Miguel 

Thiago 

Antonio 

Marc 

Carlos 

Ángel 

Juan 

Gonzalo 

Gael 

Sergio 

Nicolás 

Dylan 

Gabriel 

Jorge 

José 

Adam 

Liam 

Eric 

Samuel 

Darío 

Héctor 

Luca 

Iker 

Amir 

Rodrigo 

Saúl 

Víctor 

Francisco 

Iván 

Jesús 

Jaime 

Aarón 

Rubén 

Ian 

Guillermo 

Erik 

Mohamed 

Julen 

Luis 

Pau 

Unai 

Rafael 

Joel 

Alberto 

Pedro 

Raúl 

Aitor 

Santiago 

Rayan 

Pol 

Nil 

Noah 

Jan 

Asier 

Fernando 

Alonso 

Matías 

Biel 

Andrés 

Axel 

Ismael 

Martí 

Arnau 

Imran 

Luka 

Ignacio 

Aleix 

Alan 

Elías 

Omar 

Isaac 

Youssef 

Jon 

Teo 

Mauro 

Óscar 

Cristian 

Leonardo 

Abel 

Adrián 

Alejandro 

Ángel 

Carlos 

César 

Bruno 

Daniel 

Darío 

David 

Diego 

Emilio 

Fabián 

Felipe 

Gabriel 

Héctor 

Hugo 

Jacobo 

Jaime 

Joaquín 

Juan 

Leonardo 

Leo 

Lucas 

Marcos 

Martín 

Mateo 

Matías 

Miguel 

Nicolás 

Pablo 

Raúl 

Samuel 

Santiago 

Sebastián 

Tomás 

Tristán 

Joan 

Andrés 

Ricardo 

Manuel 

Ezequiel 

Francisco 

Elías 

Blas 

Alfonso 

Ulises 

Gerardo 

Alfredo 

Álvaro 

Amadeo 

Amancio 

Antonio 

Baltasar 

Beltrán 

Benito 

Rufino 

Boris 

Camilo 

Ciro 

Conrado 

Donato 
"""




