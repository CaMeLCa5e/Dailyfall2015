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
