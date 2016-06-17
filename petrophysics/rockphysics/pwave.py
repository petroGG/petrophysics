'''
List of functions:
- castagna - convert vs to vp with Castagna eq.
'''

def castagna(vs,a = 1.16, b = 1.36):
    '''
    Castagna with default values
    vs - m/s
    Returns:
    vp - m/s
    '''
    vp = a*vs + b*1000
    return vp

