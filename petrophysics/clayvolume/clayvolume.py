'''
Clay Volume from single Methods:
vclgr - GR,
vclth - thorium,
vclk - potassium,
vclsp - SP,
vclr - Resistivity,
vclneut - Neutronic,
vcllog - any log;

Dual methods:
vclnd - ND,
vclds - SD,
vclns - NS,
vcllog1log2 -log1log2
''' 

def vclgr(gr_log, gr_clean, gr_clay, correction=None):
    '''
    vclgr(gr_log, gr_clean, gr_clay, correction=None)
    *Input parameters:
    - gr_log - GR log reading
    - gr_clean - sand line value, read at gr_min
    - gr_clay - clay/shale line value, read at gr_max
    - Corrections are:
       'linear'
       'young' - #Larionov (1969) - Tertiary rocks
       'older' - #Larionov (1969) - Older rocks
       'clavier' - #Clavier (1971)
       'steiber' - #Steiber (1969)
    *Returns:
    - vclgr - volume of clay from GR
    '''
    igr=(gr_log-gr_clean)/(gr_clay-gr_clean)        #Linear Gamma Ray
    if (correction == "young" or correction =='tertiary'):
        vclgr_larionov_young=0.083*(2**(3.7*igr)-1) #Larionov (1969) - Tertiary rocks
        vclgr=vclgr_larionov_young
    elif correction == "older":
        vclgr_larionov_old=0.33*(2**(2*igr)-1)      #Larionov (1969) - Older rocks
        vclgr=vclgr_larionov_old
    elif correction=="clavier":
        vclgr_clavier=1.7-(3.38-(igr+0.7)**2)**0.5  #Clavier (1971)
        vclgr=vclgr_clavier
    elif correction=="steiber":
        vclgr_steiber=0.5*igr/(1.5-igr)             #Steiber (1969) - Tertiary rocks
        vclgr=vclgr_steiber
    else:
        vclgr=igr
    return vclgr
    
def vclth(th_log, th_clean, th_clay):
    '''
    vclth(th_log, th_clean, th_clay)
    *Input parameters:
    - th_log - SP log reading
    - th_clean - thorium log reading in clean zone
    - th_clay - thorium log reading in clay zone
    *Returns:
    - vclth - volume of clay from Thorium log
    '''
    vclth = (th_log-th_clean)/(th_clay-th_clean)
    return mvclth

def vclk(k_log, k_clean, k_clay):
    '''
    vclk(th_log, th_clean, th_clay)
    *Input parameters:
    - k_log - potassium log reading
    - k_clean - potassium log reading in clean zone
    - k_clay - potassium log reading in clay zone
    *Returns:
    - vclk - volume of clay from K (potassium) log
    '''
    vclk = (k_log-k_clean)/(k_clay-k_clean)
    return vclk

def vclsp(sp_log, sp_clean, sp_clay):
    '''
    vclsp(sp_log, sp_clean, sp_clay)
    *Input parameters:
    - sp_log - SP log reading
    - sp_clean - sand line value, read at sp_min
    - sp_clay - clay/shale line value, read at sp_max
    *Returns:
    - vclsp - volume of clay from SP log
    '''
    vclsp=(sp_log-sp_clean)/(sp_clay-sp_clean)
    return vclsp

def vclr(r_log, r_clean, r_clay):
    '''
    vclr(r_log, r_clay, r_clean)
    *Input parameters:
    - r_log - Resistivity log reading
    - r_clean - Resistivity clean reading
    - r_clean - Resistivity clay reading
    *Returns:
    - vclr - volume of clay from Resistivity log
    '''
    vr=(r_clay/r_log)*(r_clean-r_log)/(r_clean-r_clay)
    if (r_log > 2* r_clay):
        vclr = 0.5 * (2 * vr)**(0.67*(vr+1)) 
    else:
        vclr = vr
    return vclr

def vclneut(neut_log,neut_clay,neut_clean):
    '''
    vclneut(neut_log,neut_clay,neut_clean)
    *Input parameters:
    - neut_log - Neutronic log reading
    - neut_clean- Neutronic clean reading
    - neut_clay - Neutronic clay/shale reading
    *Returns:
    - vclneut - volume of clay from Neutronic log
    '''
    vclneut=((neut_log/neut_clay)*(neut_log-neut_clean)/(neut_clay-neut_clean))**0.5
    return vclneut

def vcllog(log, log_clean, log_clay):
    '''
    vcllog(log, sp_clean, sp_clay)
    *Input parameters:
    - log - the log reading
    - log_clean - sand line value, read at sp_min
    - log_clay - clay/shale line value, read at sp_max
    *Returns:
    - vcllog - volume of clay from a log at your choice
    '''
    vcllog=(log-log_clean)/(log_clay-log_clean)
    return vcllog

