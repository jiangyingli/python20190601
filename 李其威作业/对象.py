class dog():
    name=""
    age=""
    def eat(self):
         print("吃一碗")

dog.age=100
dog1=dog()
dog1.name="zhangjiayuan"
print(dog1.name)
dog1.eat()



dog2=dog()
dog2.age=0
print(dog2.age)