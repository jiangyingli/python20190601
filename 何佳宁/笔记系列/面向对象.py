class Computer:
    size=""
    color=""
    brand=""
    def search(self):
        print("搜索")
    def store(self):
        print("存储")
    def introduce(self):
        print("My size is"+Computer.size)


computer1=Computer()
computer1.size="large"
computer1.introduce()

computer2=Computer()
computer2.search()







