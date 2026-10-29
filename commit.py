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
