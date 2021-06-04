import sys, os, json


# 'drug_integrate': whether or not integrating all drug features when constructing input data
# 'drug_indep': whether or not summing features of drug1 and drug2 (False: sum)
method_config_dict = {
    'deepsynergy_preuer_2018':{
        'synergy_data': 'NCI_ALMANAC',
        'cell_data': 'NCI_60',
        'cell_list': 'all',        
        'drug_feats': ['morgan_fingerprint'], 
        'cell_feats': ['exp'], 
        'cell_feat_filter': 'variance',
        'drug_feat_filter': 'target',
        'model_name': 'NN',
        'cell_integrate': True, 
        'drug_integrate': True,
        'drug_indep': False
    },

    'nn_xia_2018':{
        'synergy_data': 'NCI_ALMANAC',
        'cell_data': 'NCI_60',
        'cell_list': 'all',        
        'drug_feats': ['morgan_fingerprint'], 
        'cell_feats': ['exp','mir','pro'], 
        'cell_feat_filter': None,
        'drug_feat_filter': 'target',
        'model_name': 'nn_xia_2018',
        'cell_integrate': False, 
        'drug_integrate': False,
        'drug_indep': True
    },

    'nn_kim_2020':{
        'synergy_data': 'NCI_ALMANAC',
        'cell_data': 'NCI_60',
        'cell_list': 'all',        
        'drug_feats': ['morgan_fingerprint','drug_target'], 
        'cell_feats': ['exp'], 
        'cell_feat_filter': 'variance',
        'drug_feat_filter': 'target',
        'model_name': 'nn_kim_2020',
        'cell_integrate': True,
        'drug_integrate': False,
        'drug_indep': True
    },

    'AuDNNsynergy_zhang_2018':{
        'synergy_data': 'NCI_ALMANAC',
        'cell_data': 'NCI_60',
        'cell_list': 'all',        
        'drug_feats': ['morgan_fingerprint'], 
        'cell_feats': ['exp','mut','cop'], 
        'cell_feat_filter': None,
        'drug_feat_filter': 'target',
        'model_name': 'autoencoder',
        'cell_integrate': False,
        'drug_integrate': True,
        'drug_indep': False
    },

    'ERT_jeon_2018':{
        'synergy_data': 'NCI_ALMANAC',
        'cell_data': 'NCI_60',
        'cell_list': 'all',        
        'drug_feats': ['drug_target','monotherapy'], 
        'cell_feats': ['exp','mut','cop'], 
        'cell_feat_filter': 'cancer',
        'drug_feat_filter': 'target',
        'model_name': 'ERT',
        'cell_integrate': True,
        'drug_integrate': True,
        'drug_indep': False
    },

    'XGBOOST_janizek_2018':{
        'synergy_data': 'NCI_ALMANAC',
        'cell_data': 'NCI_60',
        'cell_list': 'all',        
        'drug_feats': ['morgan_fingerprint'], 
        'cell_feats': ['exp'], 
        'cell_feat_filter': 'variance',
        'drug_feat_filter': 'target',
        'model_name': 'XGBOOST',
        'cell_integrate': True,
        'drug_integrate': True,
        'drug_indep': False
    },

    'XGBOOST_celebi_2019':{
        'synergy_data': 'NCI_ALMANAC',
        'cell_data': 'NCI_60',
        'cell_list': 'all',        
        'drug_feats': ['morgan_fingerprint','drug_target','monotherapy'], 
        'cell_feats': ['exp','mut','cop'], 
        'cell_feat_filter': 'cancer',
        'drug_feat_filter': 'target',
        'model_name': 'XGBOOST',
        'cell_integrate': True,
        'drug_integrate': True,
        'drug_indep': False
    },

    'Logit_li_2020':{
        'synergy_data': 'NCI_ALMANAC',
        'cell_data': 'NCI_60',
        'cell_list': 'all',        
        'drug_feats': ['drug_target'], 
        'cell_feats': ['exp'], 
        'cell_feat_filter': 'variance',
        'drug_feat_filter': 'target',
        'model_name': 'LR',
        'cell_integrate': True,
        'drug_integrate': True,
        'drug_indep': False
    }
}
