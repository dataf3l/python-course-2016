
file_handle = open("data.txt", "r")
all_the_bytes = file_handle.read()
lines_of_file = all_the_bytes.split("\n")
dataset = []


for line in lines_of_file:
    items = line.split(" ")
    if line == "":
        continue
    ints = map(toInt,  items)
    dataset.append(ints)

print dataset



