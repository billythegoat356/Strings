from sys import argv
from os.path import isfile


characters = [
    ' ', ',', '.', ';', ':', '?', '!', '/', '"', "'", '(',
    ')', '[', ']', '{', '}', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', 
    '3', '4', '5', '6', '7', '8', '9'
    ]


if len(argv) < 2:
    print("Not enough arguments-")
    exit()

if len(argv) > 2:
    print("Too much arguments-")
    exit()


if not isfile(argv[1]):
    print("Not a file-")
    exit()

with open(argv[1], 'r', encoding="cp437") as f:
    content = (f.read()).splitlines()

for line in content:
    show = False
    for char in line:
        if char in characters:
            print(char, end='')
            show = True
    if not show:
        print()


