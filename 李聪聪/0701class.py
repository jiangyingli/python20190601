class People:
    name=""
    age=0
    height=0.0
    weight=0.0
    sex=""

    def study(self):
        print("好好学习天天向上")

    def eat(self):
        print("世间唯有美食不可辜负")

    def say(self):
        print("我是"+self.name)


People.age=18
People.height=185
people1=People()
people1.name="张三"
print(people1.name)
people1.height=180
print(people1.height)
people1.study()


people2=People()
people2.name="李四"
print(people2.height)
print(People.age)
people2.eat()
people2.say()