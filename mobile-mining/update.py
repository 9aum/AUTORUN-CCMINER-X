import os
import json
import time
import pip
from config import bannerup
try:
    os.system("@cls||clear")
    bannerup()
    os.system(f"rm -rf AUTORUN-CCMINER-X && cd ../etc/mobile-mining/set-miner && cp -r offline.json online.json /../ && cd ../etc && rm -rf mobile-mining")
    os.system(f"cd ../bin && rm -f edit-miner run-miner add-ip")
    os.system(f"git clone https://github.com/pichetx/AUTORUN-CCMINER-X")
    os.system(f"cd AUTORUN-CCMINER-X/mobile-mining/set-miner && rm -r offline.json online.json")
    os.system(f"mv offline.json online.json /AUTORUN-CCMINER-X/mobile-mining/set-miner")
    os.system(f"cd AUTORUN-CCMINER-X && chmod +x setupate.sh && sh setupdate.sh")
    
    time.sleep(2)
except:
    print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ \033[0m\n\n") 