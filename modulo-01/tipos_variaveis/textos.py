# ==========================================
# TEXTOS (STRINGS) EM PYTHON
# ==========================================
# Em Python, qualquer texto delimitado por aspas 
# simples ('') ou duplas ("") é uma string.

# 1. Criação e Concatenação (Juntar textos)
nome = "Ana"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome  # Juntando com operador +
print("1. Nome Completo:", nome_completo)

# 2. Formatação de Strings (f-strings)
# A forma mais moderna e limpa de incluir variáveis dentro de um texto
idade = 25
mensagem = f"A {nome} tem {idade} anos de idade."
print("2. Mensagem formatada:", mensagem)

# 3. Métodos de Modificação (Maiúsculas/Minúsculas)
texto_base = "Aprendendo Python!"
print("3. Tudo em maiúsculas:", texto_base.upper())
print("3. Tudo em minúsculas:", texto_base.lower())

# 4. Substituição e Divisão
frase = "Eu gosto de bananas"
nova_frase = frase.replace("bananas", "maçãs")  # Substitui uma palavra por outra
print("4. Frase alterada:", nova_frase)

palavras = frase.split(" ")  # Divide o texto nos espaços, gerando uma lista
print("4. Texto dividido:", palavras)

# 5. Descobrindo o tamanho do texto
# Conta todos os caracteres, incluindo os espaços
tamanho = len(texto_base)
print(f"5. O texto '{texto_base}' tem {tamanho} caracteres.")

# 6. Acessando partes do texto (Fatiamento / Slicing)
# Strings funcionam como listas de caracteres (o índice começa em 0)
linguagem = "Python"
primeira_letra = linguagem[0]
tres_primeiras = linguagem[0:3]  # Pega do índice 0 até o 2
print(f"6. Primeira letra: {primeira_letra} | Três primeiras: {tres_primeiras}")
