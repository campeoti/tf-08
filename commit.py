# Histórico de commits do Git transformado em objetos.
# Rodar no terminal: python3 commit.py
#
# Cada commit sabe qual commit veio antes dele (o pai). Indo de pai em pai
# chegamos no primeiro commit do projeto, que é o caminho que o git log faz.


# Um commit é um registro com número, mensagem e autor, ligado ao commit
# anterior. O primeiro commit do projeto não tem pai, por isso pai começa
# como None.
class Commit:
    def __init__(self, id, mensagem, autor, pai=None):
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    # Imprime este commit e depois pede para o pai imprimir o dele.
    # Cada pai faz o mesmo com o seu pai, até chegar no commit sem pai,
    # que é onde a recursão para.
    def historico(self):
        print("#" + str(self.id) + " " + self.mensagem + " (" + self.autor + ")")
        if self.pai is None:
            return
        self.pai.historico()


# O repositório guarda o nome do projeto, o autor e o head, que aponta para
# o commit mais recente. Ele também conta quantos commits já criou, para dar
# um número diferente a cada um.
class Repositorio:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador_de_commits = 0

    # Cria um commit novo em cima do head atual. O contador sobe antes, então
    # o primeiro commit recebe o id 1. O commit novo passa a ser o head e o
    # antigo head vira o pai dele. Não devolve nada.
    def commitar(self, mensagem):
        self.contador_de_commits = self.contador_de_commits + 1
        self.head = Commit(self.contador_de_commits, mensagem, self.autor, self.head)

    # Mostra os commits do mais novo para o mais antigo, começando pelo head.
    # Sem nenhum commit ainda, só avisa e sai.
    def log(self):
        if self.head is None:
            print("Nenhum commit ainda")
            return
        self.head.historico()

    # Conta os commits andando do head até o primeiro, de pai em pai.
    # Quando o commit atual vira None, passamos do primeiro e acabou.
    def total_de_commits(self):
        total = 0
        commit_atual = self.head
        while commit_atual is not None:
            total = total + 1
            commit_atual = commit_atual.pai
        return total
