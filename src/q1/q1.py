import os
from multiprocessing import Pool

processos = ('google-chrome', 'clear')

def run_process(processo):
  os.system(processo)


pool = Pool(processes=2)
pool.map(run_process, processos)