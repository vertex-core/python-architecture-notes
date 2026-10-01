import time

seconds = int(input("How much time you want to sleep: "))

for i in range(seconds, 0, -1):
    seconds = i % 60
    print(f"00:00:{seconds}")
    time.sleep(1)
print("Time is up")
