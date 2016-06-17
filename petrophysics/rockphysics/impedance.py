'''
List of functions:
- acoustic - impedance vp*den
- shear - impedance vs*den
'''

def acoustic(vp, den):
    pwave_impedance = vp * den
    return pwave_impedance

def shear(vs, den):
    shear_impedance = vs * den
    return shear_impedance

