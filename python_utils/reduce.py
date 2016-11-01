def prod(s):
    if not isinstance(s, list):
        return -1
    def prod_temp(x, y):
        return x * y

    return reduce(prod_temp, s)
    
