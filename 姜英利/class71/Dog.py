
class Dog:   #  class定义类，一类事物的抽象，模板（将来产生对象都依据模板）
    #变量：属性
    name=""
    age=0
    color=""
    height=0.0
    sex=""
    #函数：功能
    def eat(self):
        print("狗能吃东西")
    def drink(self):
        print("狗能喝水")
    def say(self):
        print("我是"+self.name)
# 类直接调用属性
Dog.name = "狗狗" #所有对象共享的
dog = Dog()#1狗（对象）
dog.name="小狗"
dog.age = 5
dog.sex="公"
dog.eat()
dog.say()
print(dog.name)

dog1 = Dog()#2狗（对象）
dog1.name = "大狗"
dog1.age=10
dog1.sex="母"
dog1.eat()
dog1.say()
print(dog1.name)

print(Dog.name)


# 类-》N对象（相互独立，互不影响）
# 之前，