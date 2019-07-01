'''
print(r"我是一\"个老师")

#bool两个值的类型

#True / False


print(10+5)

print(10-5)


print(10*5)

print(10/5)

print(35/10)

a = 10

b = 20
print(a+b)

#print(0.1+0.05)
#浮点运算导致的


print(100 % 6)

print(3**2)

print(100//6)



a = 1#一个等号赋值

b = 2
#两个等号是比较，结果为True或False

print( 
a == b )

a = 3
a = a + 5
print(a)




a += 5
print(a)
'''
'''
#列表

list = [1,2,3,4,5,6,7,8]

print( list[0] )

list.append(100)#向末尾追加

del list[6]

list[4] = 55


print(list)


print( list[3:5] )


list1 = [11,22]

print(list + list1)#拼接

#in/not in运算是判断是否包含某元素


print(100 in list)


print(len(list))#list的长度
print(max(list))#list里最大的值
print(min(list))#求list里最小的值

a = list.count(100)

list.extend([111,112])
#向list拓展若干元素


print( list  )


print( list.index(111) )

list.insert(3,999)#插入元素

print(list)

print(
list.pop())#删除最后一个元素


print(list)


list.remove(100)

print(list)


list.sort()
print(list)


#
list3 = list#复制地址

list3 = list.copy()#复制一份，产生新的

list[1]=0

print(list)
print(list3)


 = (1,2,3,4,5)
print(list)


list[0] = 100
'''
'''
#       关键字   值

map = { "张三":"90","李四":"93","王五":"100" }


print( map["李四"] )


map1 = {"一班":["张三","李四","王五"],"二班":["black","red","green"]}


print(map1["一班"][0])

#二维结构以后说

'''


#if
'''两种情况
age = 23

if age > 30 :#if后如果为真（成立），则执行后续冒号后的内容，否则不执行
    #if控制的这个语句，必须缩进（tab）
    #如果if管3行，则3行必须对齐
    print("而立")
    print("掉头发")
    print("正式升级为大叔")
else :
    print("你还年轻")
    print("你还年轻")
    print("你还年轻")

'''
'''
#N种情况

score = 50

if score >= 90 :
    print("买个手机")
elif score >= 80 :
  print("买个手机卡")
elif score >= 70 :
    print("买个手机壳")
elif score >= 60 :
    print("买个手机膜")
else :
    print("家法伺候")

'''
#循环
#只要括号里为真，永远的执行下去，直到括号里为假
'''
max = 10000
age = 1
while( age <= max  ):
    print("我又长了一岁",age)
    age = age +1
'''

#题目:1-100里所有能被7整除的数有哪些,他们的和是多少
max = 100
a = 1
sum = 0
while(a <= max ):
    if(a % 7 == 0 ):
        sum = sum + a
    a = a + 1
print(sum)


#作业1：输入一个数a，表示分钟，求这是几小时，几分钟
#作业2：求100以内奇数
#作业3：将1-10存入一个列表中，已知列表中初始值全是0，长度是10
#作业4：已知一个列表中全都是1，将前一半值变成2
#作业5（BOSS）：已知a，b两个数，求a，b的所有公因子





