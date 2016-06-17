'''
List of functions:
m - lithology identifier M
n - lithology identifier N
ro_maa - apparent matrix density
dtmaa - apparent matrix transit time
umaa - apparent matrix volumetric cross section
'''

def m(dt,dt_fl,den,den_fl):
    '''
    m(dt,dt_fl,den,den_fl)
    *Input parameters:
    - dt - sonic transit time from log [us/ft]
    - dt_fl - sonic transit time in the formation fluid[us/ft]
    - den - bulk density from log [g/cc]
    - den_fl - fluid density [g/cc]
    *It Calculates:
    - m - lithology indentifier "m" calculated with m =(dt_fl-dt)/(den - den_fl)* 0.01
    For metric you need to multiply equations with 0.003
    '''
    m =(dt_fl-dt)/(den - den_fl)* 0.01
    return m

def n(phin,phin_fl,den,den_fl):
   '''
   n(den,den_fl,phin,phin_fl)
    *Input parameters:
    - phin - neutronic porosity in limestone units [decimal]
    - phin_fl - neutronic porosity of the fluid of the formation (ussualy=1)[decimal]
    - den - bulk density from log [g/cc]
    - den_fl - fluid density [g/cc]
    *It Calculates:
    - n - lithology indentifier "n" calculated with n=(phin_fl-phin))/(den - den_fl)
    '''
   n = (phin_fl-phin)/(den - den_fl)
   return n

def romaa(den, den_fl, phi_ND):
    '''
    romaa(den, den_fl, phi_ND)
    *Input parameters:
    - den - bulk density from log [g/cc]
    - den_fl - fluid density [g/cc] 
    - phi_ND - neutron-density crossplot porosity [decimal]
    *It calculates:
    - romaa - apparent matrix density [g/cc]
    '''
    romaa = (den - phi_ND * den_fl)/(1-phi_ND)
    return romaa

def dtmaa(dt, dt_fl, phi_NS):
    '''
    dtmaa(dt, dt_fl, phi_NS)
    *Input parameters:
     - dt - sonic transit time from log [us/ft]
     - dt_fl - sonic transit time in the formation fluid[us/ft]
     - phi_NS - neutron-sonic crossplot porosity [decimal]
    *It calculates:
    - dtmaa - apparent matrix transit time [us/ft]
     '''
    dtmaa = (dt - phi_NS * dt_fl) / (1-phi_NS)
    return dtmaa

def umaa(den, PEF, U_fl, phi_ND):
    '''
    umaa(den, PEF, U_fl, phi_ND)
    *Input parameters:
    - den - bulk density from log [g/cc]
    - PEF - photoelectric absorption [barns/electron]
    - U_fl - fluid volumetric cross section (0.398 barns/cm3 for fresh water, 1.36 barns/cm3 for salt water)
    - phi_ND - neutron-density crossplot porosity [decimal]
    *It calculates:
    - umaa - apparent matrix volumetric cross section [barns/cm3] calculated with  u_maa = ((PEF * den) - (phi_ND * U_fl))/(1-phi_ND)
    '''
    umaa = ((PEF * den) - (phi_ND * U_fl))/(1-phi_ND)
    return umaa
