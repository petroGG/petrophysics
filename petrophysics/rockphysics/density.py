'''
List of functions:
- gardner - convert vp to vs with Castagna eq.
- bellotti_consolidated
- bellotti_unconsolidated
- lindseth
'''

def gardner(vp,a=0.23,b=0.25):
    '''
    (vp,a=0.23,b=0.25)
    *Input parameters:
     - vp - ft/s (use a=0.31, b=0.25 for metric)
    *Returns:
     - den - g/cc
    '''
    den = a * vp**b
    return den

def bellotti_consolidated(dt):
    '''
    *Input parameters:
     - dt - travel time - us/ft
    *Returns:
     - den - g/cc
     '''
    den = 3.28 - dt / 89
    return den

def bellotti_unconsolidated(dt):
    '''
    *Input parameters:
     - dt - travel time - us/ft
    *Returns:
     - den - g/cc
     '''
    den = 2.75 - 2.11 * (dt - 47)/(dt+200)
    return den

def lindseth(vp):
    '''
    *Input parameters:
     - vp - ft/s
    *Returns:
     - den - g/cc
     '''
    den = (vp - 3460)/(0.308 * vp)
    return den
