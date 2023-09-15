# Função para criar uma conta
def cria_conta(numero, titular, saldo, limite):
    conta = {
        'numero': numero,
        'titular': titular,
        'saldo': saldo,
        'limite': limite
    }
    return conta

# Função para depositar dinheiro na conta
def deposita(conta, valor):
    conta['saldo'] += valor

# Função para sacar valor da conta
def saca(conta, tipo_conta, valor):
    if tipo_conta == 'saldo':
        conta['saldo'] -= valor
    elif tipo_conta == 'limite':
        conta['limite'] -= valor

# Função para imprimir o extrato da conta
def extrato(conta):
    print(f'Número da Conta: {conta["numero"]}')
    print(f'Saldo: {conta["saldo"]}')

# Exemplo de conta
minha_conta = cria_conta('12345-6', 'João', 1000.0, 2000.0)
deposita(minha_conta, 500.0)
saca(minha_conta, 'saldo', 200.0)
extrato(minha_conta)