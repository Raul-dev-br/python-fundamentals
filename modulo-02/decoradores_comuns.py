class ContaBancaria:
    # Atributo de classe: compartilhado por todas as contas
    codigo_banco = "341"

    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular        # Atributo de instância
        self.saldo = saldo_inicial    # Atributo de instância

    # 1. Método de instância (Modifica o estado do objeto)
    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
            print(f"Depositado R${valor:.2f} na conta de {self.titular}.")

    # 2. Método de classe (Acessa ou modifica o estado da classe)
    @classmethod
    def alterar_codigo_banco(cls, novo_codigo: str) -> None:
        cls.codigo_banco = novo_codigo
        print(f"Código do banco alterado globalmente para: {cls.codigo_banco}")

    # 3. Método estático (Função utilitária isolada)
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        # Uma validação simples apenas para ilustrar (ex: checar o tamanho)
        cpf_limpo = cpf.replace(".", "").replace("-", "")
        return len(cpf_limpo) == 11


# --- Testando os comportamentos na prática ---

# Usando o Método Estático (@staticmethod)
# Veja que não precisamos criar nenhuma conta para validar um CPF!
cpf_valido = ContaBancaria.validar_cpf("123.456.789-00")
print(f"O CPF enviado é válido? {cpf_valido}\n")

# Criando instâncias (Objetos)
conta_ana = ContaBancaria("Ana", 1000.0)
conta_bob = ContaBancaria("Bob", 500.0)

# Usando o Método de Instância
# Ele altera especificamente o saldo da Ana, sem mexer no do Bob
conta_ana.depositar(250.0)
print(f"Saldo da Ana: R${conta_ana.saldo}")
print(f"Saldo do Bob: R${conta_bob.saldo}\n")

# Usando o Método de Classe (@classmethod)
# Ele altera uma propriedade que afeta a classe inteira de uma vez só
print(f"Código original do banco da Ana: {conta_ana.codigo_banco}")

ContaBancaria.alterar_codigo_banco("033")

# Agora todas as contas refletem a mudança automaticamente
print(f"Novo código na conta da Ana: {conta_ana.codigo_banco}")
print(f"Novo código na conta do Bob: {conta_bob.codigo_banco}")
