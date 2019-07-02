file = open("C:/Users/DELL/Desktop/记事本.txt", "r")
i=0
for line in file:
    line = file.readline()
    new_line = line[:1]
    file_name = 'F:/dic/divided//' +str(new_line) + ".txt"
print("done")
