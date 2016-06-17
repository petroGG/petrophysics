'''
List of functions:
- pwave_modulus
- shear_modulus
- bulk_modulus - (K) 
- lame1st - Lame 1st coefficient lambda
- shear_modulus - (G) 
- young_modulus - (E) 
- poisson - ratio (mu)
'''

def pwave_modulus(den, vp):
    '''
    den - kg/m3
    vp - m/s
    Returns:
    m - GPa (equation adds division by 10^9 and the final result is in GPa)
    '''
    m = (den*vp**2)/10**9
    return m

def shear_modulus(den, vs):
    '''
    den - kg/m3
    vp - m/s
    Returns:
    m - GPa (equation adds division by 10^9 and the final result is in GPa)
    '''
    g = (den*vs**2)/10**9
    return g

def bulk_modulus(den,vp,vs):
    '''
    den - kg/m3
    vp - m/s
    vs - m/s
    Returns:
    k - GPa (equation adds division by 10^9 and the final result is in GPa)
    '''
    k = (den*vp**2-(4/3)*vs**2)/10**9
    return k

def lame1st(den, vp, vs):
    '''
    den - kg/m3
    vp - m/s
    vs - m/s
    Returns:
    lame1st - GPa (equation adds division by 10^9 and the final result is in GPa)
    '''
    lame1st = (den *(vp**2 - 2*vs**2))/10**9
    return lame1st

def young_modulus(den, vp, vs):
    '''
    den - kg/m3
    vp - m/s
    vs - m/s
    Returns:
    e - GPa (equation added division by 10^9 and the final result is in GPa)
    '''
    e = ((den*vs**2*(3*vp**2-4*vs**2))/(vp**2-vs**2))/10**9
    return e

def poisson(den, vp, vs):
    '''
    den - kg/m3
    vp - m/s
    vs - m/s
    Returns:
    mu - GPa (equation adds division by 10^9 and the final result is in GPa)
    '''
    mu = ((den*vs**2*(3*vp**2-4*vs**2))/(vp**2-vs**2))/10**9
    return mu
