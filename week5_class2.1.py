from sys import argv

## example script for using argv
f = argv[1]
# assuming our file is the second argument 

with open(f, 'r') as file:
    content = file.read()

def first_word(string):
    l = string.split()
    return l[0]

if __name__ == "__main__":
    print(first_word(content))