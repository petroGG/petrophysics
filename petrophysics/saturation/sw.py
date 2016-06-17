import math
'''
List of water saturation formulas:
- archie
- simandoux
- modified Simandoux
- schlumberger
- fertl
- poupon
- indonesian
- modified indonesian
Eq that require PhiT:
- waxmansmith
- juhazs
- dualwater
- archiet
Eq requiring Rw,Rt,Rmf,Rxo:
- ratio
'''

def archie(Rw, Rt, Phi, a, m, n):
        '''
        archie(Rw, Rt, Phi, a, m, n)
        *Input parameters:
        - Rw - water resistivity
        - Rt - true resistivity
        - Phi - porosity (must be effective); Using PoroT (Total Porosity will lead to SwArchiePhit)
        - a - tortuosity factor  (sandstones: 0.62 ; limestone: )
        - m - cementation exponent (sandstones:  ; limestone: )
        - n - saturation exponent  (sandstones: 2.15 ; limestone: )
        - F - formation factor
        *Returns:
         - archie - water saturation from Archie equation
        '''
        F = a / (Phi**m)
        archie = (F * Rw/Rt)**n
        return archie
    
def simandoux(Rw, Rt, Phi, Rsh, Vsh, a, m):
        '''
        simandoux(Rw, Rt, Poro, Rsh, Vsh, a, m)
        **Simandoux (1963)
          for shaly-sandy formations, used with saline fm waters
          Equation soved for n=2
        *Input parameters:
        - Rw - water resistivity
        - Rt - true resistivity
        - Phi - porosity
        - Rsh - shale resistivity
        - a - tortuosity factor
        - m - cementation exponent
        - n - saturation exponent
        - Vsh - Volume of shale
        *Returns:
         - simandoux - water saturation from Simandoux
        '''
        term1 = Phi**m/(a*Rw)
        term2 = Vsh/Rsh
        term3 = -1/Rt
        delta = (term2**2 - 4*term1*term3)**(1/2)
        simandoux = ((-1)*term2 + delta) / 2*term1
        return simandoux

def modified_simandoux(Rw, Rt, Phi, Rsh, Vsh, a, m):
        '''
        modified_simandoux(Rw, Rt, Poro, Rsh, Vsh, a, m)
        **Modified Simandoux (19xx  ?)
          shaly-sandy formations with saline fm waters
          Equation soved for n=2
        *Input parameters:
        - Rw - water resistivity
        - Rt - true resistivity
        - Phi - porosity
        - Rsh - shale resistivity
        - Vsh - Volume of shale
        - a - tortuosity factor
        - m - cementation exponent
        - n - saturation exponent
        *Returns:
         - modified_simandoux - water saturation from modified Simandoux eq.
        '''
        term1 = Phi**m/(a*Rw*(1-Vsh))
        term2 = Vsh/Rsh
        term3 = -1/Rt
        delta = (term2**2 - 4*term1*term3)**(1/2)
        modified_simandoux = ((-1)*term2 + delta) / 2*term1
        return modified_simandoux

def schlumberger(Rw, Rt, Phi, Rsh, Vsh):
        '''
        schlumberger(Rw, Rt, Phi, Rsh, Vsh)
        **Schlumberger (1975)
         used for shaly-sandy formations, doesnt need a,m,n
        *Input parameters:
        - Rw - water resistivity
        - Rt - true resistivity
        - Phi - porosity
        - Rsh - shale resistivity
        - Vsh - Volume of shale
        *Returns:
         - schlumberger - water saturation
        Formula taken from Asquite (Basic Log Intepretation)
        '''
        term1= sqrt((Vsh/Rsh)**2 + Phi**2/(0.2*Rw*Rt*(1-Vsh)))-(Vsh/Rsh)
        term2= Phi**2 /(0.4*Rw*(1-Vsh))
        schlumberger = term1 / term2
        return schlumberger

