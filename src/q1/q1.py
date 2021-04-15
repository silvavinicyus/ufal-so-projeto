import os
from multiprocessing import Pool

processos = ('main.py', 'main2.py')

def run_process(processo):
  os.system("python3 {}".format(processo))


pool = Pool(processes=2)
pool.map(run_process, processos)