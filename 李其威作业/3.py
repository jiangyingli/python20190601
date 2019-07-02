li = open("C:/Users/DELL/Desktop/记事本.txt", "r")

line=li.readline()
while(line!=""):
    a=line[0]
    print(a)
    line = li.readline()