'''
List of funtions:
api - converts sg to api
sg - converts api to sg
'''

def api(sg):
    api = 141.5/sg - 131.5
    return api

def sg(api):
    sg = 141.5/(api + 131.5)
    return sg

