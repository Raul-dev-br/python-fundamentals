# ==========================================
# DICIONÁRIOS EM PYTHON
# ==========================================
# Um dicionário é uma coleção de itens organizada por 
# chaves e valores (como um dicionário real: Palavra -> Definição).
# Usamos chaves {} para criá-los.

# 1. Como criar um dicionário
# Estrutura: "chave": valor
usuario = {
    "nome": "Carlos",
    "idade": 28,
    "profissao": "Programador"
}
print("1. Dicionário completo:", usuario)

# 2. Acessando os valores
# Usamos a chave dentro de colchetes [] para pegar o valor correspondente
print("2. Nome do usuário:", usuario["nome"])
print("2. Idade do usuário:", usuario["idade"])

# 3. Adicionando ou alterando elementos
usuario["cidade"] = "São Paulo"  # Cria uma nova chave se ela não existir
usuario["idade"] = 29           # Atualiza o valor se a chave já existir
print("3. Dicionário modificado:", usuario)

# 4. Removendo elementos
# O método .pop() remove a chave informada e pode retornar o valor dela
profissao_removida = usuario.pop("profissao")
print("4. Profissão removida:", profissao_removida)
print("4. Dicionário após a remoção:", usuario)

# 5. Evitando erros ao buscar chaves (Método .get)
# Se você buscar uma chave que não existe com [], o código quebra.
# O método .get() evita isso retornando 'None' ou uma mensagem padrão.
print("5. Email:", usuario.get("email"))  # Retorna None (não dá erro)
print("5. Telefone:", usuario.get("telefone", "Não cadastrado"))

# 6. Descobrindo chaves e valores separadamente
print("6. Apenas as chaves:", list(usuario.keys()))
print("6. Apenas os valores:", list(usuario.values()))


# ==========================================
# MÉTODOS DE DICIONÁRIOS EM PYTHON
# ==========================================

# Vamos começar com um dicionário de exemplo
produto = {
    "nome": "Notebook",
    "preco": 3500,
    "estoque": 12
}

# 1. .get() -> Busca segura de valores
# Evita que o programa quebre se a chave não existir.
# Se não achar, retorna None ou um valor padrão definido por você.
print("1. Marca:", produto.get("marca"))  # Retorna: None
print("1. Marca padrão:", produto.get("marca", "Sem marca"))  # Retorna: Sem marca

# 2. .keys() -> Pega todas as chaves
# Muito útil para descobrir quais informações existem no dicionário.
chaves = produto.keys()
print("2. Chaves do dicionário:", list(chaves))

# 3. .values() -> Pega apenas os valores
# Ignora as chaves e traz somente os dados guardados.
valores = produto.values()
print("3. Valores do dicionário:", list(valores))

# 4. .items() -> Pega pares de (chave, valor)
# Transforma cada par em uma tupla. É o método perfeito para usar com loops 'for'.
print("4. Itens:", list(produto.items()))

# 5. .update() -> Atualiza ou adiciona vários itens de uma vez
# Se a chave já existir, atualiza o valor. Se não existir, ela é criada.
produto.update({"preco": 3200, "cor": "Cinza"})
print("5. Após o update:", produto)

# 6. .pop() -> Remove uma chave específica e devolve o valor dela
# Útil quando você quer retirar um dado, mas precisa usar o valor dele antes.
estoque_removido = produto.pop("estoque")
print(f"6. Valor removido: {estoque_removido} | Dicionário atual:", produto)

# 7. .clear() -> Apaga tudo
# Limpa completamente o dicionário, deixando-o vazio {}.
produto.clear()
print("7. Após o clear:", produto)
