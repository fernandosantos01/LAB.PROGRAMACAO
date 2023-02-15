class Disciplina:
    def __init__(self, codigo, nome, semestre, professores=None, alunos=None, carga_horaria=0, dias_horarios=None):
        self.codigo = codigo
        self.nome = nome
        self.semestre = semestre
        self.professores = professores or []
        self.alunos = alunos or []
        self.carga_horaria = carga_horaria
        self.dias_horarios = dias_horarios or []

class Professor:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

class Aluno:
    def __init__(self, matricula, nome, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso

class MiniControleAcademico:
    def __init__(self):
        self.disciplinas = []
        self.professores = []
        self.alunos = []

    def cadastrar_disciplina(self):
        codigo = int(input("Código da disciplina: "))
        nome = input("Nome da disciplina: ")
        semestre = input("Semestre: ")
        carga_horaria = int(input("Carga horária: "))
        dias_horarios = input("Dias e horários: ")
        disciplina = Disciplina(codigo, nome, semestre, carga_horaria=carga_horaria, dias_horarios=dias_horarios)
        self.disciplinas.append(disciplina)
        print("Disciplina cadastrada com sucesso!")

    def pesquisar_disciplina(self):
        codigo = int(input("Código da disciplina: "))
        for disciplina in self.disciplinas:
            if disciplina.codigo == codigo:
                print("Código: ", disciplina.codigo)
                print("Nome: ", disciplina.nome)
                print("Semestre: ", disciplina.semestre)
                print("Professores: ", disciplina.professores)
                print("Carga horária: ", disciplina.carga_horaria)
                print("Dias e horários: ", disciplina.dias_horarios)
                return
        print("Disciplina não encontrada.")

    def listar_disciplinas(self):
        for disciplina in self.disciplinas:
            print("Código: ", disciplina.codigo)
            print("Nome: ", disciplina.nome)

    def cadastrar_professor_disciplina(self):
        codigo_disciplina = int(input("Código da disciplina: "))
        for discipl
