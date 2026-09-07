# Devo confessar que essa ideia de decorador eu não conhecia e achei muito interessante
# Pelo o que eu entendi é como se fosse um "Embrulho de um caixa", podemos fazer autenticações sem mudar a função princispl

def meu_decorador(func):
  def wrapper():
    print("Coisas que podem vir antes da função principal!")
    func()
    print("Coisas que podem vir depois da função principal!")
  return wrapper

@meu_decorador
def func_principal():
  print("Funcão executada!")

func_principal()

# Decoradores podem ser feitos com classes também
class MeuDecoradorComClass():
  def __init__(self, func):
    self.func = func

  def __call__(self):
    print("Antes da função!")
    self.func()
    print("Depois da função!")

@MeuDecoradorComClass
def segunda_func():
  print("Segunda Func!")

