t = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
a = (input('Enter: '))

print([t[:-1] + (a,) for t in t])