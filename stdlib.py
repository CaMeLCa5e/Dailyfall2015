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


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print list(enumerate(seasons))

print list(enumerate(seasons, start=1))

# aka... 
def enumerate(sequence, start=0):
    n = start 
    for elem in sequence: 
        yield n, elem 
        n += 1 

print enumerate(9)        
