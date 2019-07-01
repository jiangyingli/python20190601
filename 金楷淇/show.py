def show():
    file = open("C:\\Users\\jkq\\Desktop\\记账本.txt","r")
    str=file.read()
    print(str)
    file.close()
show()
