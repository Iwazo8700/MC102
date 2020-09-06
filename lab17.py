#nome: Enzo Hideki Iwata
#RA: 215394
import re
class EmailInvalido(Exception):
    pass

class SenhaFraca(Exception):
    pass

class RAInvalido(Exception):
    pass
def senha_invalida(senha):#função para verificar a senha
    if len(senha) < 8:#confere tamanho
        raise SenhaFraca()
    numero = re.findall(r'\d+', senha)
    numero = "".join(numero)
    if len(numero) < 2:#confere quantidade de numeros
        raise SenhaFraco()
    minusculo = re.findall(r'[a-z]+', senha)
    minusculo = "".join(minusculo)
    if len(minusculo) < 2:#confere quantidade de minusculos
        raise SenhaFraca()
    maiusculo = re.findall(r'[A-Z]+', senha)
    maiusculo = ''.join(maiusculo)
    if len(maiusculo) == 0:#confere quantidade de maiusculos
        raise SenhaFraca()
    caractere = re.findall(r'[!@#$&*]+', senha)
    caractere = "".join(caractere)
    if len(caractere) == 0:#confere caracters
        raise SenhaFraca()
def email_invalido(email):#função para verificar email invalido
    sla = re.findall(r'[a-zA-Z0-9\+\-\.\_]+@\w+\.\w\w\w?\w?', email)
    sla = "".join(sla)
    if not sla == email:#se o email conrresponder o sla vai ser igual ao email
        raise EmailInvalido
class Repositorio:
    def __init__(self):
        self.alunos = []
    #Este método recebe o parâmetro aluno e o insere no repositório
    def adicionar(self, aluno):
        for one in range(len(self.alunos)):#confere se não tem nenhum ra igual
            if self.alunos[one].ra == aluno.ra:
                raise RAInvalido()
        senha_invalida(aluno.senha)
        email_invalido(aluno.email)
        self.alunos.append(aluno)#caso não haja erro ele adiciona no repositorio
    #Este método recebe o parâmetro aluno e altera, no repositório, os dados do aluno com RA igual a aluno.ra
    def alterar(self, aluno):
        luffy = True
        for fruta in range(len(self.alunos)):#se tiver ra igual ele altera o aluno
            if self.alunos[fruta].ra == aluno.ra:
                self.alunos[fruta] = aluno
                luffy = False
                break
        if luffy:
            raise RAInvalido()
        senha_invalida(aluno.senha)
        email_invalido(aluno.email)

    #Este método recebe o parâmetro ra e deve retornar o aluno que possui o RA informado como parâmetro
    def achaAluno(self, ra):#acha aluno quando o ra é igual
        luffy = True
        for gomu in range(len(self.alunos)):
            if self.alunos[gomu].ra == ra:
                return self.alunos[gomu]
        if luffy:
            raise RAInvalido()
    #Este método recebe o parâmetro ra e deve remover o aluno correspondente do repositório
    def remover(self, ra):
        luffy = True
        for piece in range(len(self.alunos)):#deleta o aluno quando eleesta no repositorio
            if self.alunos[piece].ra == ra:
                del self.alunos[piece]
                luffy = False
                break
        if luffy:
            raise RAInvalido()
    #Este método exclui todos os alunos do repositório.
    def limparRepositorio(self):
        self.alunos = []#limpa o limparRepositorio
