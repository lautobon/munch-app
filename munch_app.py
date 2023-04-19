''' 
Munch App MVP
v0.1
El propósito de esta app es generar un menú a partir de los platos favoritos y generar una lista de compras de ingredientes si así se requiere.
'''
# ----- Importar -----

from random import choice

# ----- A. Funciones -----
# A1. Elegir platos


def chooseDishes(days):
    while len(myMenu) < int(days):
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("Listo! Aquí está tu menú... ")
    print()
    for dish in myMenu:
        print(myMenu.index(dish) + 1, dish)
    print()
    print("De todos estos platos, mi favorito sería ... " + choice(myMenu))


# A2. Construir lista de compras


def buildShoppingList():
    myShoppingList = []
    if "Pizza" in myMenu:
        myShoppingList.append(pizza)
    if "Hamburguesa" in myMenu:
        myShoppingList.append(hamburguesa)
    if "Alitas de pollo" in myMenu:
        myShoppingList.append(alitasDePollo)
    if "Tacos de carne" in myMenu:
        myShoppingList.append(tacosDeCarne)
    if "Sandwich" in myMenu:
        myShoppingList.append(sandwich)
    if "Omelet" in myMenu:
        myShoppingList.append(omelet)
    if "Perro caliente" in myMenu:
        myShoppingList.append(perroCaliente)
    print()

    for dish in (myShoppingList):
        for ingredient in (dish):
            print(dish.index(ingredient) + 1, ingredient)
    print()
    print("Listo! Buen provecho.")


# ----- B. Listas -----

foodWeLike = ["Pizza", "Hamburguesa", "Alitas de pollo", "Tacos de carne", "Sandwich", "Omelet", "Perro caliente"]

pizza = ["Base", "Salsa de tomate", "Queso", "Pepperoni", "Chillis"]
hamburguesa = ["Pan", "Carne", "Queso", "Papas a la francesa", "Tomate", "Maduro"]
alitasDePollo = ["Alitas de pollo", "Salsa miel mostaza", "Picante"]
tacosDeCarne = ["Tortillas", "Maiz", "Carne", "Cebolla", "Piña"]
sandwich = ["Pan tajado", "Jamon serrano", "Queso tajado", "Mantequilla"]
omelet = ["Huevos", "Espinaca", "Tomate", "Queso"]
perroCaliente = ["Pan", "Salchicha", "Papas chips", "Salsa de piña", "Queso", "Huevo codorniz"]

myMenu = []
myShoppingList = []

# 1. Cuantos días planear?

print("Hola, soy Munch y te ayudaré a planear un menú para tu comida.")

answer = input("Cuántos días deseas que planee? ")
print()

print("Perfecto. Voy a planear " + answer + " comida(s) de tu lista de platos favoritos.")

# 2. Elegir platos

chooseDishes(answer)


# 3. Construir lista de compras
answer = input("Te gustaría una lista de compras para este menú? ***Escribe 'y' para confirmar:*** ")


if answer == "y":
    buildShoppingList()

else:
    print()
    print("Ya está. Adiós por ahora. :)")
