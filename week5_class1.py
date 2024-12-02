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


### writing files ### 
## file.write()
with open("my_file.txt", 'w') as file: # note the change in mode -- 'w'
    file.write("This is my first line")
    file.write("Here is my second line")
# my_file.txt won't look quite right. We have to tell python to skip a line 
# whenever we want to write to separate lines. Add "\n" after first line 

## appending a file 
with open("my_file.txt", 'w') as file: 
    file.write("A new line\n")
# notice the other lines are gone! 'w' overwrites old file content.
# to avoid this use append

with open("my_file.txt", 'a') as file: # 'a' for append mode
    file.write("Appended new line\n")

## x mode
# alternatively, you can also avoid overwriting content with 'x' mode which
# only creates the file to write to if it doesn't already exist
# with open("my_file.txt", 'x') as file: 
#     file.write("Appended new line\n")


## writing lists to files 
my_list = ["Line 1", "Line 2", "Line 3", "Line 4"]
with open("new_file.txt", 'w') as file: 
    for line in my_list: 
        file.write(f"{line}\n")	


## + mode
with open("new_file.txt", 'a+') as file: 
    file.write("Line 5\n")
    file.seek(0)
    updated_list = file.readlines()


