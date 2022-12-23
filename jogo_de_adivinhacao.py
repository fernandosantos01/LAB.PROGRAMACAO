import random
import sys
import time

#acertou = False

contador_de_jogadas = 0

contador_para_chances = 0

contador_para_resultado = 0


numero_secreto = random.randint(1,100)

while True:

    print(f'*****Bem vindo ao Jogo de Adivinhação*****\n')
    inicio = time.time()
    nome_usuario = input("Qual o seu nome?\n")

    print('—- Menu de Opções —-')
    nivel = input('F - Fácil\nM - Médio\nD - Difícil\nQual a sua opção?\n')

    nivel_do_jogo = nivel

    if(nivel_do_jogo == "F"):
      tentativas = 10
    if(nivel_do_jogo == "M"):
      tentativas = 5
    if(nivel_do_jogo == "D"):
      tentativas = 3

    contador_para_chances = tentativas

    for i in range(0,tentativas):

      print(f'Seu numero de chances é {contador_para_chances}')
      contador_para_chances = contador_para_chances -1

      #Serve para contabilizar o numero de chances restantes do usuário
      contador_para_resultado = contador_para_resultado +1
      
    #while(acertou not)
      
      palpite_usuario = input("Qual o seu palpite ?\n")

      #Essa linha de codigo serve para a conversão de string para   tipo inteiro 
      palpite = int(palpite_usuario)
      contador_de_jogadas = contador_de_jogadas+1
        #A letra 'f' serve para melhorar a formatação
      print(f'O usuario {nome_usuario} deu o palpite {palpite}')
      if(palpite == numero_secreto):
        print(f'{nome_usuario} você acertou o número {numero_secreto}, a quantidade de jogadas foram {contador_de_jogadas}')
        fim = time.time()
        print ('duracao: %.2f segundos' % (fim - inicio))
        break
        
        #sys.exit("Programa encerrado")
        #acertou = True

      else:
        print(f'{nome_usuario} você errou o número secreto!')

        #teste de resultado
        #print(f'{nome_usuario} O numero correto era {numero_secreto}!')
        
        #acertou = False
        
      if(palpite<numero_secreto):
        print(f'{nome_usuario} Você errou pra baixo, Portanto digite um numero maior')
      if(palpite>numero_secreto):
        print(f'Você errou para cima, Portanto digite um numero menor')
        

      if(contador_para_resultado==tentativas):
        print(f'{nome_usuario} O numero correto era {numero_secreto}!')
      
    opcao = input ("Deseja continuar? [1 - Sim || 2 - Não]\n")
    opc = int(opcao)
    if(opc == 2):
      break