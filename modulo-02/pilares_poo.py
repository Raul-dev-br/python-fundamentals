# Aqui vem a primeira característica POO
# HERANÇA + POLIMORFISMO- Exemplo
class Animal:
  def __init__(self, nome):
    self.nome = nome
  def emitir_som(self):
    pass

class Cachorro(Animal):
  def emitir_som(self):
    return print("Au, Au")

class Gato(Animal):
  def laber(self):
    print("To me labendo, porra!")
  def emitir_som(self):
    return print("Miau, Miau")

class GatoNordestino(Gato):
  def emitir_som(self):
    return print(f"MEAU, MEAU eu sou o gato do {self.nome}")

gato_nordestino = GatoNordestino("Lula")
gato_nordestino.emitir_som()

# ENCAPSULAMENTO - Exemplo
class ContaBancaria:
  def __init__(self, saldo):
    self.__saldo = saldo
  def mostrar_saldo(self):
    return f"O seu saldo bancário é de: {self.__saldo}"
  
  def depositar(self, deposito):
    if deposito > 0:
      self.__saldo += deposito
    else:
      return f"O valor é {deposito} negativo/nulo!"
    
  def sacar(self, saque):
    if saque == "Sextou":
      self.__saldo -= self.__saldo
      return "Sextou! Você sacou tudo."
    elif saque <= self.__saldo:
      return "Saque é maior que o saldo!"
    else:
      self.__saldo -= saque
      return f"Você sacou {saque}! Agora você tem {self.__saldo}"

conta_zezinho = ContaBancaria(100)
print("Zezinho sacou rece eu o decimo terceiro e depositou 1500!")
conta_zezinho.depositar(1500)
print("Zexinho ficou feliz e sacou tudo o que tinha pra tomar cachaça e comer muié!")
conta_zezinho.sacar("Sextou")
print(f"Zezinho foi ver no outro dia e descobriu que tinha: {conta_zezinho.mostrar_saldo()}")

# ABSTRAÇÃO - Exemplo
from abc import ABC, abstractmethod

class Veiculo(ABC):
  @abstractmethod
  def ligar(self):
    pass
  @abstractmethod
  def desligando(self):
    pass

class Carro(Veiculo):
  def __init__(self, tipo):
    self.tipo = tipo
  def ligar(self):
    if self.tipo == "monza":
      return "Ligando Poçante de Velho Cuiudo!"
    elif self.tipo == "byd":
      return "Eu to dou a bunda. Ligando BYD!"
    return "Ligando Poçante!"
  def desligando(self):
    return "Desligando Poçante"

monza_do_seu_ze = Carro("monza")
print("O seu zé ligou o carro!")
print(monza_do_seu_ze.ligar())