import time
import json
import random
import socket

# Data generation parameters
N_ATHLETES = 2
N_DATA = -1     # -1 for infinite amount
TIMEOUT = 5     # time between two new data generation

# TCP/IP communication
HOST = "logstash"
PORT = 5044
N_TENTATIVES = 10

# Fonction de génération aléatoire de données
def generate_data(athlete_id: int = 1):
    return json.dumps({
        "athlete_id": athlete_id,
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        "heart_rate": random.randint(120, 180),
        "oxygen_saturation": random.randint(90, 100)
    })

# Wait for Logstash to start
tentative_count = 0
while tentative_count < N_TENTATIVES:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        print("Connected successfully to Logstash")
        break
    except Exception as e:
        print(f"Still waiting for Logstash... (try {tentative_count + 1} out of {N_TENTATIVES})")
        time.sleep(5)
if tentative_count >= N_TENTATIVES:
    raise InterruptedError(f"Connection to Logstash failed after {tentative_count} tries.")

# Sending data
with s:
    count = 0
    need_data = True

    # Envoyer des données toutes les 10 secondes
    while need_data:
        for id in range(N_ATHLETES):
            data = generate_data(athlete_id=id+1)
            s.sendall((data + "\n").encode())  # Envoi des données au stdin de Logstash
        time.sleep(TIMEOUT)  # Pause de 5 secondes

        if N_DATA != -1:
            count += 1
            if count > N_DATA:
                need_data = False
