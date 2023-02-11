import time
import random
import termcolor
import pyfiglet
from pynput.keyboard import Key, Controller

keyboard = Controller()

clear

# Crea el texto ASCII con pyfiglet
ascii_text = pyfiglet.figlet_format("Typing simulator")

# Da color al texto ASCII con termcolor
colored_ascii = termcolor.colored(ascii_text, 'red')

# Imprime el texto ASCII
print(colored_ascii)
print("\033[94m" + "BY MASIVERUS" + "\033[0m")

# Pide al usuario que escriba el texto a simular
text = input("Write the text to simulate: ")

print("\033[93m" + "Simulating keyboard in 5 seconds" + "\033[0m")

# Divide el texto en palabras
words = text.split()

# Define las velocidades de escritura
speeds = [0.07, 0.1, 0.15, 0.20]

# Espera 5 segundos antes de ejecutar
time.sleep(5)

# Recorre cada palabra
for i, word in enumerate(words):
    # Genera una velocidad aleatoria
    speed = random.choice(speeds)

    # Escribe la palabra
    for char in word:
        if char in ['.', ',', '!', '?', 'ñ', 'á', 'é', 'í', 'ó', 'ú', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            time.sleep(speed*2.5)
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(speed)

    # Añade un espacio después de cada palabra, excepto si es la última
    if i != len(words) - 1:
        keyboard.press(Key.space)
        keyboard.release(Key.space)
