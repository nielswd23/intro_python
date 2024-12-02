## reading and writing csv files -- base python
with open("example.csv", 'w') as file: 
    file.write("Toby,Tagalog,New Orleans\n")
    file.write("Jan,Spanish,Nanning\n")
    file.write("Kevin,Chinese,Ottawa\n")

data = []
with open("example.csv", 'r') as file: 
    for line in file:
        data.append(line.rstrip().split(","))