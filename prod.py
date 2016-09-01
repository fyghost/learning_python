def prod(s):
    if not isinstance(s, list):
        return -1

    return reduce(lambda x,y: x*y, s)
    
