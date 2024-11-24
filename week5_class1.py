### read files ###
# file.read() and file.readlines()
with open("example.txt", 'r') as file:
    content = file.read()

with open("example.txt", 'r') as file:
    lines_list = file.readlines()

# iterating through lines
my_list = []
with open("example.txt", 'r') as file: 
    for line in file: # defaulty iterates by line 
        my_list.append(line.rstrip()) 
        # handy .rstrip() removes whitespaces. Including "\n"

