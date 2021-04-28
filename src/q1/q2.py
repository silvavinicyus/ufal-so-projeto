import logging
import time
import random
from  threading import Thread

def thread_function(kid, priority):
  logging.info("--------------- Criança %s -----------------------", kid)
  logging.info("Recebeu a bola")
  logging.info("Dominou a bola por %s segundos", priority)
  time.sleep(priority)  
  logging.info("Tocou a bola")

if __name__ == '__main__':
  format = "%(message)s"
  logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
  priorityTime = [8, 3, 5, 4, 1, 1, 2, 3, 4, 2]
  for i in range(0, 10):
    priority = random.choice(priorityTime)
    priorityTime.remove(priority)
    # print(priority)
    x = Thread(target=thread_function, args=(i,priority,))
    x.start()
    x.join()