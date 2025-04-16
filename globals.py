# 公共变量
missing_ratios=[0.1,0.2,0.3]
# missing_ratios=[0.4,0.5,0.6,0.7,0.8]
# missing_ratios=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]

models=["PMILD", "KNN","Mean","Mode", "MICE", "MissForest", "GAIN", "MIWAE","MVIIL_GAIN"]
# models=["PMILD", "KNN","Mean","Mode", "MICE", "MissForest", "GAIN", "MIWAE"]

datasets=["CCA","german","Japanese","LCC","PaiPaiDai","Prosper","Renrendai","Stock","Taiwann","CustomerBehavior","HealthCare"] #
lu_missforest_datasets=["CCA","german","Japanese","Prosper","Stock"]
zhuo_missforest_datasets=["LCC","PaiPaiDai","Renrendai"] #,"Taiwann"
datasets_types={
    "CCA":{'cont': list(range(3)),'ord': list(range(3, 10)),'bin': list(range(10, 14))},
    "german":{'ord': list(range(0, 18)), 'bin': [18, 19]},
    "Japanese":{'cont': list(range(6)), 'ord': [7, 8, 9, 10, 14], 'bin': [6, 11, 12, 13]},
    "LCC":{'cont': list(range(11)),'ord': list(range(11, 26)),'bin': list(range(26, 28))},
    "PaiPaiDai":{'cont': list(range(11)),'ord': list(range(11, 24)),'bin': list(range(24, 32))},
    "Prosper":{'cont':list(range(8)),'ord':list(range(8,29)),'bin':list(range(29, 30))},
    'Renrendai':{'cont':[0],'ord':list(range(1,13))},
    "Stock":{'cont': list(range(12)),'ord': list(range(12, 16))},
    # "Stock":{'cont': list(range(16))},
    "Taiwann":{'ord': list(range(0, 23))}
}

datasets_names = {
    "CCA": "CCA.csv",
    "german": "german.csv",
    "Japanese": "Japanese.csv",
    "LCC": "LCC.csv",
    "PaiPaiDai": "PaiPaiDai.csv",
    "Prosper": "Prosper.csv",
    "Renrendai": "Renrendai.csv",
    "Stock": "Stock.csv",
    "Taiwann": "Taiwann.csv",
    "CustomerBehavior":"CustomerBehavior.csv",
    "HealthCare":"HealthCare.csv"
}
label_datasets = ["CCA", "german", "Japanese", "LCC", "Prosper", "Renrendai","Taiwann","HealthCare"] #, "Taiwann"
# label_datasets = ["Japanese"]
unlabel_datasets = ["PaiPaiDai", "Stock","CustomerBehavior"]

iterations=100
# GAIN参数
gain_parameters = {'batch_size': 128, 'hint_rate': 0.9,'alpha': 100,'iterations': iterations}

final_datasets_types={
    "Australia":{'cont': list(range(3)),'ord': list(range(3, 10)),'bin': list(range(10, 14))},
    "German":{'ord': list(range(0, 18)), 'bin': [18, 19]},
    "Japanese":{'cont': list(range(6)), 'ord': [7, 8, 9, 10, 14], 'bin': [6, 11, 12, 13]},
    "LendingClub":{'cont': list(range(11)),'ord': list(range(11, 26)),'bin': list(range(26, 28))},
    "PaiPaiDai":{'cont': list(range(11)),'ord': list(range(11, 24)),'bin': list(range(24, 32))},
    "Prosper":{'cont':list(range(8)),'ord':list(range(8,29)),'bin':list(range(29, 30))},
    'RenRenDai':{'cont':[0],'ord':list(range(1,13))},
    "Stock":{'cont': list(range(12)),'ord': list(range(12, 16))},
    # "Stock":{'cont': list(range(16))},
    "Taiwan":{'ord': list(range(0, 23))},
    "CustomerBehavior":{'cont':list(range(2,8)),'ord':[1],'bin':[0]},
    "HealthCare":{'cont':[0,3,4,7,9],'ord':[2,6,10,11,12],'bin':[1,5,8]}
}