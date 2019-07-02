# 面向对象

# 1、所有语言都朝面向对象方向发展

    # 庞大复杂 ， 可拓展性，可维护性
#封装一种方式，显卡，


# from 姜英利.class71.Dog import Dog

#由类产生的具体的对象，该对象可以调用类中的属性和函数
# dog = Dog()
# dog.age = 5
# print(dog.age)

# 排序

# list = [4,7,9,2,11,89,50]
# list.sort( reverse=True )
# print(list)

#手动排序
# 冒泡排序法

# 不满足要求的交换位置
# 小-大
# j = list[i]
# list[i]=list[i+1]
# list[i+1]=j

list = [4,50,7,11,89,9,2]
# 效率的提升，重要的，运行效率提升50%，量的积累，12306网站，
for j in range(len(list)-1):
    for i in range(len(list)-1-j):
        if( list[i] > list[i+1]):
            list[i], list[i+1] = list[i+1], list[i]

    print(list)
for i in range(len(list)):
    print(list[i],end=' ')

# 冒泡
#我再发一个排序算法，2同学
# 从名单中随机选2人的算法
# 不选姓王和张的，可设置的
# 一个人被选过，下一次随机的时候不选，3次之后失效

