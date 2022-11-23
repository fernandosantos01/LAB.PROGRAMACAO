import random
import sys

#acertou = False

contador_para_chances = 0

contador_para_resultado = 0


numero_secreto = random.randint(1,100)

nome_usuario = input("Qual o seu nome?\n")

nivel = input("Qual o nivel?\n")

nivel_do_jogo = int (nivel)

if(nivel_do_jogo == 1):
  tentativas = 3
  if(nivel_do_jogo == 2):
    tentativas = 5
    if(nivel_do_jogo == 3):
      tentativas = 6

contador_para_chances = tentativas

for i in range(0,tentativas):

  print(f'Seu numero de chances é {contador_para_chances}')
  contador_para_chances = contador_para_chances -1

  #Serve para contabilizar o numero de chances restantes do usuário
  contador_para_resultado = contador_para_resultado +1
  
#while(acertou not)
  
  palpite_usuario = input("Qual o seu palpite ?")

  #Essa linha de codigo serve para a conversão de string para   tipo inteiro 
  palpite = int(palpite_usuario)

    #A letra 'f' serve para melhorar a formatação
  print(f'O usuario {nome_usuario} deu o palpite {palpite}')
    
  if(palpite == numero_secreto):
    print(f'{nome_usuario} você acertou o número       {numero_secreto}')
    
    sys.exit("Programa encerrado")
    #acertou = True

  else:
    print(f'{nome_usuario} você errou o número secreto!')
    
    #Linha de código comentada a seguir foi ultilizada para fazer o teste do encerramento instataneo
     
    #print(f'{nome_usuario} O numero correto era {numero_secreto}!')
    
    #acertou = False
    
  if(palpite<numero_secreto):
    print(f'{nome_usuario} Você errou pra baixo, Portanto digite um numero maior')

  else:
    print(f'Você errou para cima, Portanto digite um numero menor')

  if(contador_para_resultado==tentativas):
    print(f'{nome_usuario} O numero correto era {numero_secreto}!')
    