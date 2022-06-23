from math import sqrt
#sorry in advance for the bad variables i was converting this from TIBASIC
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
def triForB(a,c):
    if (isInt(a) != True and isInt(c) != True):
        return False
    output = sqrt((c**2)-(a**2))
    return output
def triForC3D(l,w,h):
    if (isInt(l) != True and isInt(w) != True and isInt(h) != True):
        return False
    output = sqrt((sqrt((l**2)+(w**2))**2)+(h**2))
    return output
def vertOfPorab(a, b, c):
    if (isInt(a) != True and isInt(b) != True and isInt(c) != True):
        return False
    xVrt = (-(b))/(2*(a))
    yVrt = (a*(xVrt)**2)+(b*(xVrt))+(c)
    return [xVrt, yVrt]
def pointOnPorab(x, a, b, c):
    if (isInt(a) != True and isInt(b) != True and isInt(c) != True and isInt(x) != True):
        return False
    c = c-x
    topPlus = -(b)+sqrt(b**2 - (4*(a)*(c)))
    botPlus = (2*(a))
    topMins = -(b)-sqrt(b**2 - 4*(a)*(c))
    botMins = (2*(a))
    return [[(topPlus/botPlus), x], [(topMins/botMins), -x]]