'''
class cat:
    color = ""
    weight = 0
    owner = ""
    age = 0

    def funoverwight(self):
        weight = int(input("它的体重"))
        if weight > 10:
            print(self.owner,"的猫太沉了")




cat1 = cat()
cat1.owner = "王鸿儒"
cat1.funoverwight()
'''
list = [43, 34, 666, 744, 12, 2, 1, 45, 97, 54]
for j in range(len(list)-1):
    for i in range(len(list)-1-j):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]

print(list)


