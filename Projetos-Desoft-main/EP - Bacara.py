#EP - Design de Software
#Equipe: Larissa Jordana de Paula Soares
#Data: 18/10/2020
# Sou foda
# O jogo consiste em partidas onde pode apostar se o jogador ou o banco sonseguem um soma de cartas mais próxima do 9.
# NÃO É UMA DISPUTA
# A aposta é para o jogador ou banco ESSA É A ÚNICA INTERAÇÃO QUE O JOGADOR VAI TER, QUE É APOSTAR EM QUEM ERA VENCER A PARTIDA
#(JOGADOR, BANCO OU EMPATE)
# Todo resto do jogo é realizado pela mesa, mas com regras.
# Regras que tem que ter no jogo:
# APOSTA TEM QUE SER COM NÚMEROS INTEIROS POSITIVOS DE FICHAS.
# O JOGADOR COMECARÁ COM A QUANTIDADE DE FICHAS QUE EU QUISER
# O JOGADOR APOSTA EM QUEM VAI VENCER (JOGADOR, BANCO OU EMPATE)
# APARTIR DAÍ A MESA REALIZARÁ TODO O RESTO DO JOGO AUTOMATICAMENTE.
# É UTILIZADO O BARALHO COMPLETO COM 52 CARTAS.
#INICIALMENTE A MESA EMBARALHA AS CARTAS E DISTRIBUI DUAS PARA O JOGADOR E O BANCO.
# SE A SOMA DAS CARTAS DO JOGADOR OU BANCO FOR IGUAL A 8 OU 9 O JOGADOR TERMINA E AS APOSTAS SÃO PAGAS.

# Primeiro passo criar variáveis:
import random
#Váriaveis para fichas e
Fichas= 100
pergunta3 = True

print ('você começa com:{0} fichas'.format(Fichas)) 
# while está em loop para que o jogo não pare, até que o jogador peça ou perca.
while Fichas > 0 and pergunta3: 
    
    pergunta=int(input('Qual é o valor da aposta?'))


    while pergunta>Fichas or pergunta <= 0:
        pergunta=int(input('Qual é valor da aposta?'))

    pergunta2=input('Em quem você vai apostar? (Banco, Jogador, Empate)')

    while pergunta2 != 'Banco'and pergunta2 != 'Jogador'and pergunta2 != 'Empate':
        pergunta2=input('Em quem você vai apostar? (Banco, Jogador, Empate)') 

    cartas=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]*8
    random.shuffle(cartas)

    Banco=[]
    Jogador=[]

    Banco.append(cartas[0])
    Banco.append(cartas[1])
    Jogador.append(cartas[2])
    Jogador.append(cartas[3])

    soma_banco=sum(Banco)
    soma_jogador=sum(Jogador)

    print(soma_banco,soma_jogador) #Apagar

    s_b=str(soma_banco) #s_b é uma variação que recebe a soma banco como uma string

    if soma_banco >= 10:
        B=s_b[1]
    elif soma_banco < 10:
        B=s_b[0]


    s_j=str(soma_jogador)
    if soma_jogador >= 10:
        J=s_j[1]
    else:
        J=s_j[0]

    print (B,J)#Apagar

    if B != '8' and B !='9' and J != '8' and J!='9':
        
        if B <= '5':
            Banco.append(cartas[4])
            soma_banco=sum(Banco)
            s_b=str(soma_banco)
            
            if soma_banco >= 10:
            
                B=s_b[1]
            
            elif soma_banco < 10:
            
                B=s_b[0]
        else:
            B=s_b[0]
    else:
        None

    if J != '8' and J !='9' and B != '8' and B!='9':
        if J <='5':
            Jogador.append(cartas[5])
            soma_jogador=sum(Jogador)
            s_j=str(soma_jogador)

            if soma_jogador >= 10:
                J=s_j[1]
            else:
                J=s_j[0]
        else:
            J=s_j[0]
    else:
        None

    print(B,J) #apagar

    if B > J:
        print ('Banco Ganhou')
        if pergunta2 == 'Banco':
            Fichas += (95/100)*pergunta
            N_Fichas=int(Fichas)
            print('Você venceu a aposta e possui agora {0}'.format(N_Fichas))
        else:
            Fichas -= pergunta
            N_Fichas=int(Fichas)
            print('Você perdeu a aposta e possui agora {0}'.format(N_Fichas))

    elif B < J:
        print('Jogador ganhou')
        if pergunta2 == 'Jogador':
            Fichas += pergunta
            N_Fichas=int(Fichas)
            print('Você venceu a aposta e possui agora {0}'.format(N_Fichas))
        else:
            Fichas -= pergunta
            N_Fichas=int(Fichas)
            print('Você perdeu a aposta e possui agora {0}'.format(N_Fichas))

    else:
        print('Deu Empate')
        if pergunta2 == 'Empate':
            Fichas += 8*pergunta
            N_Fichas=int(Fichas)
            print('Você venceu a aposta e possui agora {0}'.format(N_Fichas))
        else:
            Fichas -= pergunta
            N_Fichas=int(Fichas)
            print('Você perdeu a aposta e possui agora {0}'.format(N_Fichas))

    if N_Fichas <= 0:
        print('Você perdeu o jogo, mais sorte na próxima vez')
    else:
        pergunta3=input('Quer continuar jogando?(Sim ou Não)')
        while pergunta3 != 'Sim' and pergunta3 != 'Não':
            pergunta3 = input ( 'Não entendi sua resposta. Quer continuar jogando?(Sim ou Não)')
        if pergunta3 == 'Sim':
            pergunta3 = True

        elif pergunta3 == 'Não':
            pergunta3 = False
            print ('Xau, Xau, até a próxima vez')
            



    










