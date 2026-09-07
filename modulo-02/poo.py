# Essa é a primeira vrez que estou tendo contato com a ideia de um linguagem POO
# CLASSE
from datetime import date

class Pessoa:
  def __init__(self, nome, dt_nasc, peso, altura):
    self.nome = nome
    self.data_nasc = dt_nasc
    self.peso = peso
    self.altura = altura

  def saudacao(self):
    print(f"Olá, o meu nome é {self.nome}!")

  def calcular_idade(self):
    dt_atual = date.today()
    dt_nasc = self.data_nasc

    idade = dt_atual.year - dt_nasc.year

    ja_fez_aniversario = (dt_atual.month, dt_atual.day) >= (dt_nasc.month, dt_nasc.day)
    if not ja_fez_aniversario:
      idade = idade - 1
    print(f"Eu tenho {idade} anos de idade")

  def falar_do_peso(self):
    print(f"Eu estou peasando {self.peso} kilos!")

  def falar_da_altura(self):
    print(f"Eu tenho {self.altura:.0f}")

nascimento = date(1900, 9, 6)
mauro = Pessoa("Mauro", nascimento, 100, 190)
mauro.calcular_idade()
mauro.falar_da_altura()