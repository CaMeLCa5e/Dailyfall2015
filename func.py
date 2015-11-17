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


m = {'a':1, 'b':2, 'c':3, 'd':4}
for k, v in m.iteritems():
    print '{}: {}'.format(k, v)

a = [1,2,3,4,5,6]    
group_adjacent = lambda a, k: zip(*([iter(a)]*k))
print group_adjacent(a, 2)
print group_adjacent(a, 3)
print group_adjacent(a, 1)

from itertools import islice
group_adjacent = lambda a, k: zip(*(islice(a, i, None, k) for i in range(k)))
group_adjacent(a, 3)
group_adjacent(a, 2)
group_adjacent(a, 1)