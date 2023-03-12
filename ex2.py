from threading import Thread
from time import sleep

def cubo(tempo_espera,n):
    Calcular =n**3
    sleep(tempo_espera)
    print(f'\n Calculando o Cubo de {n}...')
    print(f'O cubo de {n} é {Calcular}')

def quadrado(tempo_espera,n):
    Calcular =n**2
    sleep(tempo_espera)
    print(f'\n Calculando o Quadrado de {n}...')
    print(f'O quadrado de {n} é {Calcular}')

print("Iniciando o programa: ")
t1 = Thread(target=cubo,args=(3,5))
#Iniciando a primeira Thread
t1.start()

t2 = Thread(target=quadrado,args=(2,5))
#Iniciando a segunda Thread
t2.start()

#Finalizando as Thread
t1.join()
t2.join()

#FIM
print("\n Finalizando o programa!\n")
