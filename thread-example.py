import _thread as td
import time

max_loop = 5
num_thread = 0

def task(task_name, delay): 
  global max_loop, num_thread
  num_thread += 1

  ct = 0
  while ct < max_loop:
    time.sleep(delay)
    print("Thread: %s" % (task_name))
    ct += 1
  
  num_thread -= 1

td.start_new_thread(task, ("Tarefa 1", 2))
td.start_new_thread(task, ("Tarefa 2", 4))

print(num_thread)

while num_thread > 0:
  pass