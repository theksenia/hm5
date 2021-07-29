import random
s = set()

for _ in range(0, 10) : s.add(random.randint(0, 100))
for i in s: print(i, end=" ")
print("\n")

a = int(input("Enter A: "))

is_found = False
for item in s:
    if item == a:
        is_found = True
        break

print(is_found)