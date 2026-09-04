# ==============================================================================
# GUIA DE FUNCIONALIDADES DO 'IMPORT' EM PYTHON
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. IMPORTAÇÃO PADRÃO (import modulo)
# Importa o módulo inteiro. Para usar as funções, você precisa usar o prefixo.
# Vantagem: Evita conflito de nomes (você sempre sabe de onde a função veio).
# ------------------------------------------------------------------------------
import math

print("--- 1. Importação Padrão ---")
# Precisamos usar 'math.' antes da função
raiz = math.sqrt(16)
print(f"Raiz de 16 usando 'import math': {raiz}")
print(f"Valor de Pi: {math.pi}\n")


# ------------------------------------------------------------------------------
# 2. IMPORTAÇÃO ESPECÍFICA (from modulo import funcao)
# Traz apenas o que você precisa diretamente para o seu código.
# Vantagem: Código mais limpo na hora de usar (não precisa do prefixo).
# Desvantagem: Pode causar conflito se você já tiver uma variável com o mesmo nome.
# ------------------------------------------------------------------------------
from math import sin, cos

print("--- 2. Importação Específica ---")
# Usamos a função diretamente, sem o 'math.'
resultado_sin = sin(0)
print(f"Seno de 0 usando 'from math import sin': {resultado_sin}\n")


# ------------------------------------------------------------------------------
# 3. APELIDO PARA MÓDULO OU FUNÇÃO (import modulo as apelido)
# Dá um nome mais curto ou conveniente para o módulo ou função.
# Vantagem: Muito útil para módulos com nomes longos ou bibliotecas famosas (como pandas as pd).
# ------------------------------------------------------------------------------
import datetime as dt
from math import factorial as fat

print("--- 3. Uso de Apelidos (Alias) ---")
# Usando o apelido 'dt' em vez de 'datetime'
ano_atual = dt.datetime.now().year
print(f"Ano atual usando 'import datetime as dt': {ano_atual}")

# Usando o apelido 'fat' para a função 'factorial'
print(f"Fatorial de 5 usando o apelido 'fat': {fat(5)}\n")


# ------------------------------------------------------------------------------
# EXTRA: Por que evitamos o 'from modulo import *'?
# ------------------------------------------------------------------------------
# A sintaxe 'from math import *' importa TUDO do módulo de uma vez.
# Isso é considerado uma má prática (anti-pattern) porque polui o código,
# consome memória desnecessária e pode sobrescrever funções suas sem você perceber.
