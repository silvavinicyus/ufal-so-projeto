from threading import Thread, Lock
import logging

lock = Lock()

saldoA = 500
saldoB = 900

def processo1():  
  lock.acquire()

  global saldoA, saldoB

  x = saldoA
  x = x - 200
  saldoA = x

  x = saldoB
  x = x + 100
  saldoB = x

  lock.release()

def processo2():
  lock.acquire()

  global saldoA, saldoB

  y = saldoA
  y = y-100
  saldoA = y

  y = saldoB
  y = y + 200
  saldoB = y

  lock.release()  

if __name__ == '__main__':
  format = "%(message)s"
  logging.basicConfig(format=format, level=logging.INFO)
  
  processo1 = Thread(target=processo1, args=())
  processo2 = Thread(target=processo2, args=())

  processo1.start()  
  processo2.start()
  processo1.join()
  processo2.join()

  logging.info("Saldo A: %s", saldoA)
  logging.info("Saldo b: %s", saldoB)