import json

########################################################################################
######  Este script pode ser usado para criar um arquivo de configurações padrão  ######
######  para o supervisório caso haja algum problema com o original               ######
########################################################################################

config = {"ip": "127.0.0.1", "porta": 505, "scan_time": 1000, "casadec": 2, "largcol": 60, 
"tamfont": 13, "ccylim": 80, "ctylim": 800, "ctemplim": 100, "cxlim": 100, "tvylim": 250, 
"tpylim": 30, "ttemplim": 600, "txlim": 100, "bcylim": 40, "btylim": 80, "btemplim": 100, 
"bxlim": 100, "htorqueylim": 300, "hempylim": 200, "htemplim": 100, "hxlim": 100}

with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=4)