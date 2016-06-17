from . import sw

# Water Saturation of invaded zone
# it uses formulas from sw module
# by replacing the Rmf with Rw, Rxo with Rt

def archie(Rmf, Rxo, Phi, a, m, n):
        archie = sw.archie(Rmf, Rxo, Phi, a, m, n)
        return archie
    
def simandoux(Rmf, Rxo, Phi, Rsh, Vsh, a, m):
        simandoux = sw.simandoux(Rmf, Rxo, Phi, Rsh, Vsh, a, m)
        return simandoux

def modified_simandoux(Rmf, Rxo, Phi, Rsh, Vsh, a, m):
        modified_simandoux = sw.modified_simandoux(Rmf, Rxo, Phi, Rsh, Vsh, a, m)
        return modified_simandoux

def schlumberger(Rmf, Rxo, Phi, Rsh, Vsh):
        schlumberger = sw.schlumberger(Rmf, Rxo, Phi, Rsh, Vsh)
        return schlumberger

def fertl(Rmf, Rxo, Phi, Rsh, Vsh, a):
        fertl= sw.fertl(Rmf, Rxo, Phi, Rsh, Vsh, a)
        return sw_fertl

def poupon(Rmf, Rxo, Phi, Rsh, Vsh, a, m, n):
        poupon = sw.poupon(Rmf, Rxo, Phi, Rsh, Vsh, a, m, n)
        return poupon

def indonesian(Rmf, Rxo, Phi, Rsh, Vsh, a, m, n):
        indonesian = sw.indonesian(Rmf, Rxo, Phi, Rsh, Vsh, a, m, n)
        return indonesian        
        
def modified_indonesian(Rmf, Rxo, Phi, Rsh, Vsh, a, m, n):
        modified_indonesian = sw.modified_indonesian(Rmf, Rxo, Phi, Rsh, Vsh, a, m, n)
        return modified_indonesian

def waxmansmith(Rmf, Rxo, PhiT, aa, mm, CEC):
        waxmansmith = sw.waxmansmith(Rmf, Rxo, PhiT, aa, mm, CEC)
        return waxmansmith


def juhasz(Rmf, Rxo, PhiT, PhiSh, a, m, Vsh, Rsh, Temp):
        juhasz = sw.juhasz(Rmf, Rxo, PhiT, PhiSh, a, m, Vsh, Rsh, Temp)
        return juhasz


def dualwater(Rmf, Rxo, PhiT, PhiTSh, Vsh, Rsh):
        dualwater = sw.dualwater(Rmf, Rxo, PhiT, PhiTSh, Vsh, Rsh)
        return dualwater

def archiet(Rmf, Rxo, PhiT, a, m, n):
        archiet = sw. archiet(Rmf, Rxo, PhiT, a, m, n)
        return archiet
