import random
rand1=random.randint(1,3)
rand2=random.randint(1,3)
if (rand1!=rand2):


    file = open("C:\\Users\\jkq\\Desktop\\名单.txt", "r")
    str = file.readlines()

    if (str[rand1][0]=="王"):
        print(str[rand1+1])
    elif(str[rand1][0]!="王"):
        print(str[rand1])
    file.close()

    file = open("C:\\Users\\jkq\\Desktop\\名单.txt", "r")
    str = file.readlines()
    file.close()
    if (str[rand2][0]=="王"):
        print(str[rand2+1])
    elif(str[rand2][0]!="王"):
        print(str[rand2])
        # for a in range(len(str)):
        #     list = str[a].split()
        # file.close()
        # file=open("C:\\Users\\jkq\\Desktop\\名单.txt","r")
        # str=file.readlines()
        # print(str)
        # file.close()
        # print(str[rand1],str[rand2])