#DOUBLE-CLAY Indicators: ND, SD, SN

def vclnd(neut,den,neut_clean1,den_clean1,neut_clean2,den_clean2,neut_clay,den_clay):
    '''    
    vclnd(neut,den,neut_clean1,den_clean1,neut_clean2,den_clean2,neut_clay,den_clay):
    It calculates the Clay Volume from ND (Neutron Density) - by defining a clean line and a clay point
    *Input parameters:
    - The clean line is defined by the line with the following points: (neut_clean1,den_clean1), (neut_clean2,den_clean2)
    - The clay point is defined by: (neut_clay, den_clay)
    - Readings from logs: neut, den
    *Returns:
    - vclnd - volume of clay from Neutron - Density 
    '''
    term1 = (den_clean2-den_clean1)*(neut-neut_clean1)-(den-den_clean1)*(neut_clean2-neut_clean1)
    term2 =(den_clean2-den_clean1)*(neut_clay-neut_clean1)-(den_clay-den_clean1)*(neut_clean2-neut_clean1)
    vclnd=term1/term2
    return vclnd

def vclsd(sonic,den,sonic_clean1,den_clean1,sonic_clean2,den_clean2,sonic_clay,den_clay):
    '''
    vclsd(sonic,den,sonic_clean1,den_clean1,sonic_clean2,den_clean2,sonic_clay,den_clay)
    It calculates the Clay Volume from SD (Sonic Density) - by defining a clean line and a clay point
    *Input parameters:
    - The clean line is defined by the line with the following points: (sonic_clean1,den_clean1), (sonic_clean2,sonic_clean2)
    - The clay point is defined by: (sonic_clay, den_clay)
    - Readings from logs: sonic, den
    *Returns:
    - vclsd - volume of clay from Sonic - Density 
    '''
    term1 = (den_clean2-den_clean1)*(sonic-sonic_clean1)-(den-den_clean1)*(sonic_clean2-sonic_clean1)
    term2 =(den_clean2-den_clean1)*(sonic_clay-sonic_clean1)-(den_clay-den_clean1)*(sonic_clean2-sonic_clean1)
    vclsd=term1/term2
    return vclsd

def vclns(neut,sonic,neut_clean1,sonic_clean1,neut_clean2,sonic_clean2,neut_clay,sonic_clay):
    '''
    vclns(neut,sonic,neut_clean1,sonic_clean1,neut_clean2,sonic_clean2,neut_clay,sonic_clay)
    It calculates the Clay Volume from NS (Neutron Sonic) - by defining a clean line and a clay point
    *Input parameters:    The clean line is defined by the line with the following points: (neut_clean1,sonic_clean1), (neut_clean2,sonic_clean2)
    - The clay point is defined by: (neut_clay, sonic_clay)
    - Readings from logs: neut,sonic
    *Returns:
    - vclns - volume of clay from Neutron - Sonic 
    '''
    term1 = (neut_clean2-neut_clean1)*(sonic-sonic_clean1)-(neut-neut_clean1)*(sonic_clean2-sonic_clean1)
    term2 =(neut_clean2-neut_clean1)*(sonic_clay-sonic_clean1)-(neut_clay-neut_clean1)*(sonic_clean2-sonic_clean1)
    vclns=term1/term2
    return vclns

def vcllog1log2(log1,log2,log1_clean1,log2_clean1,log1_clean2,log2_clean2,log1_clay,log2_clay):
    '''
    vcllog1log2(log1,log2,log1_clean1,log2_clean1,log1_clean2,log2_clean2,log1_clay,log2_clay)
    It calculates the Clay Volume from XPlot of two logs at your choice (Log1, Log2) - by defining a clean line and a clay point
    *Input parameters:
    - The clean line is defined by the line with the following points: (log1_clean1,log2_clean1), (log1_clean2,log2_clean2)
    - The clay point is defined by: (log1_clay, log2_clay)
    - Readings from logs: log1, log2
    *Returns:
    - vclns - volume of clay from Neutron - Sonic 
    '''
    term1 = (log1_clean2-log1_clean1)*(log2-log2_clean1)-(log1-log1_clean1)*(log2_clean2-log2_clean1)
    term2 =(log1_clean2-log1_clean1)*(log2_clay-log2_clean1)-(log1_clay-log1_clean1)*(log2_clean2-log2_clean1)
    vcllog1log2 = term1 / term2
    return vcllog1log2
