##############################################################
# O programa representa um Restaurante. O primeiro thread
# representa um cliente que chega faz um pedido.
# O segundo Thread representa o garçom atendendo os clientes.
##############################################################

import time
import random
from threading import Thread, Condition


fila = []
condition = Condition()

class ThreadCliente(Thread):
    def run(self):
        nums = range(15)
        global queue
        while True:
            numero = random.choice(nums)
            condition.acquire()
            fila.append(numero)
            print(f"Cliente {numero} fez um pedido.")
            condition.notify()
            condition.release()
            time.sleep(4) 


class ThreadGarcom(Thread):
    def run(self):
        global fila
        while True:
            condition.acquire()
            if not fila:
                print ("Fila de pedidos vazia, garçom aguardando novos clientes ...")
                condition.wait()
                print ("Novo cliente será atendido")

            numero = fila.pop(0)
            print(f"Cliente {numero} atendido!")
            condition.release()
            time.sleep(4) 


ThreadCliente().start()
ThreadGarcom().start()