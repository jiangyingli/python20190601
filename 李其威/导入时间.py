import time

localtime = time.localtime()
result = str(localtime[0]) + "-" + str(localtime[1]) + "-" + str(localtime[2])
print(result)