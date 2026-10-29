# Histórico de commits do Git feito com classes.
# Rodar no terminal: python3 commit.py
#
# Cada commit guarda o commit anterior (o pai). Indo de pai em pai a gente
# chega no primeiro commit, que é o que o git log faz.


# Commit: tem um número, a mensagem, o autor e o pai.
# O primeiro commit não tem pai, por isso o padrão é None.
class Commit:
    def __init__(self, id, mensagem, autor, pai=None):
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    # Imprime este commit e manda o pai imprimir o dele, e assim por diante.
    # Para quando chega no commit que não tem pai.
    def historico(self):
        print("#" + str(self.id) + " " + self.mensagem + " (" + self.autor + ")")
        if self.pai is None:
            return
        self.pai.historico()


# Repositorio: guarda o nome, o autor, o head (último commit feito) e um
# contador que serve para dar um número diferente a cada commit.
class Repositorio:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador_de_commits = 0

    # Soma 1 no contador e cria o commit com esse número. O pai dele é o
    # head atual, e depois o commit novo vira o head. Não retorna nada.
    def commitar(self, mensagem):
        self.contador_de_commits = self.contador_de_commits + 1
        self.head = Commit(self.contador_de_commits, mensagem, self.autor, self.head)

    # Mostra os commits do mais novo pro mais antigo.
    # Se ainda não tem commit, só avisa.
    def log(self):
        if self.head is None:
            print("Nenhum commit ainda")
            return
        self.head.historico()

    # Conta os commits começando no head e indo de pai em pai.
    # Quando chega em None acabaram os commits.
    def total_de_commits(self):
        total = 0
        commit_atual = self.head
        while commit_atual is not None:
            total = total + 1
            commit_atual = commit_atual.pai
        return total


repositorio = Repositorio("lancamento-notas", "Rodrigo Campeoti - 6326012")
repositorio.log()
repositorio.commitar("Cria a tela de cadastro de alunos")
repositorio.commitar("Adiciona o calculo da media final")
repositorio.commitar("Corrige o arredondamento das notas")
repositorio.commitar("Documenta como rodar o projeto")
repositorio.log()
print(repositorio.total_de_commits())
