total_evens = 0

for i in range(5):
    if i % 2 == 0:
        total_evens += 1

for b in range(10):
    if b % 2 == 0:
        total_evens += 1

for c in range(2, 9, 3):
    if c % 2 == 0:
        total_evens += 1

for d in range(-4, 6, 2):
    if d % 2 == 0:
        total_evens += 1

for e in range(5, 6):
    if e % 2 == 0:
        total_evens += 1

print(total_evens)
