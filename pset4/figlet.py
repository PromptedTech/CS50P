from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit('invalid bro')
elif len(sys.argv) == 3 and  sys.argv[1] != '-f' and sys.argv[1] != '--font':
    sys.exit('invalid bro')
elif len(sys.argv) == 3 and sys.argv[2] not in figlet.getFonts():
    sys.exit('invalid bro')
elif len(sys.argv) == 3:
    figlet.setFont(font=sys.argv[2])
elif len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))

txt = input('enter your txt brotha: ')
print(figlet.renderText(txt))

