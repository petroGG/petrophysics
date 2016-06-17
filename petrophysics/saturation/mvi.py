'''
List of functions:
sw_sxo - movable hydrocarbon index
swr - movable hydrocarbon index
bvw - bulk volume of water
'''

def sw_sxo(Rxo, Rmf, Rw, Rt):
        '''
        sw/sxo - is called movable hydrocarbon index
        --if sw/sxo ratio is less than 0.7 (ss) or 0.6 (carb), mv hc are present--
        - Rmf - mud filtrate resistivity @ formation temperature
        - Rxo - shallow resistivity (from LL8, MSFL, ML)
        - Rw - water resistivity
        - Rt - true resistivity
        '''
        sw_sxo = (Rxo/Rmf * Rw/Rt)**(1/2)
        return sw_sxo

def swr(Rxo, Rmf, Rw, Rt):
        '''
        swr - movable hydrocarbon index
        0.625 or 5/8 - works well for moderate invasion
        then sxo=sw^(1/5) and results: swr = ....
        - Rmf - mud filtrate resistivity @ formation temperature
        - Rxo - shallow resistivity (from LL8, MSFL, ML)
        - Rw - water resistivity
        - Rt - true resistivity
        '''
        swr = (Rxo/Rmf * Rw/Rt)**(0.625)
        return swr

#BVW

def bvw(sw,phi):
        bvw = sw * phi
        return bvw
