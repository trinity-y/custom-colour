from colored import fg, bg
from os import system
print((fg(input("foreground colour code: "))+bg(input("background colour code: "))) + "\n"*100 + "done!")
system("cls")