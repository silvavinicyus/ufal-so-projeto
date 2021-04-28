import os
import platform
from multiprocessing import Pool

system = platform.system()

if (system.lower() == "linux"):
  processos = ('google-chrome', 'clear')
else:
  processos = ('start chrome', '')

def run_process(processo):  
  os.system(processo)

if __name__ == '__main__':
  pool = Pool(processes=2)
  pool.map(run_process, processos)
