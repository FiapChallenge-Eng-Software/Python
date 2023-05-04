# Otavio Vitoriano 552012
# Sofia Coutinho 552534
# Gabriel Torres 98600
# Jéssica Brum 97944
# Eduardo Fedeli 550132
# cria um dicionário vazio para representar o estoque


vend_usu = "vendedor1"
vend_pass = "12345"

# Função para definir mensagem de horário
import datetime
hora = datetime.datetime.now().time()
if hora.hour < 12:
    msg = "Bom dia!"
elif hora.hour < 18:
    msg = "Boa tarde!"
else:
    msg = "Boa noite!"

# Mensagem de boas-vindas
print(f"{msg} Seja bem-vindo à Vinheria Agnello!")

# Loop para garantir que o usuário insira uma opção válida (1 ou 2)
while True:
    usu = input("Você deseja logar como:\n1-Vendedor\n2-Cliente\n")

    if usu == "1":
        while True:
            vend_usu_input = input("Digite seu e-mail: ")
            if vend_usu_input == vend_usu:
                vend_pass_input = input("Digite sua senha: ")
                if vend_pass_input == vend_pass:
                    print("Login efetuado com sucesso!")
                    # código para o menu do vendedor
                    ########################## SISTEMA DE ESTOQUE E COMPRA#################
                    ##########################SISTEMA DE ESTOQUE E COMPRA#################
                    print(f"Obrigado, {msg}!")
                    exit()
                else:
                    print("Senha incorreta. Tente novamente.")
            else:
                print("E-mail incorreto. Tente novamente.")
                break

    elif usu == "2":
        pos = ["sim", "Sim", "S", "s", "Ss", "ss"]
        dec = None
        while dec is None:  # cadastro de usuário e senha
            usuarios = {}
        while True:
            print("Bem-vindo ao sistema de cadastro!")
            usuario = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")
            if usuario in usuarios:
                print("Usuário já existe. Por favor, tente novamente.")
            else:
                usuarios[usuario] = senha
                print("Usuário cadastrado com sucesso!")
                break

        # login de usuário e senha
        while True:
            print("Bem-vindo ao sistema de login!")
            usuario_login = input("Digite seu nome de usuário: ")
            senha_login = input("Digite sua senha: ")
            if usuario_login in usuarios and usuarios[usuario_login] == senha_login:
                print("Login efetuado com sucesso!")
                dec = input("Você deseja realizar uma compra? Se sim, vamos para o cadastro!")
                if dec in pos:
                    nome = input("Digite seu primeiro nome: ")
                    sobrenome = input("Digite seu sobrenome: ")
                    idade = int(input("Digite sua idade: "))

                    print("\nAgora vamos para o cadastro de endereço!")

                    rua = None
                    while rua is None:
                        rua = input("Digite o nome da sua rua: ")

                    bairro = None
                    while bairro is None:
                        bairro = input("Digite o bairro: ")

                    num = None
                    while num is None:
                        num = input("Digite o número da casa: ")

                    cep = None
                    cep_str = input("Digite o CEP: ")
                    try:
                        cep = int(cep_str)
                    except ValueError:
                        print("Por favor, digite um CEP válido.")

                    comp = None
                    while comp is None or not comp.strip():
                        comp = input("Digite o complemento (opcional): ") or None
                print(f"Esses são seus dados:\nNome: {nome} {sobrenome}\nIdade: {idade}\nSeus dados de endereço são:\nRua: {rua}\nBairro: {bairro}\nNúmero: {num}\nCEP: {cep}\nComplemento: {comp}")     
                break

    else:
        print("Opção inválida. Tente novamente.")        
    
else:
            print(f"Obrigado, {msg}!")
######################### CADASTRO DE CLIENTE# #############################


