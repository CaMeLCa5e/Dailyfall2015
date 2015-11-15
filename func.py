a, b, c = 1, 2, 3
print a, b, c

a, b, c = [1, 2, 3]
print a, b, c

a, b, c = (2*i+1 for i in range(3))
print a, b, c

a, (b, c), d = [1, (2, 3), 4]

print a
print b
print c
print d

a, b = 1, 2
a, b = b, a
print a, b

a = ["hello", "world", "!"]
for i, x in enumerate(a):
    print '{}: {}'.format(i, x)

