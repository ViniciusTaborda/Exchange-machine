# TDE Maquina de troco

print('='*60)
print('{:^60}'.format('Maquina de troco - TDE'))
print('='*60)
print('Por: Vinicius Eduardo Taborda Costa')

# ENTRADA DE QUANTIDADES DE MOEDAS EM ESTOQUE
estoqueMoedas1Real = int(input('Forneca a quantidade de moedas de 1 real em estoque: '))
estoqueMoedas50Cents = int(input('Forneca a quantidade de moedas de 50 centavos em estoque: '))
estoqueMoedas25Cents = int(input('Forneca a quantidade de moedas de 25 centavos em estoque: '))
estoqueMoedas10Cents = int(input('Forneca a quantidade de moedas de 10 centavos em estoque: '))
estoqueMoedas5Cents = int(input('Forneca a quantidade de moedas de 5 centavos em estoque: '))

# VALOR DE CADA MOEDA
UM_REAL = 1.00
CINQUENTA_CENTS = 0.50
VINTE_E_CINCO_CENTS = 0.25
DEZ_CENTS = 0.10
CINCO_CENTS = 0.05

# CALCULO DA QUANTIDADE DO TROCO

while True:

    valorTotalDoEstoque = (estoqueMoedas1Real * UM_REAL ) + (estoqueMoedas50Cents * CINQUENTA_CENTS) + (estoqueMoedas25Cents * VINTE_E_CINCO_CENTS) + (estoqueMoedas10Cents * DEZ_CENTS) + (estoqueMoedas5Cents * CINCO_CENTS)

    print('Valor total disponivel no estoque:', valorTotalDoEstoque)
    print('=' * 60)

    # QUANTIDADE DE TROCO PARA CADA MOEDA
    trocoDeMoedasDe1Real = 0
    trocoDeMoedasDe50Cents = 0
    trocoDeMoedasDe25Cents = 0
    trocoDeMoedasDe10Cents = 0
    trocoDeMoedasDe5Cents = 0

    # ENTRADA DO VALOR GASTO E PAGO PELO CLIENTE
    valorPagoPeloCliente = float(input('Forneca o valor pago pelo cliente: '))
    valorGastoPeloCliente = float(input('Forneca o valor gasto pelo cliente: '))
    print('=' * 60)

    # CALCULO DO TROCO
    troco = (valorPagoPeloCliente - valorGastoPeloCliente)

    if valorTotalDoEstoque >= troco:

        # MOEDA DE UM REAL
        while (estoqueMoedas1Real > 0) and (troco > 0) and (troco >= UM_REAL) and (estoqueMoedas1Real != 0):
            trocoDeMoedasDe1Real = trocoDeMoedasDe1Real + 1
            estoqueMoedas1Real = estoqueMoedas1Real - 1
            troco = troco - UM_REAL

        # MOEDA DE CINQUENTA CENTAVOS
        while (estoqueMoedas50Cents > 0) and (troco > 0) and (troco >= CINQUENTA_CENTS) and (estoqueMoedas50Cents != 0):
            trocoDeMoedasDe50Cents = trocoDeMoedasDe50Cents + 1
            estoqueMoedas50Cents = estoqueMoedas50Cents - 1
            troco = troco - CINQUENTA_CENTS

        # MOEDA DE VINTE E CINCO CENTAVOS
        while (estoqueMoedas25Cents > 0) and (troco > 0) and (troco >= VINTE_E_CINCO_CENTS) and (estoqueMoedas25Cents != 0):
            trocoDeMoedasDe25Cents = trocoDeMoedasDe25Cents + 1
            estoqueMoedas25Cents = estoqueMoedas25Cents - 1
            troco = troco - VINTE_E_CINCO_CENTS

        # MOEDA DE DEZ CENTAVOS
        while (estoqueMoedas10Cents > 0) and (troco > 0) and (troco >= DEZ_CENTS) and (estoqueMoedas10Cents != 0):
            trocoDeMoedasDe10Cents = trocoDeMoedasDe10Cents + 1
            estoqueMoedas10Cents = estoqueMoedas10Cents - 1
            troco = troco - DEZ_CENTS

        # MOEDA DE CINCO CENTAVOS
        while (estoqueMoedas5Cents > 0) and (troco > 0) and (troco >= CINCO_CENTS) and (estoqueMoedas5Cents != 0):
            trocoDeMoedasDe5Cents = trocoDeMoedasDe5Cents + 1
            estoqueMoedas5Cents = estoqueMoedas5Cents - 1
            troco = troco - CINCO_CENTS

        # SAIDA DE QUANTIDADE DE MOEDAS PARA O TROCO
        print('=' * 60)
        print('O cliente recebera', trocoDeMoedasDe1Real, 'moedas de um real.')
        print('O cliente recebera', trocoDeMoedasDe50Cents, 'moedas de cinquenta centavos.')
        print('O cliente recebera', trocoDeMoedasDe25Cents, 'moedas de vinte e cinco centavos.')
        print('O cliente recebera', trocoDeMoedasDe10Cents, 'moedas de dez centavos.')
        print('O cliente recebera', trocoDeMoedasDe5Cents, 'moedas de cinco centavos.')
        print('=' * 60)
        print('Faltou:{:.2}'.format(troco))
        print('=' * 60)

    else:
        print ('Quantidade de moedas no estoque insuficiente para dar troco.')
        print('=' * 60)
    if valorTotalDoEstoque <= 0:
        print('Nao ha mais moedas disponiveis no estoque.')
        break
