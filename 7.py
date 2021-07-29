import random

s1 = set()
s2 = set()
for _ in range(0, 10):
    s1.add(random.randint(0, 15))
    s2.add(random.randint(0, 15))

for i in s1: print(i, end=" ")
print("\n")
for i in s2: print(i, end=" ")
print("\n")

s1= s1-s2

print(s1)