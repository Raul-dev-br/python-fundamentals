class Animal:
  def __init__(self, nome: str):
    self.nome = nome
  def emitir_som(self, som: str):
    return f"{self.nome} está emitindo um som: {som}"

class Mamifero(Animal):
  def amamentar(self):
    return f"{self.nome} está amamentando!"

class Ave(Animal):
  def voar(self):
    return f"{self.nome} está voando!"

class Morcego(Mamifero, Ave):
  def dormir_de_cabeca_pra_baixo(self):
    return f"{self.nome} está dormindo!"

batman = Morcego("Batman")
print(f"O morcego {batman.dormir_de_cabeca_pra_baixo()}")
print(f"O morcego {batman.emitir_som("sons ultrassonicos!")}")