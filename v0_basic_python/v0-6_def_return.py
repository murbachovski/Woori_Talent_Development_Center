# from pyfiglet import Figlet

# f = Figlet(font='slant')
# print(f.renderText("TEST"))

import pyfiglet
from termcolor import colored

def call(sentence, color):
    a = pyfiglet.figlet_format(sentence)
    b = colored(a, color)
    return b

call("HELLO", "blue")

# return으로 값을 받으시오.
c = call("FINISH", "red")
print(c)