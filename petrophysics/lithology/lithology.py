'''
List of functions:
m - lithology identifier M
n - lithology identifier N
ro_maa - apparent matrix density
dtmaa - apparent matrix transit time
umaa - apparent matrix volumetric cross section
ur_lith - umaa-ro_maa-based lithology estimate
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

def ur_lith(umaa, romaa, **kwargs):
    '''
    ur_lith(umaa, romaa)
    *Input parameters:
    - umaa - apparent matrix volumetric cross section [barns/cm3]
    - romaa - apparent matrix density [g/cc]
    *It calculates and returns a tuple in the form of (ur_qtz, ur_cal, ur_dol) where:
    - ur_qtz - volume of quartz (v/v)
    - ur_cal - volume of calcite (v/v)
    - ur_dol - volume of dolomite (v/v)
    Solution after: Doveton, J.H. (1994), _Geologic Log Analysis Using Computer Methods_, 
                    AAPG Computer Applications in Geology, No. 2
    *Requires: NumPy for matrix inversion
    '''
    import numpy as np

    qtz_roma = 2.65
    cal_roma = 2.71
    dol_roma = 2.87
    qtz_uma = 4.80
    cal_uma = 13.80
    dol_uma = 9.00
    unity = 1.00

    inv = np.matrix([[qtz_roma, cal_roma, dol_roma],
                     [qtz_uma, cal_uma, dol_uma],
                     [unity, unity, unity]]).I

    qtz = inv[0,0] * romaa + inv[0,1] * umaa + inv[0,2]
    cal = inv[1,0] * romaa + inv[1,1] * umaa + inv[1,2]
    dol = inv[2,0] * romaa + inv[2,1] * umaa + inv[2,2]
    if qtz < 0.0:
        qtz = 0.0
    if qtz > 1.0:
        qtz = 1.0
    if cal < 0.0:
        cal = 0.0
    if cal > 1.0:
        cal = 1.0
    if dol < 0.0:
        dol = 0.0
    if dol > 1.0:
        dol = 1.0
    ur_qtz = qtz / (qtz + cal + dol)
    ur_cal = cal / (qtz + cal + dol)
    ur_dol = dol / (qtz + cal + dol)

    return ur_qtz, ur_cal, ur_dol

