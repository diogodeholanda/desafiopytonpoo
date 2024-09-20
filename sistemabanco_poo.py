from abc import ABC, abstractclassmethod, abstractproperty

from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []#contas foi iniciada vazia

    def realizar_transação(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)#adiciona a conta recebida por parâmetro no array de conta


class PessoaFisica(Cliente) :
    def __init__ (self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)#chama o construtor da classe pai
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

