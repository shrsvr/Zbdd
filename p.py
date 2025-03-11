import os
os.system("unzip mnu.zip && unzip z.zip")
os.system("chmod +x *")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"bash run.sh")
