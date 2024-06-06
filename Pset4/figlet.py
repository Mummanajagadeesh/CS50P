import pyfiglet
import sys
import random

from pyfiglet import Figlet
figlet=Figlet()

if len(list(sys.argv))==1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
    test=str(input("Input:"))
    print(figlet.renderText(test))

elif len(list(sys.argv))==3 and ((sys.argv[1]=="-f") or (sys.argv[1]=="-font")) and (sys.argv[2] in figlet.getFonts()):
    figlet.setFont(font=sys.argv[2])
    test=str(input("Input:"))
    print(figlet.renderText(test))

else:
    sys.exit("Invalid usage")
