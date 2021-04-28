from threading import Thread, Lock
import logging

lock = Lock()

saldoA = 500
saldoB = 900

def processo1():    
  lock.acquire()
  logging.info("\nPerformando ações do Processo 1")

  global saldoA, saldoB

  x = saldoA
  x = x - 200
  saldoA = x

  x = saldoB
  x = x + 100
  saldoB = x

  logging.info("Saldo após processo 1: ")
  logging.info("Saldo A: %s", saldoA)
  logging.info("Saldo B: %s", saldoB)
  logging.info("Finalizando ações do Processo 1")
  lock.release()

def processo2():  
  lock.acquire()
  logging.info("\nPerformando ações do Processo 2")

  global saldoA, saldoB

  y = saldoA
  y = y-100
  saldoA = y

  y = saldoB
  y = y + 200
  saldoB = y

  logging.info("Saldo após processo 2: ")
  logging.info("Saldo A: %s", saldoA)
  logging.info("Saldo B: %s", saldoB)
  logging.info("Finalizando ações do Processo 2")
  lock.release()  

if __name__ == '__main__':
  format = "%(message)s"
  logging.basicConfig(format=format, level=logging.INFO)
  
  processo1 = Thread(target=processo1, args=())
  processo2 = Thread(target=processo2, args=())

  processo1.start()  
  processo1.join()
  processo2.start()
  processo2.join()

  logging.info("\nSaldos finais: ")
  logging.info("Saldo A: %s", saldoA)
  logging.info("Saldo B: %s", saldoB)