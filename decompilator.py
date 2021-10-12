from sys import argv
from os.path import isfile
from string import printable as CHARS


def main():
    if len(argv) != 2:
        print("Invalid arguments.\npython3 " + argv[0] + " binary.exe")
        return 1
    
    if not isfile(argv[1]):
        print("Invalid file path passed.")
        return 1

    with open(argv[1], 'r', encoding="cp437") as stream:
        content = stream.read()
    stream.close()

    output = ""
    for char in content:
        if char in CHARS:
            output += char
    
    with open('.'.join(argv[1].split('.')[0:-1]) + '.out', 'w+') as stream:
        stream.write(output)
    stream.close()
    return 0

if __name__ == "__main__":
    main()
