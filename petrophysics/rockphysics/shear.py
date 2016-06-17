'''
List of functions:
- castagna - convert vp to vs with Castagna eq.
'''

def castagna(vp,a=1.16,b=1.36):
    '''
    Castagna with default value
    vp - m/s
    Returns:
    vs - m/s
    '''
    vs = vp/a  - b *1000/ a
    return vs



