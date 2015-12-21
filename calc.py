# loop  = 1 
# choice = 0 

# while loop == 1: 
#     print "welcome to calculator"
#     print "  "
#     print "1, addition"
#     print "2, subtraction"
#     print "3, multiplication"
#     print "4, division"
#     print "5, quit"
#     print "  "

#     choice = input("choose your option")
#     if choice == 1: 
#         add1 = input("add this:")
#         add2 = input("to this:")
#         print add1, "+", add2, =, add1 + add2
#         

def menu():
    print "  "
    print "1, addition"
    print "2, subtraction"
    print "3, multiplication"
    print "4, division"
    print "5, quit"
    print "  "
    return input("choose an option: ")

def add(a,b):
    print a + b

def sub(a,b):
    print a - b

def mul(a,b):
    print a * b    

def div(a,b):
    print a / b
    
