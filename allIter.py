import sys


def all(iterable):
    for element in iterable: 
        if not element: 
            return False 
    return True 

def any(iterable):
    for element in iterable: 
        if element:
            return True
    return False     

print bin(887)

print bool([True])

v = 7

# print __call__(v)
# does not have a call method

print "___"
if v == callable(v):
    print True

print "___"

# i = 9

print chr(97)
print chr(1)
print chr(2)
print chr(3)
print chr(4)


# class C(object):
#     @classmethod
#     def f(cls):
#         print 'hello'
# C(f)        


getframe_expr = 'sys._getframe({}).f_code.co_name'

def foo():
    print 'I am foo calling bar'
    bar()

def bar():
    print 'I am bar calling baz'
    baz()

def baz():
    print 'baz'
    caller = eval(getframe_expr.format(2))
    callers_caller = eval(getframe_expr.format(3))
    print 'I was called from', caller
    print caller, 'was called from', callers_caller

foo()    

print cmp(6, 4)
print cmp(4, 5)


