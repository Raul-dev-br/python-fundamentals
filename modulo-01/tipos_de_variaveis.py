# TIPOS DE VARIÁVEIS
# Chegando nessa parte eu vi que a parada é padrão, não foge muito do escopo de JS que eu já tinha visto.

# INT
numero_inteiro = 23
# FLOAT
numero_com_ponto = 3.141592653589793238462643383279
print(f"Número Inteiro: {numero_inteiro}") #Isso daqui tinha no JS, se chama Interpolação e você tem que botar um f antes da string
print(f"Numero com Ponto Flutuante: {numero_com_ponto}\n")

# Os números também conseguem fazer operações aritméticas: +, -, *, /
print(f"Soma: {numero_inteiro + numero_com_ponto}")
print(f"Subtração: {numero_inteiro - numero_com_ponto}")
print(f"Multiplicação: {numero_inteiro * numero_com_ponto}")
print(f"Potenciação: {numero_inteiro ** numero_com_ponto}")
print(f"Divisão: {numero_inteiro / numero_com_ponto}")
print(f"Divisão com Inteiro (//): {numero_inteiro // numero_com_ponto}\n")

# Existe Também o Módulo que entrega o resto da divisão de dois números Inteiros
print(f"Módulo de 5 e 2: {5 % 2}\n") # Os resto da divisão entre 5 e 2 é 1

# Também dá pra ver o tipo da variável com TYPE
print(f"Tipo da variavel numero_inteiro: {type(numero_inteiro)}")

# TEXTO(string)
# O bagulho é padrão mesmo.

# Declaração
nome = "Gabriel"
sobrenome = "Casemiro"
nome_completo = "Pedro Pinto"
nome_completo_aspas = """ Pedro
 Pinto""" # Este padrão foi novo para mim, a diferença é que ele consegue fazer essa quebra de linha.
nome_completo_quebra = "Pedro \
Pinto" #Outro padrão que eu aprendi.

# Formatação: Existe uma cacetada!
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Gabriel" + "Casemiro")
print("Nome completo (4a forma):" + "Gabriel", "Casemiro")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))

# GUIA DE MÉTODOS DE STRINGS EM PYTHON (NÍVEL BÁSICO)

"""
## 1. split()

1. 💡 O que faz: Divide uma string em uma lista de pedaços menores com base em um caractere separador que você escolher.
2. 🛠️ Sintaxe e Parâmetros: string.split(sep=None) — sep define o caractere onde o corte será feito (o padrão é o espaço).
3. 🏃‍♂️ Exemplo Rápido:
   frase = "Python é legal"
   palavras = frase.split(" ") # ['Python', 'é', 'legal']
4. 🧠 Exercício Nível Básico: Você tem a string nomes = "Ana,Pedro,Maria,João". Use o método split() para transformar esse texto em uma lista contendo os quatro nomes separados.
   * Dica de Execução: Passe a vírgula "," como argumento dentro do método split.
---
"""
nomes = "Ana,Pedro,Maria,João"
nomes_separados = nomes.split(",")
print(f"Exercicio 01: {nomes_separados}") 

"""
## 2. join()

1. 💡 O que faz: Junta os itens de uma lista em uma única string, usando o texto escolhido como "cola" entre os elementos.
2. 🛠️ Sintaxe e Parâmetros: separador.join(lista) — O separador é o caractere que ficará no meio dos itens da lista.
3. 🏃‍♂️ Exemplo Rápido:
   letras = ["P", "y", "t", "h", "o", "n"]
   palavra = "".join(letras) # "Python"
4. 🧠 Exercício Nível Básico: Dada a lista de palavras data = ["01", "09", "2026"], junte esses elementos para formar uma data no formato padrão brasileiro, ou seja, separados por uma barra "/".
   * Dica de Execução: Crie a string da barra "/" e chame o método .join(data) nela.
"""
data = ["01", "09", "2026"]
data_com_barra = "/".join(data)
print(f"Exercicio 02: {data_com_barra}")

"""
## 3. strip(), lstrip() e rstrip()

1. 💡 O que faz: Limpam e removem espaços em branco sobressalentes que ficam no início ou no final de uma string.
2. 🛠️ Sintaxe e Parâmetros: string.strip() — Não precisa de argumentos para remover espaços, quebras de linha ou tabulações.
3. 🏃‍♂️ Exemplo Rápido:
   texto = "   olá mundo   "
   limpo = texto.strip() # "olá mundo"
4. 🧠 Exercício Nível Básico: Um usuário digitou a senha em um formulário e digitou sem querer um espaço no começo e outro no fim: usuario_senha = " minha_senha123 ". Remova esses espaços inúteis das pontas.
   * Dica de Execução: Basta aplicar o método .strip() diretamente na variável da senha.
"""
usuario_senha = " minha_senha1234 "
senha_sem_espaco = usuario_senha.strip()
print(f"Exercicio 03: {senha_sem_espaco}")

