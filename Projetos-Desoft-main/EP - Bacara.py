#EP - Design de Software
#Equipe: Larissa Jordana de Paula Soares
#Data: 18/10/2020

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

import random
#Váriaveis para fichas e pergunta3 
Fichas= 100
pergunta3 = True

print ('você começa com:{0} fichas'.format(Fichas)) 
# while está em loop para que o jogo não pare, até que o jogador peça ou zere sua fichas.
while Fichas > 0 and pergunta3: 
    
    baralhos = int(input('Quantos baralhos serão utilizados entre 1, 6 ou 8? '))

    pergunta=int(input('Qual é o valor da aposta?'))
   # Verificação se o valor da aposta é maior que Fichas ou se o valor é menor ou igual a zero.
    while pergunta>Fichas or pergunta <= 0:
        pergunta=int(input('Qual é valor da aposta?'))

    pergunta2=input('Em quem você vai apostar? (Banco, Jogador, Empate)')
   # Verificação se a aposta será em Banco, Jogador ou Empate.
    while pergunta2 != 'Banco'and pergunta2 != 'Jogador'and pergunta2 != 'Empate':
        pergunta2=input('Em quem você vai apostar? (Banco, Jogador, Empate)') 
    
    cartas=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]*baralhos
    random.shuffle(cartas)
 # listas vazias para colocar as cartas sorteadas.
    Banco=[]
    Jogador=[]
   
    Banco.append(cartas[0])
    Banco.append(cartas[1])
    Jogador.append(cartas[2])
    Jogador.append(cartas[3])

    soma_banco=sum(Banco)
    soma_jogador=sum(Jogador)


    s_b=str(soma_banco) #s_b é uma variação que recebe a soma banco como uma string
  # Caso a soma de banco for maior que dez, será selecionado o segundo termo, se for menor permanecerá o primeiro termo 
    if soma_banco >= 10:
        B=s_b[1]
    elif soma_banco < 10:
        B=s_b[0]

  # Caso a soma de jogador for maior que dez, será selecionado o segundo termo, se for menor permanecerá o primeiro termo 
    s_j=str(soma_jogador)
    if soma_jogador >= 10:
        J=s_j[1]
    else:
        J=s_j[0]

  # Caso as somas deem diferentes de 8 ou 9.
    if B != '8' and B !='9' and J != '8' and J!='9':
        # Se soma for menor ou igual a cinco.
        if B <= '5':
            Banco.append(cartas[4])
            soma_banco=sum(Banco)
            s_b=str(soma_banco)
            # Caso a soma de Banco for maior que dez, será selecionado o segundo termo, se for menor permanecerá o primeiro termo.
            if soma_banco >= 10:
            
                B=s_b[1]
            
            elif soma_banco < 10:
            
                B=s_b[0]
        else:
            B=s_b[0]
    else:
        None
  # Caso as somas deem diferentes de 8 ou 9.
    if J != '8' and J !='9' and B != '8' and B!='9':
        # Se soma for menor ou igual a cinco.
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

  # Se a soma de Banco for Maior que Jogador.
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
  # Se a soma de Banco for Menor que Jogador.
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
  # Se não for Maior e nem Menor.
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
  # Se o valor total de fichas no final da partida for Menor ou Igual a Zero.
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
            



    










