#面向对象
#1,所有语言都朝面向对象方向发展
# 优势  程序复杂、可拓展性，可维护性
'''
class Paper:#class定义类，一类事物的抽象

    number = 0
    color = ""
    area = ""

    def write(self):
        print("打印名单")
    def use(self):
        print("垫桌子")
Paper.color = "red"

paper1 = Paper()
paper1.number = 10
paper1.color = "blue"
paper1.write()
print(paper1.color)

paper2 = Paper()
paper2.number = 100
paper2.color = "white"
paper2.use()
print(paper2.number)

print(Paper.color)
'''
list =[9,4,7,2,11,89,50]
list.sort(reverse=True)#排序
print(list)

#手动排序
#冒泡排序法 两两比较 不满足的交换位置
for j in range(len(list)-1):
    for i in range(len(list)-1-j):
        if(list[i]>list[i+1]):
        #j = list[i]
        #list[i]= list[i+1]
        #list[i+1]=j
            list[i],list[i+1]=list[i+1],list[i]
    print(list)
for i in range(len(list)):
    print(list[i],end=" ")