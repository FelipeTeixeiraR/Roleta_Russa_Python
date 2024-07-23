import random
import os

def limpar_terminal():
    
    # Detecta o sistema operacional
    if os.name == 'nt':  # Se for Windows
        os.system('cls')
    else:  # Se for Unix (Linux ou macOS)
        os.system('clear')
int = bullet = random.randrange(3, 10)
int = vazia = random.randrange(1, bullet)
int = ativa = bullet - vazia
c = 'c'
d = 'd'
vezDeOutro = False
SuaVez = True
int = carga = [c] * ativa + [d] * vazia
random.shuffle(carga)
carregadas = carga.count('c')
descarregadas = carga.count('d')
quantLife = random.randrange(1, 6)
life = quantLife
olife = quantLife
print(f"Exitem: {carregadas} balas carregadas\nE existem:  {descarregadas} balas descarregadas")
print(f"A quantidade de vida desta rodada é:{quantLife}")
while life > 0 and olife > 0:
    if not carga:
        int = bullet = random.randrange(3, 10)
        int = vazia = random.randrange(1, bullet)
        int = ativa = bullet - vazia
        c = 'c'
        d = 'd'
        int = carga = [c] * ativa + [d] * vazia
        random.shuffle(carga)
        carregadas = carga.count('c')
        descarregadas = carga.count('d')
        print(f"Exitem: {carregadas} balas carregadas\nE existem:  {descarregadas} balas descarregadas")
       
    
    escolha = input("Press 1 para atirar em você mesmo: \nPress 2 para atirar no outro:")
    tiro = carga[0]
    if SuaVez == True:
        limpar_terminal()
        print("Sua vez.")
        if escolha == "1" and tiro == "c":
            print("Levou Tiro")
            life = life - 1
            vezDeOutro = True
            print(f"Você tem {life} de vida")
        elif escolha == "2" and tiro == "c":
            print("Deu tiro em outro")
            olife = olife - 1
            print(f"Outro tem {olife} de vida")
        elif escolha == "1" and tiro == "d":
            print("Descarregado")
        elif escolha == "2" and tiro == "d":
            print("Descarregado")
            vezDeOutro = True
        carga.pop(0)
        if life <= 0:
            print("Você ganhou") 
            break
        if olife <=0:
            print("Outro ganhou")
            break
    if vezDeOutro == True:
        limpar_terminal()
        print("Vez de outro.")
        if escolha == "1" and tiro == "c":
            print("Levou Tiro")
            olife = olife - 1
            SuaVez = True
            print(f"Você tem {olife} de vida")
        elif escolha == "2" and tiro == "c":
            print("Deu tiro em Você")
            life = life - 1
            print(f"Você tem {life} de vida")
        elif escolha == "1" and tiro == "d":
            print("Descarregado")
        elif escolha == "2" and tiro == "d":
            print("Descarregado")
            SuaVez = True