def fertl(Rw, Rt, Phi, Rsh, Vsh, a):
        '''
        fertl(Rw, Rt, Phi, Rsh, Vsh, a)
        **Fertl (1975)
          used for shaly-sandy formations**
        *Input parameters:
        - Rw - water resistivity
        - Rt - true resistivity
        - Phi - porosity
        - Rsh - shale resistivity
        - a - tortuosity factor
        - m - cementation exponent
        - n - saturation exponent
        - Vsh - Volume of shale
        *Returns:
         - fertl - water saturation
        Formula taken from Asquite (Basic Log Intepretation)
        Exemple for parameter a: 0.25 for Golf Coast; 0.35 for Rocky Mountains
        ''' 
        fertl=(1/Phi)*(sqrt(Rw/Rt+((a*Vsh)/2)**2)-a*Vsh/2)
        return fertl

def poupon(Rw, Rt, Phi, Rsh, Vsh, a, m, n):
        '''
        poupon(Rw, Rt, Phi, Rsh, Vsh, a, m, n)
        **Poupon (19xx ?)
        *Input parameters:
        - Rw - water resistivity
        - Rt - true resistivity
        - Phi - porosity
        - Rsh - shale resistivity
        - Vsh - volume of shale
        - a - tortuosity factor
        - m - cementation exponent
        - n - saturation exponent
        *Returns:
        - poupon - water saturation from Poupon equation
        '''
        term1 = (1/Rt - Vsh/Rsh)
        term2 = a * Rw * (1-Vcl) / Phi**m
        poupon = (term1 * term2)**(1/n)
        return poupon

def indonesian(Rw, Rt, Phi, Rsh, Vsh, a, m, n):
        '''
        indonesian(Rw, Rt, Phi, Rsh, Vsh, a, m, n)
        **Indonesian or Poupon-Leveaux (19xx ?)
          used with fresh fm waters**
        *Input parameters:
        - Rw - water resistivity
        - Rt - true resistivity
        - Phi - porosity
        - Vsh - volume of shale
        - a - tortuosity factor
        - m - cementation exponent
        - n - saturation exponent
        *Returns:
        - indonesian - water saturation from indonesian equation
        '''
        term1 = 1/Rt**(1/2)
        term2 = (Phi**m/(a*Rw))**(1/2)
        term3 = Vsh ** (1-Vsh/2)/Rsh**(1/2)
        indonesian = (term1 / (term2 + term3))**(2/n)
        return indonesian        
        
def modified_indonesian(Rw, Rt, Phi, Rsh, Vsh, a, m, n):
        '''
        modified_indonesian(Rw, Rt, Phi, Rsh, Vsh, a, m, n)
        Modified Indonesian (19xx ?)
        Parameters:
        - Rw - water resistivity
        - Rt - true resistivity
        - Phi - porosity
        - a - tortuosity factor
        - m - cementation exponent
        - n - saturation exponent
        '''
        term1 = 1/Rt**(1/2)
        term2 = (Phi**m / (a*Rw))**(1/2)
        term3 = Vsh**((1-Vsh)/2) / Rsh**(1/2)
        modified_indonesian = (term1 / (term2 + term3))**(2/n)
        return modified_indonesian

def waxmansmith(Rw, Rt, phiT, aa, mm, CEC):
        '''
        waxmansmith(Rw, Rt, PhiT, aa, mm, CEC)
        **Waxman-Smith CEC method (does not require VCL)
          but requires core measurements of CEC
          Eq solved for n=2
        *Input parameters:
         - phiT - total porosity
         - aa - WS tortuosity saturation
         - mm - WS cementation exponent
         - Rw - formation water resistivity ohm.m
         - B - cation mobility (mho cm2 / meq)
         - Qv - concentration of exchange cations per volume unit (meq/ml pore space)
         - CEC - cation exchange capacity of shale(meq/100 gm of sample)
         - den_ma - mineral graind density (g/cc)
         - aa, mm - best determined from SCAL      
        *Returns:
         - SwTotal - total water saturation
        '''
        B = 4.6 * (1 - 0.6 * math.exp(-0.77/Rw))
        Qv = CEC * (1 - phiT) * den_ma / (100*phiT)      
        term1 = phi ** mm / aa * Rw
        term2 = B * Qv * phiT **mm / aa
        term3 = (-1) / Rt
        swT = ((-1)* term2 + (term2 ** 2 - 4*term1*term2)**(1/2)) / (2 * term1) #solve of quadratic eq for positive delta
        return swT

