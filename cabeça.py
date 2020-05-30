from random import randint

class cabeça:
    lista = []

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

    def movimentacao(lista, posAtual, mover):
        guardar = 0

        if(mover == 'esquerda'):
            if(posAtual != 0 and posAtual != 3 and posAtual != 6):
                guardar = lista[posAtual-1]
                lista[posAtual-1] = 0
                lista[posAtual] = guardar
            else:
                print('Erro')

        elif(mover == 'direita'):
            if(posAtual != 2 and posAtual != 5 and posAtual != 8):
                guardar = lista[posAtual +1]
                lista[posAtual +1] = 0
                lista[posAtual] = guardar
            else:
                print('Erro')

        elif(mover == 'baixo'):
            if(posAtual != 6 and posAtual != 7 and posAtual != 8):
                guardar = lista[posAtual+3]
                lista[posAtual+3] = 0
                lista[posAtual] = guardar
            else:
                print('Erro')

        elif(mover == 'cima'):
            if(posAtual != 0 and posAtual != 1 and posAtual != 2):
                guardar = lista[posAtual-3]
                lista[posAtual-3] = 0
                lista[posAtual] = guardar
            else:
                print('Erro')

        return lista


    def testeDeObjetivo(lista):
        completo = False
        if(lista == [1,2,3,4,5,6,7,8,0]):
            completo =  True
        return completo

    def imprime(lista):
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

    

    inicio(lista)

    completou = False
    lugar = 0
    while(completou == False):
        
        imprime(lista)
        lugar = lista.index(0)
        mover = input('esquerda, direita, cima, baixo ou terminar: ')
        if(mover == 'terminar'):
            break
        movimentacao(lista, lugar, mover)
        
        completou = testeDeObjetivo(lista)

    if(completou == True):
        print('Parabens, quebra cabeça completo')
    else:
        print('Programa terminado')