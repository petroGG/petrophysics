
def phie (phit, vcl, phish):
    phie = phit - vcl * phish
    return phie

def density(den, den_ma, den_fl, vcl=0, den_sh=0):
    '''
    density(den, den_ma, den_fl, vcl, den_sh)
    den_ma = 2.65 g/cc (sandstones), 2.71g/cc(limestone), 2.876  g/cc (dolomite)
    den_fl = 1 g/cc (fresh water), den_fl= 1.1 g/cc (salt water), fluid meaning DRILLING FLUID ?!?
    Returns:
    density porosity, with shale correction, if vcl & shale_density are provided
    '''
    phid = (den - den_ma) / (den_fl - den_ma)
    phid_sh = (den_sh - den_ma) / (den_fl - den_ma)
    phid_sh_corr = phid - vcl * phid_sh
    return phid_sh_corr

def willie(dt, dt_ma, dt_fl, vcl=0, dt_sh=0, cp = 1):
    '''
    willie(dt, dt_ma, dt_fl, vcl=0, dt_sh=0, cp = 1)
    dt_ma = 55.5 us/ft (sandstones), 47.3 us/ft(limestone), 43.7 us/ft (dolomite)
    dt_fl = 200 us/ft (fresh water), 189 us/ft (salt water), fluid meaning fm FLUID
    Returns:
    sonic porosity by Willie (average-time), with shale correction, if vcl & shale_dt are provided
    '''
    phis_w=(1/cp)*(dt-dt_ma)/(dt_fl-dt_ma)
    phis_w_sh = (dt_sh-dt_ma)/(dt_fl-dt_ma)
    phis_w_sh_corr = phis_w - vcl * phis_w_sh
    return phis_w_sh_corr

def raymer(dt, dt_ma, dt_fl, vcl=0, dt_sh=0, alpha = 5/8):
    '''
    raymer(dt, dt_ma, dt_fl, vcl=0, dt_sh=0, alpha = 5/8)
    dt_ma = 55.5 us/ft (sandstones), 47.3 us/ft(limestone), 43.7 us/ft (dolomite)
    dt_fl = 200 us/ft (fresh water), 189 us/ft (salt water), fluid meaning fm FLUID
    Returns:
    sonic porosity by Raymer Method (field), with shale correction, if vcl & shale_dt are provided
    '''
    phis_rhg=(alpha)*(dt-dt_ma)/(dt)
    phis_rhg_sh = (dt_sh-dt_ma)/(dt_fl-dt_ma)
    phis_rhg_sh_corr = phis_rhg - vcl * phis_rhg_sh
    return phis_rhg_sh_corr

def neutronic(neut, vcl, neut_sh):
    '''
    neutronic(neut, vcl, neut_sh)
    Ussualy NPHI is expressed in limestone pu.
    If sandstone is your matrix than neut_sand=neut_limestone-0.028
    Returns:
    shale corrected neutron porosity
    '''
    neut_sh_corr = neut-vcl*neut_sh
    return neut_sh_corr