def juhasz(Rw, Rt, PhiT, PhiSh, a, m, Vsh, Rsh, Temp):
        '''
        juhasz(Rw, Rt, PhiT, PhiSh, a, m, Vsh, Rsh, Temp)
        **Juhasz eq (1981)
          Eq solved for n=2
        *Input parameters:
         - PhiT - total porosity
         - PhiSh - shale porosity
         - a - tortuosity saturation
         - m - cementation exponent
         - Rw - formation water resistivity ohm.m
         - Bn - "normalized" cation mobility (mho cm2 / meq) 
         - Qvn - "normalized Qv (ranges from 0-clean sands to 1-shales) (meq/gm)
         - Temp - Formation temperature in Celsius
        *Returns:
         - SwT - total water saturation
        '''
        Bn = (-1.28+0.255*Temp - 4.059 * 10**(-4) * Temp**(-2))/(1 + Rw**1.23*(0.045*Temp-0.27)) #Thomas relation
        Qvn = Vsh * PhiSh / PhiT       
        F = a / Phi ** m
        Fsh = a / PhiSh ** m
        term1 = 1 / (F * Rw)
        term2 = (1 /(Fsh * Rsh) - 1 / Rw) * Vsh * Phish / PhiT
        term3 = (-1) / Rt
        swT = ((-1)* term2 + (term2 ** 2 - 4*term1*term2)**(1/2)) / 2 * term1 #solve of quadratic eq for positive delta
        return swT

def dualwater(Rw, Rt, PhiT, PhiTSh, Vsh, Rsh):
        '''
        dualwater(Rw, Rt, PhiT, PhiTSh, Vsh, Rsh)
        **Dual-Water (clavier, 1977) with later modifications/rearrangements.
          Formulas from Doveton "Principles of mathematical petrophysics"
        *Input parameters:
         - PhiT - total porosity
         - PhiTSh - shale porosity
         - Rw - formation water resistivity [ohm.m]
         - Rsh - shale resistivity [ohm.m]
         - Sb - clay-bound water saturation 
         - Rb - bound-water resistivity
         - swT - total water saturation
         *Returns:
         - sw - efective water saturation (or water saturation in effective pore space)
        '''
        Sb = Vsh * PhiTsh / PhiT
        Rb = Rsh * PhiTsh**2
        term1 = 1
        term2 = (-1)*Sb*(1-Rw/Rb)
        term3 = (-1)*Rw / (Rt*PhiT**2)
        swT = ((-1)* term2 + (term2 ** 2 - 4*term1*term2)**(1/2)) / 2 * term1 #solve of quadratic eq for positive delta
        sw = (swT - Sb) / (1 - Sb)
        return sw
        
def archiet(Rw, Rt, PhiT, a, m, n):
        '''
        archiet(Rw, Rt, PhiT, a, m, n)
        *Input parameters:
        - Rw - water resistivity
        - Rt - true resistivity
        - PhiT - porosity (must be effective); Using PoroT (Total Porosity will lead to SwArchiePhit)
        - a - tortuosity factor
        - m - cementation exponent
        - n - saturation exponent
        - F - formation factor
        *Returns:
         - archieT - water saturation from Archie eq. using total porosity
        '''
        F = a / (PhiT**m)
        archieT = (F * Rw/Rt)**n
        return archieT

def ratio(Rw, Rt, Rmf, Rxo):
        '''
        ratio(rw, rt, rmf, rxo)
        *Input parameters:
         - rw - water resistivity at formation temperature
         - rt - true resistivity 
         - rmf - mud filtrate resistivity at formation temperature
         - rxo - flushed zone resistivity
        *Returns:
         - SwRatio - water saturation from ratio method 
        '''
        swRatio = ((Rxo/Rt) / (Rmf/Rw)) ** (5/8)
        return swRatio
