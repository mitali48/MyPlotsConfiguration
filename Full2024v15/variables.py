# variables
variables = {}

variables['events'] = {
    'name'  : '1',      
    'range' : (1,0,2),  
    'xaxis' : 'events', 
    'fold'  : 3
}

variables['nvtx'] = {     
    'name'  : 'PV_npvsGood',      
    'range' : (100, 0, 100),  
    'xaxis' : 'number of vertices', 
    'fold'  : 3
}

variables['mll'] = {
    'name': 'mll',    
    'range' : (60,60,120), 
    'xaxis' : 'm_{ll} [GeV]',
    'fold' : 0
}

variables['mth'] = {
    'name': 'mth',
    'range' : (60,0,200),
    'xaxis' : 'm_{T}^{H} [GeV]',
    'fold' : 0
}

variables['mtw1']  = {
    'name': 'mtw1',
    'range' : (50, 0.,100),
    'xaxis' : 'm_{T}^{W_{1}} [GeV]',
    'fold' : 0
}

variables['mtw2']  = {
    'name': 'mtw2',
    'range' : (50, 0.,100),
    'xaxis' : 'm_{T}^{W_{2}} [GeV]',
    'fold' : 0
}

variables['ptll']  = {  
    'name': 'ptll',     
    'range' : (20, 0,200),   
    'xaxis' : 'p_{T}^{ll} [GeV]',
    'fold' : 0
}

variables['drll']  = {
    'name': 'drll',
    'range' : (50, 0,5),
    'xaxis' : '#Delta R_{ll}',
    'fold' : 0
}

variables['dphill']  = {
    'name': 'abs(dphill)',
    'range' : (50, 0,3.15),
    'xaxis' : '#Delta #phi_{ll}',
    'fold' : 0
}

variables['detall'] = {
    'name'  : 'abs(detall)',
    'range' : (40, 0., 5.),
    'xaxis' : '|#Delta#eta_{ll}|',
    'fold'  : 3
}

variables['pt1']  = { 
    'name': 'Lepton_pt[0]',     
    'range' : (20,0,100),
    'xaxis' : 'p_{T} 1st lep',
    'fold'  : 3                         
}

variables['pt2']  = {
    'name': 'Lepton_pt[1]',     
    'range' : (20,0,100),   
    'xaxis' : 'p_{T} 2nd lep',
    'fold'  : 3                         
}

variables['eta1']  = {
    'name': 'Lepton_eta[0]',     
    'range' : (40,-3,3),   
    'xaxis' : '#eta 1st lep',
    'fold'  : 3                         
}

variables['eta2']  = {
    'name': 'Lepton_eta[1]',     
    'range' : (40,-3,3),   
    'xaxis' : '#eta 2nd lep',
    'fold'  : 3                         
}

                        
variables['phi1']  = {
    'name': 'Lepton_phi[0]',
    'range' : (20,-3.2,3.2),
    'xaxis' : '#phi 1st lep',
    'fold'  : 3
}

variables['phi2']  = {
    'name': 'Lepton_phi[1]',
    'range' : (20,-3.2,3.2),
    'xaxis' : '#phi 2nd lep',
    'fold'  : 3
}

# MET
variables['trkMet']  = { 
    'name': 'TkMET_pt',
    'range' : (20,0,200),
    'xaxis' : 'trk met [GeV]',
    'fold' : 3
}

variables['puppimet']  = {
    'name': 'PuppiMET_pt',
    'range' : (20,0,200),
    'xaxis' : 'Puppi MET p_{T} [GeV]',
    'fold' : 3
}

variables['mpmet']  = {
    'name': 'mpmet',
    'range' : (40,0,100),
    'xaxis' : 'Min. proj. MET p_{T} [GeV]',
    'fold' : 3
}

variables['njet']  = {
    'name': 'Sum(CleanJet_pt>30)',
    'range' : (5,0,5),
    'xaxis' : 'Number of jets',
    'fold' : 2
}

variables['jetpt1']  = {
    #'name': 'Alt(CleanJet_pt, 0, -99) - 9999.9*(CleanJet_pt[0]<30)',
    'name': 'Alt(CleanJet_pt, 0, -99)',
    'range' : (40,0,200),
    'xaxis' : 'p_{T} 1st jet',
    'fold' : 0
}

variables['jetpt2']  = {
    #'name': 'Alt(CleanJet_pt, 1, -99)  - 9999.9*(CleanJet_pt[1]<30)',
    'name': 'Alt(CleanJet_pt, 1, -99)',
    'range' : (40,0,200),
    'xaxis' : 'p_{T} 2nd jet',
    'fold' : 0
}

variables['jeteta1']  = {
    #'name': 'Alt(CleanJet_eta, 0, -99) - 9999.9*(CleanJet_pt[0]<30)',
    'name': 'Alt(CleanJet_eta, 0, -99)',
    'range' : (30,-4.7,4.7),
    'xaxis' : '#eta 1st jet',
    'fold' : 0
}

variables['jeteta2']  = {
    #'name': 'Alt(CleanJet_eta, 1, -99) - 9999.9*(CleanJet_pt[1]<30)',
    'name': 'Alt(CleanJet_eta, 1, -99)',
    'range' : (30,-4.7,4.7),
    'xaxis' : '#eta 2nd jet',
    'fold' : 0
}


"""
###### Nº b-jets

btagging_WPs = {
    "DeepFlavB" : {
        "loose"    : "0.0480",
        "medium"   : "0.2435",
        "tight"    : "0.6563",
        "xtight"   : "0.7671",
        "xxtight"  : "0.9483",
    },
    "UParTAK4B" : {
        "loose"    : "0.0683",
        "medium"   : "0.3494",
        "tight"    : "0.7994",
        "xtight"   : "0.8877",
        "xxtight"  : "0.9883",
    },
    "PNetB" : {
        "loose"    : "0.0359",
        "medium"   : "0.1919",
        "tight"    : "0.6133",
        "xtight"   : "0.7544",
        "xxtight"  : "0.9688",
    }
}
btagging_SFs = {
    "DeepFlavB"      : "deepjet",
    "UParTAK4B"      : "UnifiedParT",
    "PNetB"          : "partNet",
}

for bAlgo in btagging_SFs.keys():

    bWP = btagging_WPs[bAlgo]["loose"]
    
    variables[f'nbjet_{bAlgo}']  = {
        'name': f'Sum(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Take(Jet_btag{bAlgo}, CleanJet_jetIdx) > {bWP})',
        'range' : (5,0,5),
        'xaxis' : f'Number of b-jets ({bAlgo})',
        'fold' : 2
    }
"""
