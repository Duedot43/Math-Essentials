def isInt(value):
    try:
        int(value)
    except:
        return False
    else:
        return True
def triForC(a,b):
    if (isInt(a) != True and isInt(b) != True):
        return False
    output = a**2+b**2
    return output