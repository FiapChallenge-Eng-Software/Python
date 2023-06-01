    # Otavio Vitoriano 552012
# Sofia Coutinho 552534
# Gabriel Torres 98600
# Jéssica Brum 97944
# Eduardo Fedeli 550132


# Classe para representar uma nota fiscal (NF)
class NotaFiscal:
    def __init__(self, numero, descricao, valor, pago):
        self.numero = numero
        self.descricao = descricao
        self.valor = valor
        self.pago = pago

# Lista para armazenar as notas fiscais a pagar
notas_a_pagar = []

# Lista para armazenar as notas fiscais a receber
notas_a_receber = []

from datetime import datetime

# Função para retornar a saudação com base no horário
def msg():
    hora_atual = datetime.now().hour

    if hora_atual < 12:
        return "----- Bom dia -----!"
    elif hora_atual < 18:
        return "----- Boa tarde -----!"
    else:
        return "----- Boa noite -----!"
# Função para cadastrar uma nota fiscal a pagar
def cadastrar_nf_pagar():
    numero = input("Digite o número da nota fiscal: ")
    descricao = input("Digite a descrição da nota fiscal: ")
    valor = float(input("Digite o valor da nota fiscal: "))
    pago = input("A nota fiscal já foi paga? (S/N): ").upper() == 'S'
    notas_a_pagar.append(NotaFiscal(numero, descricao, valor, pago))
    print("Nota fiscal cadastrada com sucesso!")

# Função para cadastrar uma nota fiscal a receber
def cadastrar_nf_receber():
    numero = input("Digite o número da nota fiscal: ")
    descricao = input("Digite a descrição da nota fiscal: ")
    valor = float(input("Digite o valor da nota fiscal: "))
    notas_a_receber.append(NotaFiscal(numero, descricao, valor, False))
    print("Nota fiscal cadastrada com sucesso!")

# Função para calcular o valor total das notas fiscais a pagar
def calcular_total_pagar():
    total_pagar = sum(nf.valor for nf in notas_a_pagar if not nf.pago)
    print("Total a pagar: R$", total_pagar)

# Função para calcular o valor total das notas fiscais a receber
def calcular_total_receber():
    total_receber = sum(nf.valor for nf in notas_a_receber)
    print("Total a receber: R$", total_receber)

# Função para calcular o saldo geral (total a receber - total a pagar)
def calcular_saldo_geral():
    total_pagar = sum(nf.valor for nf in notas_a_pagar if not nf.pago)
    total_receber = sum(nf.valor for nf in notas_a_receber)
    saldo_geral = total_receber - total_pagar
    print("Saldo Geral: R$", saldo_geral)

# Função para pagar uma conta a pagar
def pagar_conta():
    print("Notas fiscais a pagar:")
    for i, nf in enumerate(notas_a_pagar):
        print(f"{i+1}. Número: {nf.numero}, Descrição: {nf.descricao}, Valor: R$ {nf.valor}")

    numero = input("Digite o número da nota fiscal que deseja pagar: ")
    for nf in notas_a_pagar:
        if nf.numero == numero and not nf.pago:
            nf.pago = True
            print("Conta paga com sucesso!")
            return
    resp = input("Número de nota fiscal inválido ou a conta já foi paga. Deseja pagar todas as contas? (S/N): ")
    if resp.upper() == 'S':
        for nf in notas_a_pagar:
            if not nf.pago:
                nf.pago = True
        print("Todas as contas foram pagas com sucesso!")
    else:
        print("Pagamento cancelado.")

# Função para exibir a lista de contas cadastradas
def exibir_lista_contas():
    print("----- Lista de Contas Cadastradas -----")
    print("Contas a Pagar:")
    for nf in notas_a_pagar:
        print(f"Número: {nf.numero}, Descrição: {nf.descricao}, Valor: R$ {nf.valor}, Pago: {'Sim' if nf.pago else 'Não'}")
    print("Contas a Receber:")
    for nf in notas_a_receber:
        print(f"Número: {nf.numero}, Descrição: {nf.descricao}, Valor: R$ {nf.valor}, Pago: {'Sim' if nf.pago else 'Não'}")

# Função para exibir o menu e realizar as operações
def exibir_menu():
    while True:
        print(msg())
        print("----- Vinheria Agnello -----")
        print("1. Cadastrar nota fiscal a pagar")
        print("2. Cadastrar nota fiscal a receber")
        print("3. Calcular total a pagar")
        print("4. Calcular total a receber")
        print("5. Calcular saldo geral")
        print("6. Pagar conta")
        print("7. Exibir lista de contas")
        print("0. Sair")
        opcao = input("Digite a opção desejada: ")

        match opcao:
            case "1":
                cadastrar_nf_pagar()
            case "2":
                cadastrar_nf_receber()
            case "3":
                calcular_total_pagar()
            case "4":
                calcular_total_receber()
            case "5":
                calcular_saldo_geral()
            case "6":
                pagar_conta()
            case "7":
                exibir_lista_contas()
            case "0":
                print("Encerrando o programa...")
                return
            case _:
                print("Opção inválida! Por favor, digite uma opção válida.")

# Executa o programa
exibir_menu()
