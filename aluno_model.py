import uuid


class Aluno:
    def __init__(self, nome, idade, curso, nota):
        self.matricula = uuid.uuid4()
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota

    def __repr__(self):
        return f"Matricula:{self.matricula}\n"\
            f"Nome: {self.nome}\n"\
            f"Idade: {self.idade}\n"\
            f"Curso: {self.curso}\n"\
            f"Nota: {self.nota}"

if __name__=='__main__':
    a = Aluno('Douglas', 19, 'Python', 10)
    print(a)