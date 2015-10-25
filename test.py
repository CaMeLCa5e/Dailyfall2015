# x = ["5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"]
x = [ e.strip('"') for e in raw_input().split(',')]

# string_input = [c.strip(',').strip("'") for c in raw_input('Enter something: ').split(',')]
# string_input = [c.strip(',').strip('"') for c in raw_input('Please enter values').split()]
 

print x
