import random

s1 = set()
s2 = set()
for _ in range(0, 10) :
    s1.add(random.randint(0, 100))
    s2.add(random.randint(0, 100))

for i in s1: print(i, end=" ")
print("\n")
for i in s2: print(i, end=" ")
print("\n")

is_found = False

for i in s1:
    for j in s2:
        if i == j:
            is_found = True
print(is_found)