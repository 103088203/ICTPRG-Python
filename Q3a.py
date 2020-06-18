infile = open("names.txt", "r")
file_contents = infile.read()
names = str(file_contents).split('\n')
names_formatted = []
for name in names:
    x = name.split()
# i is the index and y is the value, enumerate checks both index and value    
    for i, y in enumerate(x):
        x[i] = y[0].upper() + y[1:].lower()
    names_formatted.append(x[0] + ' ' + x[1])
infile.close()

with open("name-formated.txt", "a") as file_object:
    for name in names_formatted:
        file_object.write(name + "\n")

print("Following is the list of names")
infile = open("name-formated.txt", "r")
file_contents = infile.read()
print(file_contents)
infile.close()