from termcolor import colored
import pyfiglet
# pip install termcolor

sentence = pyfiglet.figlet_format("Hello")
# print(sentence)

# color_hello = colored("Hello", "red")
color_hello = colored(sentence, "red")
print(color_hello)
