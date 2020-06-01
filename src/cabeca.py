from random import randint

lista = [0,1,2,8,7,3,6,5,4]



def inicio(lista):
        for i in range(0, 9):
            torio = randint(0,8)
            if(i == 0):
                lista.append(torio)
            else:
                while (torio in lista):
                    torio = randint(0,8)
                lista.append(torio)
        return lista

def calcularDistancia(lista, lugarEstado, direcao):
    copiaLista = lista.copy()
    lugar = copiaLista.index(0)
    lugarObjeto = copiaLista.index(lugarEstado)

    if(lugarObjeto+1 != lugarEstado):
    
        movimentacao(copiaLista, lugar, direcao)

        indice = copiaLista.index(lugarEstado)
        indice = indice +1
        conta = 0


        while(indice != lugarEstado):

            if(abs(indice - lugarEstado) < 3):
                if(lugarEstado == 4 or lugarEstado == 7):
                    if(lugarEstado == 7 and indice < 7):
                        conta = conta + (conta +3)
                        indice = lugarEstado
                    else:
                        conta = conta + abs(indice - lugarEstado)
                        indice = lugarEstado
                else:
                    if(indice < lugarEstado):
                        indice = indice + 1
                        conta = conta +1
                    elif(indice > lugarEstado):
                        indice = indice -1
                        conta = conta +1

            elif(indice < lugarEstado):
                indice = indice +3
                conta = conta +1
                #print('indice: ', indice, ' conta: ', conta)
            elif(indice > lugarEstado):
                indice = indice -3
                conta = conta +1
                #print('3')
        #print('Na distancia:' , conta)
        return conta
    else:
        return 20

        

def autoResolucao(lista, lugar): 

    distancias = []
    direcao = []

    if(lugar != 6 and lugar != 7 and lugar != 8): # pode ir pra baixo
        baixo = lista[lugar+3]
        distancias.append(calcularDistancia(lista, baixo, 's'))
        print('baixo: ', baixo)
        direcao.append('s')

    if(lugar != 0 and lugar != 1 and lugar != 2): # pode ir pra cima
        cima = lista[lugar-3]
        distancias.append(calcularDistancia(lista, cima, 'w'))
        print('cima: ', cima)
        direcao.append('w')

    if(lugar != 2 and lugar != 5 and lugar != 8): # pode ir para direita
        direita = lista[lugar+1]
        distancias.append(calcularDistancia(lista, direita, 'd'))
        print('direita: ', direita)
        direcao.append('d')

    if(lugar != 0 and lugar != 3 and lugar != 6): # pode ir pra esquerda
        esquerda = lista[lugar-1]
        distancias.append(calcularDistancia(lista, esquerda, 'a'))
        print('esquerda: ', esquerda)
        direcao.append('a')

    menor = 10
    for i in range(0, len(distancias)):

        print(direcao[i], ' ', distancias[i])

        if(distancias[i] < menor):
            menor = distancias[i]
    menor = distancias.index(menor)
    mover = direcao[menor]

    movimentacao(lista, lugar, mover)
    imprime(lista)



def movimentacao(lista, posAtual, mover):
        guardar = 0

        if(mover == 'a'):
            if(posAtual != 0 and posAtual != 3 and posAtual != 6):
                guardar = lista[posAtual-1]
                lista[posAtual-1] = 0
                lista[posAtual] = guardar
            else:
                print('Erro')

        elif(mover == 'd'):
            if(posAtual != 2 and posAtual != 5 and posAtual != 8):
                guardar = lista[posAtual +1]
                lista[posAtual +1] = 0
                lista[posAtual] = guardar
            else:
                print('Erro')

        elif(mover == 's'):
            if(posAtual != 6 and posAtual != 7 and posAtual != 8):
                guardar = lista[posAtual+3]
                lista[posAtual+3] = 0
                lista[posAtual] = guardar
            else:
                print('Erro')

        elif(mover == 'w'):
            if(posAtual != 0 and posAtual != 1 and posAtual != 2):
                guardar = lista[posAtual-3]
                lista[posAtual-3] = 0
                lista[posAtual] = guardar
            else:
                print('Erro')

        return lista


def deuLoop(lista, lugar):
    
    direcao = []

    if(lugar != 6 and lugar != 7 and lugar != 8): # pode ir pra cima
        direcao.append('s')

    if(lugar != 0 and lugar != 1 and lugar != 2): # pode ir pra baixo
        direcao.append('w')

    if(lugar != 2 and lugar != 5 and lugar != 8): # pode ir para direita
        direcao.append('d')

    if(lugar != 0 and lugar != 3 and lugar != 6): # pode ir pra esquerda
        direcao.append('a')
    

    moverAleatorio = randint(0 ,len(direcao)-1)
    imprime(lista)
    print('posso ir para: ', direcao)
    print('Direção: ', direcao[moverAleatorio])
    movimentacao(lista, lugar, direcao[moverAleatorio])
    
    imprime(lista)
    return lista
    




def testeDeObjetivo(lista):
        completo = False
        if(lista == [1,2,3,4,5,6,7,8,0]):
            completo =  True
        return completo

def imprime(lista):
    print('\n---------------------------')
    for i in range(0, len(lista)):
        if(i <= 2):
            if(i == 2):
                print(lista[i],'\n')
            else:
                print(lista[i], end = '  ')
        elif(i <= 5):
            if(i == 5):
                print(lista[i],'\n')
            else:
                print(lista[i], end = '  ')
        elif(i <= 8):
            if(i == 8):
                print(lista[i],'\n')
            else:
                print(lista[i], end = '  ')



#inicio(lista)

completou = False
lugar = 0

metodo = input('1 para Auto resolução \n2 para Agente humano \n ')

if(metodo == '1'):
    imprime(lista)
    loop = 0
    copiaUm = lista.copy()

    while(completou == False):
    #for i in range(0, 20):
        lugar = lista.index(0)
    
        if(loop == 2):
            copiaDois = copiaUm.copy()
            copiaUm = lista.copy()

            if(copiaUm == copiaDois):
                deuLoop(lista, lugar)
            loop = 0

        lugar = lista.index(0)
        autoResolucao(lista,lugar)
        #print('Agente inteligete')
        loop = loop +1

elif(metodo == '2'):
    while(completou == False):
            
        imprime(lista)
        lugar = lista.index(0)
        mover = input('esquerda-a, direita-d, cima-w, baixo-s, auto ou terminar: ')
        if(mover == 'terminar'):
            break
        movimentacao(lista, lugar, mover)
            
        completou = testeDeObjetivo(lista)

    if(completou == True):
        print('Parabens, quebra cabeça completo')
    else:
        print('Programa terminado')
        
        
