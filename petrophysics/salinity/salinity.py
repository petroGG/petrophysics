'''
List of functions:
- nacl - NaCl equivalent from chlorides
- salinity - from Rw and Tf
'''
def nacl(chloride):
    '''
    nacl(chloride)
    *Input parameters:
    - chloride - [ppm]
    *Returns:
    - nacl -  NaCl equivalent calculated with formula: chloride * 1.645
    '''
    nacl = chloride * 1.645
    return nacl

def salinity(rw, tf):
    '''
    salinity(rw, tf)
    *Input parameters:
    - rw - water resistivity [ohm.m]
    - tf - formation temperature [F]
    *Returns:
    - salinity - [ppm Nacl] calculated by Crain formula.
    '''
    salinity = 400000 / tf / (rw**1.14)
    return salinity
