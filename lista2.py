import random
import sys

while True:
    vetor_disciplina = []

    print(f'---Mini Controle Acadêmico---')

    opc = int(input('1.Cadastrar Disciplina\n2. Pesquisar disciplina\n3. Listar disciplinas cadastradas\n4. Cadastrar professor em disciplina\n5. Matricular aluno em disciplina\n6. Lançar notas do aluno em uma disciplina\n7. Listar alunos de uma disciplina\n8. Listar notas dos alunos de uma disciplina\n9. Sair\n'))

    if(opc == 1):
        for opcao in opc:
            cod_disciplina = int (input ('Digite o codigo'))
            vetor_disciplina[cod_disciplina].append(cadatrar_disciplina = input('Digite o nome da disciplina'))
            semestre_disciplina = float(input('Digite o semestre'))
            carga_horaria_disciplina = int ( input('Digite a carga horaria'))
            dias_disciplina =  input('Digite os dias da disciplina')
            horarios_disciplina = input('Digite os horarios da disciplina')

