# ==========================================
# O QUE SÃO TUPLAS EM PYTHON?
# ==========================================
# Uma tupla é uma estrutura de dados que permite
# armazenar uma sequência de elementos de forma 
# ordenada e, o mais importante, IMUTÁVEL.

# 1. Como criar uma tupla
# Usamos parênteses () para definir uma tupla
minha_tupla = (10, 20, 30, 20, 40)
print("1. Minha tupla completa:", minha_tupla)

# 2. Imutabilidade (A regra de ouro)
# Diferente das listas, você NÃO pode alterar, adicionar ou remover itens.
# O código abaixo geraria um erro (TypeError):
# minha_tupla[0] = 99 

# 3. Acesso aos elementos (Indexação)
# O índice começa sempre no zero [0]
primeiro_item = minha_tupla[0]
ultimo_item = minha_tupla[-1]  # -1 pega o último elemento
print(f"3. Primeiro item: {primeiro_item} | Último item: {ultimo_item}")

# 4. Métodos úteis das tuplas
# Como são imutáveis, elas possuem poucos métodos:
quantidade_de_vintes = minha_tupla.count(20)  # Conta quantas vezes o valor aparece
posicao_do_trinta = minha_tupla.index(30)    # Encontra o índice da primeira ocorrência
print(f"4. O número 20 aparece {quantidade_de_vintes} vezes")
print(f"4. O número 30 está na posição (índice): {posicao_do_trinta}")

# 5. Tamanho da tupla
tamanho = len(minha_tupla)
print(f"5. A tupla possui {tamanho} elementos")

# 6. Tuplas aceitam tipos de dados diferentes (mistas)
tupla_mista = ("Python", 2026, True, 5.5)
print("6. Tupla com vários tipos:", tupla_mista)
