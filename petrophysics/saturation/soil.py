from . import sw

# Saturation of oil
# it uses formulas from sw module
# So = 1 - Sw

def oil(water_saturation):
        soil = 1 - water_saturation
        return soil

def archie(Rw, Rt, Phi, a, m, n):
        archie = 1 - sw.archie (Rw, Rt, Phi, a, m, n)
        return archie
    
def simandoux(Rw, Rt, Phi, Rsh, Vsh, a, m):
        simandoux = 1 - simandoux(Rw, Rt, Phi, Rsh, Vsh, a, m)
        return simandoux

def modified_simandoux(Rw, Rt, Phi, Rsh, Vsh, a, m):
        modified_simandoux = 1 - sw.modified_simandoux(Rw, Rt, Phi, Rsh, Vsh, a, m)
        return modified_simandoux

def schlumberger(Rw, Rt, Phi, Rsh, Vsh):
        schlumberger = 1 - sw.schlumberger(Rw, Rt, Phi, Rsh, Vsh)
        return schlumberger

def fertl(Rw, Rt, Phi, Rsh, Vsh, a):
        fertl= 1 - sw.fertl(Rw, Rt, Phi, Rsh, Vsh, a)
        return sw_fertl

def poupon(Rw, Rt, Phi, Rsh, Vsh, a, m, n):
        poupon = 1 - sw.poupon(Rw, Rt, Phi, Rsh, Vsh, a, m, n)
        return poupon

def indonesian(Rw, Rt, Phi, Rsh, Vsh, a, m, n):
        indonesian = 1 - sw.indonesian(Rw, Rt, Phi, Rsh, Vsh, a, m, n)
        return indonesian        
        
def modified_indonesian(Rw, Rt, Phi, Rsh, Vsh, a, m, n):
        modified_indonesian = 1 - sw.modified_indonesian(Rw, Rt, Phi, Rsh, Vsh, a, m, n)
        return modified_indonesian

def waxmansmith(Rw, Rt, phiT, aa, mm, CEC):
        waxmansmith = 1 - sw.waxmansmith(Rw, Rt, phiT, aa, mm, CEC)
        return waxmansmith

def juhasz(Rw, Rt, PhiT, PhiSh, a, m, Vsh, Rsh, Temp):
        juhasz = 1 - sw.juhasz(Rw, Rt, PhiT, PhiSh, a, m, Vsh, Rsh, Temp)
        return juhasz

def dualwater(Rw, Rt, PhiT, PhiTSh, Vsh, Rsh):
        dualwater = 1 -sw.dualwater(Rw, Rt, PhiT, PhiTSh, Vsh, Rsh)
        return dualwater

def archiet(Rw, Rt, PhiT, a, m, n):
        archiet = 1 - sw.archiet(Rw, Rt, PhiT, a, m, n)
        return archiet

def ratio(Rw, Rt, Rmf, Rxo):
        ratio = 1 - sw.ratio(Rw, Rt, Rmf, Rxo)
        return ratio

