import time

seconds = int(input("How much time you want to sleep: "))

for i in range(1, seconds + 1):
    print(i)
    time.sleep(1)
