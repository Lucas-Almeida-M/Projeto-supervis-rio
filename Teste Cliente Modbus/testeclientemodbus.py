from pyModbusTCP.client import ModbusClient
import random as random
from time import sleep

####################################################################################################
###### Este script pode ser usado para simular a conexão com o clp enviando dados aleatórios #######
####################################################################################################


client = ModbusClient(host="127.0.0.1", port=505)

client.open()

while True:
    client.write_multiple_registers(1000,[random.randrange(150,200),random.randrange(30,40),random.randrange(100,130),random.randrange(2000,2500),random.randrange(1300,1500),random.randrange(1800,2000),random.randrange(4000,5000),random.randrange(4000,5000),random.randrange(1800,2100),random.randrange(400,500),random.randrange(4000,5000),random.randrange(1500,1700),random.randrange(60,75),random.randrange(210,230),random.randrange(210,230),random.randrange(210,230)])
    client.write_multiple_registers(2000,[random.randrange(700,730),random.randrange(700,730),random.randrange(700,730),random.randrange(20,25),random.randrange(20,25),random.randrange(20,25),random.randrange(70,80),random.randrange(58,62),random.randrange(235,245),random.randrange(109,111),random.randrange(7,20),random.randrange(60,75),random.randrange(60,75),random.randrange(210,230),random.randrange(210,230),random.randrange(210,230),random.randrange(30,36),random.randrange(30,36),random.randrange(30,36),random.randrange(70,80),random.randrange(2300,2500)])
    client.write_multiple_registers(3000,[random.randrange(100,150),random.randrange(60,75),random.randrange(200,230),random.randrange(50,58)])
    print(client.read_holding_registers(1000))
    sleep(1)