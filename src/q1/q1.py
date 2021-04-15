import os
import platform
from multiprocessing import Pool

system = platform.system()

if (system.lower() == "linux"):
  processos = ('google-chrome', 'clear')
else:
  processos = ('start chrome', 'cls')

def run_process(processo):  
  os.system(processo)


pool = Pool(processes=1)
pool.map(run_process, processos)