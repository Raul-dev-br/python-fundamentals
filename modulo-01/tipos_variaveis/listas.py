# Declaracao
minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibindo a lista
print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7]) # minha_lista[1], minha_lista[2], ...minha_lista[6]
print("minha_lista[:6]:", minha_lista[:6])
print("minha_lista[2:]:", minha_lista[2:])

# 1. Criando uma lista inicial para os testes
frutas = ["maçã", "banana", "laranja"]
print(f"Lista inicial: {frutas}")

# --- ADICIONAR ELEMENTOS ---

# append(): Adiciona um elemento ao final da lista
frutas.append("uva")
print(f"Após append('uva'): {frutas}")

# insert(): Insere um elemento em um índice/posição específica (ex: posição 1)
frutas.insert(1, "morango")
print(f"Após insert(1, 'morango'): {frutas}")

# extend(): Adiciona múltiplos elementos (de outra lista) ao final
outras_frutas = ["melancia", "abacaxi"]
frutas.extend(outras_frutas)
print(f"Após extend(outras_frutas): {frutas}")


# --- REMOVER ELEMENTOS ---

# remove(): Remove o primeiro item encontrado com o valor especificado
frutas.remove("banana")
print(f"Após remove('banana'): {frutas}")

# pop(): Remove e retorna o item do índice especificado (se vazio, remove o último)
fruta_removida = frutas.pop(2)  # Remove quem está no índice 2
print(f"Após pop(2) (removeu {fruta_removida}): {frutas}")


# --- PESQUISA E INFORMAÇÃO ---

# index(): Retorna o índice (posição) da primeira ocorrência do elemento
# Vamos adicionar mais uma 'maçã' para testar os próximos métodos
frutas.append("maçã")
print(f"Lista atualizada para busca: {frutas}")

indice_maca = frutas.index("maçã")
print(f"Índice da primeira 'maçã': {indice_maca}")

# count(): Conta quantas vezes um elemento aparece na lista
quantidade_macas = frutas.count("maçã")
print(f"Quantidade de 'maçã' na lista: {quantidade_macas}")


# --- ORDENAÇÃO E INVERSÃO ---

# reverse(): Inverte a ordem atual dos elementos na lista
frutas.reverse()
print(f"Após reverse(): {frutas}")

# sort(): Ordena a lista em ordem alfabética (ou crescente para números)
frutas.sort()
print(f"Após sort() (ordem alfabética): {frutas}")


# --- UTILITÁRIOS ---

# copy(): Cria uma cópia independente da lista
copia_frutas = frutas.copy()
print(f"Cópia da lista criada: {copia_frutas}")

# clear(): Limpa completamente a lista, deixando-a vazia
frutas.clear()
print(f"Após clear() na lista original: {frutas}")
print(f"A cópia continua intacta: {copia_frutas}")
 
