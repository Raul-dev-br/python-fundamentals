# ==========================================
# NÚMEROS EM PYTHON
# ==========================================
# Python possui três tipos numéricos principais:
# int (inteiros), float (decimais) e complex (complexos).

# 1. Tipos de Números
inteiro = 10         # Tipo 'int': número sem casas decimais
decimal = 5.75       # Tipo 'float': usa ponto (.) em vez de vírgula
print(f"1. Tipos: {inteiro} é {type(inteiro)} | {decimal} é {type(decimal)}")

# 2. Operações Matemáticas Básicas
soma = 10 + 5
subtracao = 10 - 5
multiplicacao = 10 * 5
divisao = 10 / 3      # A divisão comum sempre resulta em um 'float'
print(f"2. Soma: {soma} | Divisão: {divisao}")

# 3. Operações Especiais (Muito Úteis)
divisao_inteira = 10 // 3  # Descarta as casas decimais (resultado: 3)
resto_divisao = 10 % 3     # Pega apenas o que sobrou (resultado: 1)
exponenciacao = 2 ** 3     # Dois elevado a três (2³ = 8)
print(f"3. Inteira: {divisao_inteira} | Resto: {resto_divisao} | Potência: {exponenciacao}")

# 4. Ordem de Precedência (Regra Matemática)
# Parênteses () têm prioridade máxima, seguidos de *, /, + e -
resultado_1 = 2 + 3 * 4    # Multiplica primeiro: 2 + 12 = 14
resultado_2 = (2 + 3) * 4  # Soma primeiro: 5 * 4 = 20
print(f"4. Sem parênteses: {resultado_1} | Com parênteses: {resultado_2}")

# 5. Conversão de Tipos (Casting)
# Você pode transformar números ou até textos numéricos em outros tipos
texto_numero = "42"
numero_real = int(texto_numero)  # Transforma string em inteiro
print(f"5. Texto convertido para número: {numero_real + 8}")  # Resultado: 50

# 6. Arredondamento
valor_quebrado = 3.14159
print(f"6. Arredondado para 2 casas: {round(valor_quebrado, 2)}")
