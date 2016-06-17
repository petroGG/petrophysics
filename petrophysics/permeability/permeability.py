__all__ = ['phiperm', 'fperm', 'tixier', 'wyllie_rose', 'timur', 'morris_biggs_oil', 'morris_biggs_gas', 'schlumberger', 'coates_dumanoir', 'coates_deno', 'lucia', 'fractureperm']
import math

'''
List of functions:
- based on crossplotting between core phi and perm:
phiperm - permeability from porosity
fperm - permeability from Formation factor F
- based on log-derived forumla:
tixier()
wyllie_rose()
timur()
morris_biggs_oil()
morris_biggs_gas()
schlumberger() - based on K3 chart
coates_dumanoir()
coates_deno()
lucia()
fractureporo()
'''
def phiperm(phi, c1, c2):
        '''
        phiperm(phi, c1, c2)
        *Input parameters:
        - phi - effective porosity [decimal]
        - c1 - porosity exponent (ussualy between 10 - 500)
        - c2 - permeability constant (ussualy -3 to -2.5) 
        *Returns:
        - k - permeability [mD] calculated by regression eq between core phi vs perm
        '''
        k = 10 ** (c1* phi + c2)
        return k

def fperm(phi, c1, c2, a, m):
        '''
        fperm(phi, c1, c2, a, m)
        *Input parameters:
        - phi - effective porosity [decimal]
        - c1 - permeability constant (ussualy between 4-7 * 10^6)
        - c2 - porosity exponent (ussualy 3.5-4.5) 
        - a - turtosity 
        - m - cementation exponent
        *Returns:
        - k - permeability [mD] calculated as a function of F factor and phi
        '''
        F = a / (phi ** m)
        k = c1 / ( F ** c2)
        return k

def tixier(phi, swirr):
        '''
        tixier(phi, swirr)
        *Input parameters:
        - c1 - permeability constant
        - c2 - porosity exponent
        - c3 - irreducible water saturation exponent
        - phi - porosity
        - swirr - water saturation of a zone at irreducible water saturation
        *Returns:
        - k - permeability (mD) calculated with Tixier formula dated (1949):
        k ** (1/2) = 250 * phi ** 3 / Swirr
        '''
        k = (250 * phi ** 3 / Swirr)**2
        return k

def wyllie_rose(phi, swirr, c1, c2, c3):
        ''' 
        wyllie_rose(phi, swirr, c1, c2, c3)
        *Input parameters:
        - c1 - permeability constant
        - c2 - porosity exponent
        - c3 - irreducible water saturation exponent
        - phi - porosity
        - swirr - water saturation of a zone at irreducible water saturation
        *Returns:
        - k - permeability (mD) based on generalized Wyllie Rose formula dated (1954):
        k = c1 * phi ** c2 / Swirr ** c3
        '''
        k = c1 * phi**c2 / swirr**c3
        return k

def timur(phi, swirr):               
        '''
        timur(phi,swirr)
        *Input parameters:
        - c1 - permeability constant = 8581
        - c2 - porosity exponent = 4.4
        - c3 - irreducible water saturation exponent = 2
        - phi - porosity
        - swirr - water saturation of a zone at irreducible water saturation
        *Returns:
        - k - permeability (mD) calculated with Timur formula dated (1968)
        k = c1 * phi ** c2 / Swirr ** c3
        '''
        c1 = 8581
        c2 = 4.4
        c3 = 2
        k = c1 * phi**c2 / swirr**c3
        return k

def morris_biggs_oil(phi, swirr):               
        '''
        morris_biggs_oil(phi, swirr)
        *Input parameters:
        - c1 - permeability constant = 62500
        - c2 - porosity exponent = 6
        - c3 - irreducible water saturation exponent = 2
        - phi - porosity
        - swirr - water saturation of a zone at irreducible water saturation
        *Returns:
        - k - permeability (mD) uses following coefficients in formula:
        k = c1 * phi ** c2 / Swirr ** c3
        '''
        c1 = 62500
        c2 = 6
        c3 = 2
        k = c1 * phi**c2 / swirr**c3
        return k
        
