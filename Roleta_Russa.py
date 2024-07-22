import random
int = bullet = random.randrange(3, 10)
int = vazia = random.randrange(1, bullet)
int = ativa = bullet - vazia
c = 'c'
d = 'd'
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
    if escolha == "1" and tiro == "c":
        print("Levou Tiro")
        life = life - 1
        print(f"Você tem {life} de vida")
    elif escolha == "2" and tiro == "c":
        print("Deu tiro em outro")
        olife = olife - 1
        print(f"Outro tem {olife} de vida")
    elif escolha == "1" and tiro == "d":
        print("Descarregado")
    elif escolha == "2" and tiro == "d":
        print("Descarregado")
    carga.pop(0)
    if life <= 0:
        print("Você ganhou") 
        break
    if olife <=0:
        print("Outro ganhou")
        break
    
    
    
    
    





print(carga)
print(bullet)
print(vazia)
print(ativa)
