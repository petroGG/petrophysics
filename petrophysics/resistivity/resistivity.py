__all__ = ['arp', 'ssp', 'rwsp', 'rwsp1', 'rwratio', 'rwarchie', 'rwchloride']

import math

def arp(r0, t0, tf, celsius = True):
    '''
    arp(r0, t0, tf, temperature_units)
    Examples:
    arp (0.32, 77, 102, celsius = False)
    arp (0.32, 25, 39, celsius = True)
    *Input parameters:
    r0 - resistivity at surface
    t0 - temperature at surface
    tf - temperature at formation
    celsius = True - temperature units in Celsius
    celsius = False - temperature units in Fahrenheit
    *Calculated parameters:
    arp - returns the resistivity at formation temperature tf
    '''
    if celsius == True:
        k = 21.5
        arp = r0*(t0 + k)/(tf + k)
    else:
        k = 6.77
        arp = r0*(t0 + k)/(tf + k)
    return arp

def ssp (sp, bed_thickness, Rm, Ri, metric = True):
    '''
    ssp (sp, bed_thickness, Rm, Ri)
    Exemples:
    ssp(-90,22,0.92,10)
    ssp(-90,22, arp(1.57,68,121,metric=False),10)
    *Input parameters:
    sp - sp reading from log
    bed_thickness - bed thickness in m (for metric==True) or ft (metric==False)
    Rm - mud resistivity (already converted at formation temperature)
    Ri - shallow resistivity (in the invaded zone)
    *Calculated parameters:
    SSP - static sp corrected for bed_thickness thickness and invasion
    Formulation of sp correction factor (from Western Atlas 1992, bed_thickness>3ft <50ft and Ri/Rm>5)
    '''
    if metric == True:
        bed_thickness = bed_thickness * 3.28084
    if (bed_thickness > 50 or Ri/Rm < 5):
        sp_correction = 1
    else:
        term1 = (4*(Ri/Rm)+2)**(1/3.65)-1.5
        term2 = bed_thickness - ((Ri/Rm + 11)/0.65)**1/6.05 - 0.1
        sp_correction = term1/term2+0.95
    SSP = sp * sp_correction
    return SSP

def rwsp(sp, Rm0, Rmf0, Ri, t0, tf, bed_thickness, metric = True):
    '''
    rwsp(sp, Rm0, Rmf0, Ri, t0, tf, bed_thickness, metric = True)
    *Input parameters:
    - sp - sp reading from log
    - Rm0 - mud resistivity measured at t0 temperature
    - Rmf0 - mud filtrate resistivity measured at t0 temperature
    - Ri - shallow resistivity (in the invaded zone)
    - t0 - temperature at surface
    - tf - formation temperature
    *Calculated parameters:
    - Rwe - equivalent water resistivity
    - RwSP - water resistivity from SP log
    '''
    if metric==True:
        tff = 9 /5 * tf + 32
    else:
        tff = tf
    K = 61+0.133*tff
    
    Rm = arp(Rm0, t0, tff, metric = False)

    #Correct sp to ssp:
    if metric == True:
        bed_thickness = bed_thickness * 3.28084
    SSP = ssp (sp, bed_thickness, Rm, Ri)

    # formulation from Crain
    Rmftf = arp(Rmf0, t0, tff, metric = False)
    Rmf = arp(Rmf0, t0, tff, metric = False)
    if Rmf > 0.1:
        Rmfe =  0.85 * Rmf
    else:
        Rmfe = (146 * Rmf - 5) / (337 * Rmf + 77)
    Rwe = Rmfe * 10**(SSP/K)

    if Rwe > 0.12:
        RwSP = -0.58 -10 **(0.69 * Rwe - 0.24)
    else:
        RwSP = (77 * Rwe + 5)/(146-337*Rwe)
    return RwSP

def rwsp1(sp, Rmf0, t0, tf, metric = True):
    '''
    rwsp1(sp, Rmf0, t0, tf, units)
    Formula from Djeebbar_Tiab_... book (p.825)
    *Input parameters:
    - Rmf0 - mud filtrate resistivity
    - t0 - temperature at surface
    - tf - formation temperature
    *Calculated parameters:
    - k - temperature correction
    - SSP - sp correction of bed_thickness thickness and invasion
    - Rmfe - equivalent mud filtrate resistivity
    - Rwe - equivalent water resistivity
    *Returns:
    - RwSP - water resistivity from sp
    '''
    if metric == True:
        tff = 5/9 * tf + 32
    else:
        tff = tf
    k = 61+0.133*tff
    
    Rmf = arp(Rmf0, t0, tff, metric == False)
    SSP = sp
    Rwe = Rmf / 10**(-SSP/k)

    if Rwe > 0.08:
        RwSP = Rwe
    else:
        RwSP = (Rwe + 0.131 * 10**((1/math.log(tff/19.9))-2))/(-0.5*Rwe+10**(0.0426/(math.log(tff/50.8))))         
    return RwSP

def rwratio(Rt, Rmf, Rxo):
    '''
    rwratio(Rt, Rmf, Rxo)
    *Input parameters:
    - Rt - true resistivity
    - Rmf - mud filtrate resistivity corrected at formation temperature
    - Rxo - flushed zone resistivity
    *Returns:
    - RwRatio - water resisitivity by ratio method
    '''
    RwRatio = Rt * (Rmf / Rxo)
    return RwRatio

def rwarchie(Rt, Phi, a, m):
    '''
    rwarchie(Rt, Phi, a, m)
    **calculates water resistivity Rw in a 100% water-formation ***
    *Input parameters:
    - Rt - true resistivity
    - Phi - porosity (fractional)
    - a - turtousity factor
    - m - cementation exponent
    *Returns:
    - RwARCHIE - resistivity of a 100% water bearing formation calculated with Archie formula (when Sw=1)
    '''
    RwARCHIE = Rt * Phi**m / a
    return RwARCHIE

def rwchloride(nacl, tf):
    '''
    rwchloride(nacl, tf)
    **calculates water resistivity from salinity at a given temperature**
    *Input parameters:
    - nacl - sodium chlorides [ppm]
    - tf - formation temperature [F]
    *Returns:
    - RwChloride - [ohm.m] calculated with Crain formula.
    '''
    RwChloride = (400000 / (nacl* tf))**0.88
    return RwChloride
