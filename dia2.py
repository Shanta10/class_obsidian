import random

animals = ["perro", "gato", "ratón"]

def ticket_gen():
    num_gen = set() #set es para garantizar que los numeros seran diferentes
    while len(num_gen) < 4:
        rand_num = random.randint(1, 5)
        num_gen.add(rand_num)  # Lo agregamos al conjunto
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

