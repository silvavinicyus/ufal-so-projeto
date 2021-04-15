import os
from multiprocessing import Pool

processos = ('processo1.py', 'processo2.py', 'processo3.py')

def run_process(processo):
  os.system("python3 {}".format(processo))


pool = Pool(processes=3)
pool.map(run_process, processos)