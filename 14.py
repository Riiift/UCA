EJ1
print("******************************")
print("*     pppppppppppppppp       *")
print("*   pp                PP     *")
print("*  pp    ---   ---     PP    *")
print("* pp     O      o       PP   *")
print("*pp                     PP   *")
print("* pp         <          pp   *")
print("* pp     ---------     pp    *")
print("*   pp                pp     *") 
print("*      pp pp pp pp pp        *") 
print("******************************")
#-----------------------------------------------------------------------------------------------------

EJ2
nombre = input("Ingrese su nombre")
print("mi nombre es:", nombre)
print("Hola", nombre)

#-----------------------------------------------------------------------------------------------------

EJ3
lado1 = int(input("ingrese el lado 1:"))
lado2 = int(input("ingrese el lado 2:")) 
print("Area", lado1 * lado2 )
print("Perimetro", 2*lado1 + 2*lado2 )

#-----------------------------------------------------------------------------------------------------

EJ4
x = input("Ingrese su numero:")
parte_entera = int(float(x))
parte_decimal = (float(x)) - (int(float (x)))
print ("Parte entera", parte_entera)
print ("Parte fraccionaria", parte_decimal)

#-----------------------------------------------------------------------------------------------------

EJ5
num = int(input ("ingrese numero natural de 5 digitos:"))

a = (num //10000)%10
b = (num //1000)%10
c = (num //100)%10
d = (num //10)%10
e = (num) %10
#......................
a2=a**2
b2=b**2
c2=c**2
d2=d**2
e2=e**2

print("El resultuado es:",a2,"-",b2,"-",c2,"-",d2,"-",e2,) 

#-----------------------------------------------------------------------------------------------------

EJ6
x = float(input("Ingrese base:"))     
y = float(input("Ingrese altura:"))

import math

Hipotenusa = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
Area = x*y/2 
Perimetro = (x+y+Hipotenusa)
                                
print("Calculos para un triangulo rectangulo de base",x,"y de altura",y,":\n")
print("<<< Area={:.2f}>>>  <<< Perimetro:{:.2f}>>>".format(Area,Perimetro))

#-----------------------------------------------------------------------------------------------------

EJ7

num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero:"))

num1a= num1 % 10
num2a= (num2//10)%10


print("\n","El numero resultante es :", num1a+(num2a*10),)

#-----------------------------------------------------------------------------------------------------

EJ8

num = int(input("Ingrese tiempo en segundos:"))

Dias = int(86400)
Horas = int(3600)
Minutos = int(60)
Segundos = int(1)

Rdias = num//Dias
Rhoras = (num%Dias)//Horas
Rminutos = (num%Horas)//Minutos
Rsegundos = (num%Minutos)//Segundos

print(Rdias,"dias(s)",Rhoras,"Hora(s)",Rminutos,"Minuto(s)",Rsegundos,"segundo(s)")

#-------------------------------------------------------------------------------------------------------

EJ9







