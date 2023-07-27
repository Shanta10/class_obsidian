PYTHON BASICO

Python es un lenguaje de programación ampliamente utilizado y apreciado por su legibilidad y facilidad de uso. Su sintaxis clara y estructurada permite a los desarrolladores escribir código de manera más sencilla y rápida. A continuación, se presentan algunas diferencias adicionales entre Python y JavaScript:

1. Sintaxis y Bloques de Código: Una de las diferencias notables entre Python y JavaScript es la forma en que se definen los bloques de código y las funciones. En Python, los bloques de código se delimitan mediante la indentación, lo que proporciona una estructura clara y fácil de seguir. Por otro lado, JavaScript utiliza llaves ({}) para delimitar bloques de código. Además, las funciones en Python no requieren llaves, simplemente se definen mediante la palabra clave "def" seguida del nombre de la función.


2. Tipado y Asignación de Variables: Python es un lenguaje de tipado dinámico, lo que significa que las variables pueden cambiar de tipo durante la ejecución del programa. En contraste, JavaScript es un lenguaje de tipado débil y dinámico, lo que permite conversiones automáticas de tipos de datos. Además, en Python, no es necesario declarar explícitamente el tipo de una variable, ya que se infiere automáticamente a partir del valor asignado. En JavaScript, las variables se declaran utilizando palabras clave como "var", "let" o "const", y el tipo puede cambiar durante el ciclo de vida de la variable.

  
3. Curva de Aprendizaje y Preferencia de Científicos: Los científicos y analistas de datos suelen preferir Python debido a su amplio conjunto de librerías y herramientas para la ciencia de datos, el aprendizaje automático y el análisis de datos. Python ofrece una curva de aprendizaje más suave, lo que significa que es más accesible para aquellos que no son programadores de formación, pero que desean utilizar la programación como una herramienta en sus áreas de especialización.


En resumen, aunque Python y JavaScript son lenguajes populares y versátiles, tienen diferencias significativas en cuanto a su sintaxis, tipado y aplicación. La elección entre ambos dependerá del tipo de proyecto o aplicación que se esté desarrollando, así como de las preferencias y habilidades del equipo de desarrollo. Ambos lenguajes tienen su lugar en el mundo de la programación y ofrecen ventajas únicas según el contexto en el que se utilicen.


EJERCICIOS EN CLASE:

```def multiply_by_two(x):

  """This function multiplies 

      an input number by 2 """

  return x * 2

help(multiply_by_two)

  

  

def apply_func_twice(func, arg):

  """This function applies 'func' twice to 'arg' """

  return func(func(arg))

def add_five(x):

  return x + 5

print (apply_func_twice(add_five, 10))

  

  

EJERCICIO SIGNOS ZODIACALES

  

import random

  

starSign = [

    "Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo",

    "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis"

]

prob = ['Te irá bien en el dinero', 'Te irá bien en el amor', 'Tendrás problemas en tu salud', 'Evita lugares desconocidos']

probselect = random.choice(prob)

  

inpSign = input("Ingresa un signo del zodíaco: ")

  

if inpSign in starSign:

    print(inpSign,': ', probselect)

else:

    print("El signo", inpSign, "no es válido")

  

  

  

//Eleva a la potencia 2 solo los números pares

even_squares = [i**2 for i in range (10) if i % 2 == 0]

print(even_squares)

  

  

//120

num = 5

factorial = 1

while num > 0:

  factorial *= num

  num -=1

print(factorial)

  

  

// minúsculas, MAYUSCULAS, Separado

s = "Hello, Mars!"

print(s.lower())

print(s.upper())

print(s.split(", "))

  

  

//imprime las iniciales de todos los planetas

planets = [

    'Mercury', 'Venus', 'Earth',

    'Mars', 'Jupiter', 'Saturn',

    'Uranus', 'Neptune'

]

planet_initials = {

    planet: planet[0]

    for planet in planets

}

print(planet_initials)



```


EJERCICIO LOTERIA
```import random

  

animals = ["perro", "gato", "ratón"]

  

def ticket_gen():

num_gen = set() #set es para garantizar que los numeros seran diferentes

while len(num_gen) < 4:

rand_num = random.randint(1, 5)

num_gen.add(rand_num) # Lo agregamos al conjunto

return num_gen

  

lottery_number = ticket_gen()

user_number = ticket_gen()

  

animal_select = random.choice(animals)

animal_user = random.choice(animals)

  

def winner():

  

print("EL BOLETO GANADOR ES:", lottery_number, animal_select)

print("TU BOLETO CONTIENE:", user_number, animal_user)

  

if lottery_number == user_number and animal_select == animal_user:

print("¡GANASTE!")

else:

print("PERDISTE")

if animal_select == animal_user:

print("REPITE")

winner()

winner()
```