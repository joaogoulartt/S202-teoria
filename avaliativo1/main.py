import pymongo
import threading
import time
import random

# Gerando temperatura
def getTemp():
    return random.uniform(30, 40)

# Gerando e armazenando informação dos sensores no MongoDB
def sensor(sensor_name, exec_time, collection):
    while True:
        temp = getTemp()
        print(f'{sensor_name}: {temp:.2f}°C')
        
        doc = {
            "nomeSensor": sensor_name,
            "valorSensor": temp,
            "unidadeMedida": "°C",
            "sensorAlarmado": False
        }

        collection.replace_one({"nomeSensor": sensor_name}, doc, upsert=True)
        print(f"{sensor_name} adicionado com sucesso!")

        # Sensor alarmed:
        if temp > 38:
            print(f"Atenção! Temperatura muito alta! Verificar {sensor_name}!")
            collection.update_one({"nomeSensor": sensor_name}, {"$set": {"sensorAlarmado": True}})
            print(f"{sensor_name} atualizado com sucesso!")
            break
        else:
            time.sleep(exec_time)

# Criando database e collections:
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["bancoiot"]
collection = db["sensores"]

# Criando threads:
thread1 = threading.Thread(target=sensor, args=("Sensor1", 5, collection))
thread2 = threading.Thread(target=sensor, args=("Sensor2", 10, collection))
thread3 = threading.Thread(target=sensor, args=("Sensor3", 15, collection))

# Iniciando threads:
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

# Apresentando resultados:
results = collection.find()
for info in results:
    print("\n ${info}")