"""
## 4. replace()

1. 💡 O que faz: Substitui uma palavra ou caractere por outro texto dentro da string original.
2. 🛠️ Sintaxe e Parâmetros: string.replace(antigo, novo) — antigo é o termo que você quer tirar; novo é o termo que vai entrar.
3. 🏃‍♂️ Exemplo Rápido:
   texto = "Eu gosto de Java"
   novo_texto = texto.replace("Java", "Python") # "Eu gosto de Python"
4. 🧠 Exercício Nível Básico: Você tem a frase frase = "O preço do produto é R$ 10,00". Modifique o texto para mudar a palavra "produto" para "Notebook".
   * Dica de Execução: Use o método replace passando "produto" como primeiro argumento e "Notebook" como segundo.
"""
texto = "Lula Gouti"
ladrao = "Lula"
verdadeiro_goat = texto.replace(ladrao, "Bonoro").replace("Gouti", "Goat")
print(f"Exercicio 04: {verdadeiro_goat}")

"""
## 5. find() vs index()

1. 💡 O que faz: Procuram por um caractere ou palavra na string e dizem em qual posição (índice) ele começa. find() retorna -1 se não achar, enquanto index() gera um erro no programa.
2. 🛠️ Sintaxe e Parâmetros: string.find(termo) / string.index(termo) — O termo é o caractere ou texto que você quer localizar.
3. 🏃‍♂️ Exemplo Rápido:
   frase = "Estude Python"
   posicao = frase.find("Python") # Retorna 7
4. 🧠 Exercício Nível Básico: Dada a string frase_site = "Visite o nosso site em google.com", descubra em qual posição do texto começa a palavra "google.com" usando o método mais seguro caso ela não exista.
   * Dica de Execução: Prefira usar o método find() para que o seu código retorne -1 caso mude a frase e a palavra suma.
"""
frase_site = "Visite o nosso site em google.com"
where_is_google_dot_com = frase_site.find("google.com")
print(f"Exercício 05: { "Achou!" if where_is_google_dot_com >= 0 else "Não achou"}")

"""
## 6. format() e f-strings

1. 💡 O que faz: Serve para colocar variáveis dentro de um texto de forma bonita e organizada, além de controlar o número de casas decimais de números flutuantes.
2. 🛠️ Sintaxe e Parâmetros: f"Texto {variavel}" ou f"{valor:.2f}" (onde .2f limita para duas casas decimais).
3. 🏃‍♂️ Exemplo Rápido:
   nome = "Hugo"
   print(f"Olá, {nome}!") # "Olá, Hugo!"
4. 🧠 Exercício Nível Básico: Você tem as variáveis produto = "Camiseta" e preco = 49.9. Use uma f-string para exibir a mensagem: "O preço da Camiseta é R$ 49.90" (garantindo os dois dígitos centavos após o ponto).
   * Dica de Execução: Use a regra {preco:.2f} dentro da f-string para formatar o preço com duas casas decimais.
"""
produto = "Camiseta"
preco = 49.9
print(f"O preço da {produto} é R${preco:.2f}")

"""
## 7. startswith() e endswith()

1. 💡 O que faz: Descobrem se uma string começa (startswith) ou termina (endswith) com um determinado caractere ou palavra, devolvendo True ou False.
2. 🛠️ Sintaxe e Parâmetros: string.startswith(termo) / string.endswith(termo).
3. 🏃‍♂️ Exemplo Rápido:
   site = "https://brasil.gov.br"
   seguro = site.startswith("https") # True
4. 🧠 Exercício Nível Básico: Você recebeu o nome de um arquivo: arquivo = "foto_ferias.jpg". Verifique se este arquivo é uma imagem no formato JPG, checando se ele termina com ".jpg".
   * Dica de Execução: Aplique o método endswith(".jpg") na variável e veja se o retorno é verdadeiro.
"""
arquivo = "foto_ferias.jpg"
print(f"O arquivo é JPG: {"E JPG" if arquivo.endswith(".jpg") else "Não e JPG"}")

"""
## 8. upper() e lower()

1. 💡 O que faz: Convertem todas as letras do texto para maiúsculas (upper) ou todas para minúsculas (lower).
2. 🛠️ Sintaxe e Parâmetros: string.upper() / string.lower() — Não usam argumentos dentro dos parênteses.
3. 🏃‍♂️ Exemplo Rápido:
   nome = "Ana"
   print(nome.upper()) # "ANA"
4. 🧠 Exercício Nível Básico: Um usuário digitou a opção de confirmação como resposta = "SIM". Converta essa resposta inteira para letras minúsculas para que ela fique padronizada como "sim".
   * Dica de Execução: Chame o método .lower() na variável resposta.
"""
resposta = "SIM"
print(f"Nova resposta: {resposta.lower()}")


"""
## 9. isdigit(), isnumeric() e isalpha()

1. 💡 O que faz: Checam se a string contém apenas números inteiros (isdigit) ou apenas letras do alfabeto (isalpha), sem símbolos ou espaços.
2. 🛠️ Sintaxe e Parâmetros: string.isdigit() / string.isalpha() — Devolvem True ou False.
3. 🏃‍♂️ Exemplo Rápido:
   idade = "25"
   print(idade.isdigit()) # True
4. 🧠 Exercício Nível Básico: Você tem a string telefone = "999998888". Verifique se essa string contém apenas números decimais válidos antes de convertê-la para um número inteiro.
   * Dica de Execução: Use a função telefone.isdigit() e analise o resultado booleano.
"""
telefone = "999998888"
if(telefone.isdecimal()):
  telefone_numerico = int(telefone)
  print(f"É decimal! Novo tipo: {type(telefone_numerico)}")
else:
  print("Continha mais coisa!")