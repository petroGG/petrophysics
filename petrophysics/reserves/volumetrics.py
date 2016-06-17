'''
List of functions:
ooip - original oil in place
ogip - original gas in place
oil - oil reserves
gas - gas reserves
tarweight - tar oil in place
ghip - gas hydrates in place
bg - gas volume factor
bo - oil volume factor
rf - recovery factor estimated from sw, sxo
'''

def ooip(area, thickness, sw, phi, ngr, bo, metric=True):
    '''
    ooip(area, thickness, sw, phi, ngr, bo, metric=True)
    *Input parameters:
    - area - [m2] or [acres]
    - thickness - gross thickness in [m] or [ft]
    - sw - water saturation (fractional)
    - phi - effective porosity (fractional)
    - ngr - Net/Gross Ratio (fractional)
    - bo - Oil Volume Factor [res bbl/ ST bbl]
    *Returns:
     - ooip (original oil in place) in [m3] or [bbl]
    '''
    so = 1 - sw
    if metric==True:
        ooip = area * thickness * so * phi * ngr / bo
    else:
        ooip = 7758 * area * thickness * so * phi * ngr / bo
    return ooip

def ogip(area, thickness, sw, phi, ngr, bg):
    '''
    ogip(area, thickness, sw, phi, ngr, bo, metric=True)
    *Input parameters:
    - area - in [m2] or [uk]
    - thickness - gross thickness in [m] or [ft]
    - sw - water saturation (fractional)
    - phi - effective porosity (fractional)
    - ngr - Net/Gross Ratio (fractional)
    - bo - Gas Volume Factor for gas at initial conditions
    *Returns:
     - ogip (original oil in place) in [m3] or [bbl]
    '''
    sg = 1 - sw
    if metric==True:
        ogip = area * thickness * sg * phi * ngr / bg
    else:
        ogip = 7758 * area * thickness * sg * phi * ngr / bg
    return ogip
    
def oil(ooip, RF):
    oilreserves = ooip * RF
    return oilreserves

def gas(ogip, RF):
    oilreserves = ooip * RF
    return gasreserves

def tarweight(area, netpay, sw, phie, vsh, den_hy, den_ma, den_sh, den_wa):
    '''
    tarweight(area, netpay, sw, phie, vsh, den_hy, den_ma, den_sh, den_wa)
    *Input parameters:
    - area - acres or m2
    - netpay - 
    - sw - water saturation
    - vsh - volume of shale
    - denHy - hydrocarbon density kg/m3
    - denMa - matrix density kg/m3
    - denSh - shale density kg/m3
    - denWa - water density kg/m3
    *Calculated variables:
    - wt_tar - Tar weight - tonnes/m2
    - wt_sh - Shale weight - tonnes/m2 
    - wt_snd - Sand weight - tonnes/m2
    - wt_wtr - Water weight - tonnes/m2
    - wt_rock - Total rock weight - tonnes/m2
    - tar_frac - Tar mass fraction
    - tar_wt_percent - Tar weight - decimal percent
    *Returns:
    - ooip_m3 - original oil in place [m3]
    '''
    wt_tar = phie * (1 - sw) * den_hy / 1000
    wt_snd = (1 - vsh - phie) * den_ma / 1000
    wt_shale = vsh * den_sh / 1000
    wt_water = phie * sw * den_wa / 1000
    wt_rock = wt_tar + wt_shale + wt_snd + wt_water
    tar_frac = wt_tar / wt_rock
    tar_wt_percent= 100 * wt_tar / wt_rock
    ooip_tonnes = 0.001 * tar_frac * netpay * den_hy * area
    ooip_m3 = ooip_tonnes / den_hy
    return ooip_m3

def ghip(area, thickness, phie, metric = True, methane = True):
    '''
    ghip(area, thickness, phie kg0, kv3)
    *Input parameters:
     - area - reservoir area (m2 or acres)
     - thickness - m or ft
     - c - 1 for Metric units, 43.56 for English units 
     - kg0 - equivalent gas hydrate volume factor (fractional):170 for methane, 60 for propane
     - hpv - hydrocarbon volume (feet or meters)
     - pv - pore volume (feet or meters)
    Returns:
     - ghip - gas in place as hydrates (Mcf or m3)
     '''
    pv = phie * thickness
    if methane == True:
        kg0 = 170
    else:
        kg0 = 60
    hpv = pv * kg0
    #Calculate gas in place.
    if metric == True:
        c = 1
    else:
        c = 43.56
    ghip = c * hpv * area
    return ghip

def bg(p0, t0, pf, tf, z, metric=False):
    '''
    *Input parameters:
    - p0 - surface pressure (14.5psi / 1atm)
    - t0 - surface temp
    - p1 - formation pressure
    - t1 - formation temperature
    - zp - gas compresiibility
    - k - conversion factor for temperature to R degrees(460 for English, 273 for Metric)
    *Returns:
     - bg - gas volume factor
    '''
    if metric==True:
        k = 273
    else:
        k = 460
    bg = round((p0 * (t0 + k)) / (pf * (tf + k)) * z,3)
    return bg

def bo(gor, metric = True):
    '''
    bo(gor, metric = True)
    *Input parameters:
    - gor - gas oil ratio in m3/m3 or scf/bbl
    - n - no of hundreds ft of gas produced per bbl of oil
    *Returns:
    - bo - gas volume factor (scf/bbl)
    '''
    if metric==True:
        n = gor / 0.17810760667903525 / 100
    else:
        n = gor/100
    bo = round (1.05 + (n * 0.05),1)
    return bo

def rf(sw,sxo):
    '''
    rf(sw,sxo)
    *Input parameters:
    - sw - water saturation
    - sxo - flushed zone water saturation
    *Returns:
     - rf - recovery factor
    '''
    rf = (sxo-sw)/(1-sw)
    return rf
