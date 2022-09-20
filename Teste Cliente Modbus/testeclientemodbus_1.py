from pyModbusTCP.client import ModbusClient
import random as random
from time import sleep

####################################################################################################
###### Este script pode ser usado para simular a conexão com o clp enviando dados aleatórios #######
####################################################################################################


client = ModbusClient(host="127.0.0.1", port=505)

client.open()

while True:
    client.write_multiple_registers(1000,[random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200)])
    client.write_multiple_registers(2000,[random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200)])
    client.write_multiple_registers(3000,[random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200)])
    print(client.read_holding_registers(1000))
    sleep(1)