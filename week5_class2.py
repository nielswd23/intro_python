import csv 
import os

### reading and writing csv files -- base python ###
with open("example.csv", 'w') as file: 
    file.write("Toby,Tagalog,New Orleans\n")
    file.write("Jan,Spanish,Nanning\n")
    file.write("Kevin,Chinese,Ottawa\n")

data = []
with open("example.csv", 'r') as file: 
    for line in file:
        data.append(line.rstrip().split(","))


### csv library ###
## reading csv files 
data1 = []
with open("example.csv", 'r') as file: 
    reader = csv.reader(file)
    for row in reader:
        data1.append(row)

## dictionaries from CSVs
people = []
with open("example.csv", 'r') as file: 
    reader = csv.reader(file)
    for row in reader:
        person = {}
        person["name"], person["lang"], person["city"] = row[0], row[1], row[2]
        people.append(person)

people = []
with open("example.csv") as file:
    reader = csv.DictReader(file, fieldnames=['name', 'lang', 'city'])
    for row in reader:
        people.append(row)

## writing csv files
with open("new_file.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Toby','Tagalog','New Orleans'])
    writer.writerow(['Jan','Spanish','Nanning'])

with open("new_file.csv", 'w') as file:
    writer = csv.DictWriter(file, fieldnames=["name","city"])
    writer.writerow({'name':'Toby', 'city':'New Orleans'})

# alternatively, if you have a list of dictionaries to write to a file
with open("new_file.csv", 'w') as file:
    writer = csv.DictWriter(file, fieldnames=["name","city","lang"])
    writer.writeheader()
    writer.writerows(people)


### OS library ###
## creating another directory 
os.mkdir('folder')

with open("./folder/file1.txt", 'w') as file: 
    file.write("Here is the content for file 1\n")

with open("./folder/file2.txt", 'w') as file: 
    file.write("Here is the content for file 2\n")

with open("./folder/file3.txt", 'w') as file: 
    file.write("Here is the content for file 3\n")

## reading files in another directory
with open("./folder/file2.txt", 'r') as file: 
    content = file.read()

## reading multiple files with os.listdir()
path = "./folder/"
my_list = []
for file_name in os.listdir(path):
    with open(path + file_name, 'r') as file:
        content = file.read()
        my_list.append(content)


### file permissions ###
os.access(path + "file1.txt", os.W_OK)
os.chmod(path + "file1.txt", 0o444)

# # following code should return an error because file permissions were changed
# with open(path + "file1.txt", 'w') as file: 
#     file.write("Corrupted content\n")


# TODO : write the argparse python script. And write out some notes in 
# week5 exercise and week6 exercise based on the notes