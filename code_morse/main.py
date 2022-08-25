
from os.path import join, dirname
import time
from playsound import playsound

translate_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                  'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',  'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                  'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
                  '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                  '8': '---..', '9': '----.', '0': '-----', ' ': '/'}

message = 'This is just a message'

morse_message = " ".join(translate_dict[c] for c in message.upper())


def play_morse_code(message):
    folder = dirname(__file__)
    short = join(folder, 'short.mp3')
    long = join(folder, 'long.mp3')

    for c in message:
        if c == '.':
            playsound(short)
            time.sleep(0.2)
        elif c == '-':
            playsound(long)
            time.sleep(0.2)
        elif c == '/' or c == ' ':
            time.sleep(0.3)
        else:
            print('Invalid character detected!')


print(morse_message)
play_morse_code(morse_message)

reverse_dict = {value: key for key, value in translate_dict.items()}
reverse_message = " ".join(reverse_dict[c] for c in morse_message.split(" "))
print(reverse_message)