def morris_biggs_gas(phi, swirr):               
        '''
        morris_biggs_gas(phi, swirr)
        *Input parameters:
        - c1 - permeability constant = 6241
        - c2 - porosity exponent = 6
        - c3 - irreducible water saturation exponent = 2
        - phi - porosity
        - swirr - water saturation of a zone at irreducible water saturation
        *Returns:
        - k - permeability (mD) calculated with Morris Biggs formula for gas reservoirs:
        k = c1 * phi ** c2 / Swirr ** c3
        '''
        c1 = 6241
        c2 = 6
        c3 = 2
        k = c1 * phi**c2 / swirr**c3
        return k

def schlumberger(phi, swirr):               
        '''
        schlumberger(phi, swirr)
        *Input parameters:
        - c1 - permeability constant = 10000
        - c2 - porosity exponent = 4.5
        - c3 - irreducible water saturation exponent = 2
        - phi - porosity
        - swirr - water saturation of a zone at irreducible water saturation
        *Returns:
        - k - permeability (mD) calculated with Morris Biggs formula for oil reservoirs:
        k = c1 * phi ** c2 / Swirr ** c3
        '''
        c1 = 10000
        c2 = 4.5
        c3 = 2
        k = c1 * phi**c2 / swirr**c3
        return k

def coates_dumanoir(rw, rt_irr, phi, den_hc):
        '''
        coates_dumanoir(Rw, Rtirr, den_hc)
        *Input parameters:
        - rw - fm. water res @ fm. temp
        - rt_irr - true resistivity from a formation at irreducible water saturation
        - phi - porosity
        - den_hc - hydrocarbon density in g/cc
        - c - constant based on hydrocarbon density
        - w - constant
        *Returns:
        - k - permeability calculated with Coates-Dumanoir formula dated (1973)
        '''
        c = 23 + 465 * den_hc - 188 * den_hc**2
        w = ((3.75 - phi) + ((math.log(Rw/Rtirr)+2.2)**2)/2)**(1/2)
        k = ((c * phi **(2*w))/(w**4 * (Rw/Rtirr)))**2
        return k

def coates_deno(phi, swirr, c1):
        '''
        coates_deno(phi, swirr, c1)
        *Input parameters:
         - phi - porosity
         - swirr - water saturation of a zone at irreducible water saturation
         - c1 - coefficient between 6500 to 10000 for oil, 650 to 1000 for gas
        *Returns:
         - k - permeability [mD] calculated with Coates-Deno formula (or Coates simplified) dated (1981)
        '''
        c1 = 100
        k = (c1 * phi **2 * (1 - swirr) / swirr)**2
        return k

def lucia(phie, phisec, swirr):
        '''
        lucia(phi, phiSec, swirr)
        *Input parameters:
         - phie - shale corrected porosity from density neutron logs (fractional)
         - phisec - secondary porosity index (SPI) (fractional)
         - swirr - water saturation (fractional)
         - phig - inter-grain porosity (fractional)
         - rfn - rock fabric number (unitless)
        *Returns:
         - k - permeability (mD) calculated by Lucia(2003) formula
        '''
        phig = phie - phisec
        rfn = math.exp(7.163 + 1.883 * math.log(phig) + math.log(swirr)) / (3.063 + 0.610 * math.log(phig))
        k = math.exp((27.56 - 12.08 * math.log(rfn)) + ((8.671 - 3.603 * math.log(rfn)) * math.log(phig)))
        return k

def fractureperm(wf, df, kf1):
        '''
        fractureperm(wf, df, kf1)
        *Input parameters:
        - df - fracture frequency (fractures per meter)
        - wf - fracture aperture (millimeters)
        - kf1 - number of main fracture directions (1 for sub-horizontal or sub-vertical;
        2 for orthogonal sub-vertical; 3 for chaotic or brecciated)
        - phi_frac - fracture porosity from scanner (fractional)
        *Returns:
        - k - fracture permability (mD) from fractures
        '''
        phi_frac = 0.001* wf * df * kf1
        k = 833 * 10**11 * phi_frac**3 / (df**2 * kf1**2)
        return k
