class whr:
    age=""
    height=""
    weight=""
    name=""
    def eat(self):
        print("贼能吃")
    def sleep(self):
        print("贼能睡")
    def say(self):
        print("我是"+self.name)




whr333=whr()
whr333.weight="200kg"
whr333.name="whr"
print(whr333.weight)
whr333.sleep()
whr333.say()