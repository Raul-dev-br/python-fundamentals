import subprocess

opcao = 6
lista_tarefas = []

def limpar_tela():
  subprocess.run("cls", shell=True)

def continuar():
  input("\nPressione Enter para continuar...")
  
def verificacao_tarefa_existe(idx) -> bool:
  if idx < 0 or idx > len(lista_tarefas):
      print("Número de Tarefa não existe!")
      continuar()
      return False
  return True

def adicionar():
  limpar_tela()
  nome_tarefa = input("Digite o nome da tarefa: ")
  if not nome_tarefa:
    print("[ERROR]A tarefa tem que ter um nome!")
    continuar()
    return
  else:
    lista_tarefas.append({ "name": nome_tarefa.strip(), "isMarked": False })
    print(f"Tarefa Adicionada: {nome_tarefa}")

def ver(querContinuar: bool):
  limpar_tela()
  if len(lista_tarefas) < 1:
    print("Não tem nenhuma tarefa na Lista!")
    continuar()
    return
  else:
    for i, tarefa in enumerate(lista_tarefas):
      print(f"{i + 1}. [ {"✔" if tarefa["isMarked"] else ""} ] {tarefa["name"]}")
    if querContinuar:
      continuar()

def atualizar():
  while True:
    try:
      ver(False)
      idx_tarefa = int(input("\nEscolha a tarefa a ser atualizada: "))
      break
    except ValueError:
      print("Entrada inválida! Por favor, digite um número inteiro.")
      continuar()
      limpar_tela()
  if idx_tarefa <= 0 or idx_tarefa > len(lista_tarefas):
    print("Número de Tarefa não existe!")
    continuar()
    return
  novo_nome_tarefa = input(f"Escreva a nova atualizacao para a tarefa ({idx_tarefa}): ")
  lista_tarefas[idx_tarefa - 1] = {"name": novo_nome_tarefa, "isMarked": False }
  continuar()

def completar():
  ver(False)
  while True:
    try:
      idx_tarefa = int(input("Escolha o número da tarefa para marcar como completada: "))
      break
    except ValueError:
      print("Entrada inválida! Por favor, digite um número inteiro.")
  if idx_tarefa <= 0 or idx_tarefa > len(lista_tarefas):
    print("Número de Tarefa não existe!")
    continuar()
    return
  else:
    lista_tarefas[idx_tarefa - 1]["isMarked"] = True
    print(f"Voce deu um checked na tarefa ({idx_tarefa})!")
  continuar()

def deletar():
  ver(False)
  mensagem_confirmacao = input("Você quer realmente apagar todas as tarefas marcadas como checked? (S - N): ")
  if mensagem_confirmacao.lower() == "s":
    global lista_tarefas
    lista_tarefas = [tarefa for tarefa in lista_tarefas if not tarefa["isMarked"]]
    print("Todas as tarefas com checked foram apagadas!")
    continuar()
  else:
    continuar()
    return

def verLista():
  print(f"Lista Completa: {lista_tarefas}")
  continuar()

while True:
  print("1. Adicionar Tarefa")
  print("2. Ver Tarefas")
  print("3. Atualizar Tarefa")
  print("4. Completar Tarefa")
  print("5. Deletar Tarefas Completadas")
  print("6. Sair")
  opcao = int(input("Digite sua escolha: ")) or 10

  if opcao == 6:
    limpar_tela()
    break

  match opcao:
    case 1:
      adicionar()
    case 2:
      ver(True)
    case 3:
      atualizar()
    case 4:
      completar()
    case 5:
      deletar()
    case 7:
      verLista()
    case _:
      print("Não escolheu nenhuma funcao!")
      continuar()

  limpar_tela()

