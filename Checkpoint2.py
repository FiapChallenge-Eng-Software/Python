# Otavio Vitoriano 552012
# Sofia Coutinho 552534
# Gabriel Torres 98600
# Jéssica Brum 97944
# Eduardo Fedeli 550132
# cria um dicionário vazio para representar o estoque
# Definir inventário vazio
estoque = {
     "1": ("Vinho tinto", 5, 149.90),
    "2": ("Vinho branco", 10, 99.90),
    "3": ("Vinho rosé", 7, 79.90),
    "4": ("Vinho do Porto", 3, 199.90),
}

# Definir credenciais do vendedor
vend_usu = "vendedor1"
vend_pass = "12345"
# Definir mensagem de boas-vindas
import datetime
import getpass
hora = datetime.datetime.now().time()
if hora.hour < 12:
    msg = "Bom dia!"
elif hora.hour < 18:
    msg = "Boa tarde!"
else:
    msg = "Boa noite!"
print(f"{msg} Seja bem-vindo à Vinheria Agnello!")

# Loop de opções do usuário
while True:
    opcao = input("Você deseja logar como:\n1-Vendedor\n2-Cliente\n")

    # Opção do vendedor
    if opcao == "1":
        while True:
            vend_usu_input= None
            while vend_usu_input is None:
                vend_usu_input = input("Digite seu nome de usuário: ")
                if vend_usu_input == "":
                    print("Digite um nome de usuário por favor: ")
                    vend_usu_input=None
                    
                if vend_usu_input == vend_usu:
                    vend_pass_input = input("Digite sua senha: ")
                    if vend_pass_input == vend_pass:
                        print("\n*****Login efetuado com sucesso!******\n")
                        # TODO: adicionar menu para gerenciamento de estoque
                        while True:
                            print("\nSelecione uma opção:\n1 - Verificar estoque\n2 - Modificar estoque\n3 - Sair")
                            opcao_vend = input()
                            
                            if opcao_vend == "1": #VERIFICAÇÃO DE ESTOQUE 
                                print("\nEstoque atual:\n")
                                for numero, (nome, quantidade, valor) in estoque.items():
                                    print(f"{numero}. {nome} - {quantidade} unidades - R$ {valor:.2f}")
                                    
                                    
                            elif opcao_vend == "2": #EDIÇÃO DO ESTOQUE 
                                print("\nAdicionar ou remover produtos do estoque:\n")
                                for numero, (nome, quantidade, valor) in estoque.items():
                                    print(f"{numero}. {nome} - {quantidade} unidades - R$ {valor:.2f}")
                                escolha = input("\nDigite o número do produto que deseja modificar: ")
                                
                                if escolha in estoque:
                                    nome, quantidade, valor = estoque[escolha]
                                    print(f"\nProduto selecionado: {nome} - {quantidade} unidades - R$ {valor:.2f}")
                                    opcao_estoque = input("\nO que deseja fazer:\n1 - Adicionar unidades\n2 - Remover unidades\n3 - Alterar valor\n4 - Cancelar\n")
                                    
                                    if opcao_estoque == "1":
                                        quantidade_add = int(input("Digite a quantidade que deseja adicionar: "))
                                        estoque[escolha] = (nome, quantidade + quantidade_add, valor)
                                        print(f"\n{quantidade_add} unidades de {nome} adicionadas ao estoque.\n")
                                   
                                    elif opcao_estoque == "2":
                                        quantidade_rem = int(input("Digite a quantidade que deseja remover: "))
                                        
                                        if quantidade_rem > quantidade:
                                            print(f"\nNão há {quantidade_rem} unidades de {nome} em estoque.\n")
                                        
                                        else:
                                            estoque[escolha] = (nome, quantidade - quantidade_rem, valor)
                                            print(f"\n{quantidade_rem} unidades de {nome} removidas do estoque.\n")
                                   
                                    elif opcao_estoque == "3":
                                        novo_valor = float(input("Digite o novo valor: "))
                                        estoque[escolha] = (nome, quantidade, novo_valor)
                                        print(f"\nValor de {nome} alterado para R$ {novo_valor:.2f}\n")
                                    
                                    elif opcao_estoque == "4":
                                        print("\nOperação cancelada.\n")
                                    
                                    else:
                                        print("\nOpção inválida. Operação cancelada.\n")
                                else:
                                    print("\nProduto não encontrado. Operação cancelada.\n")
                                    
                            elif opcao_vend == "3": #EXIT DO GERENCIADOR
                                print("\nSaindo do gerenciador de estoque...")
                                exit()   
                            else:
                                print("\nOpção inválida. Tente novamente.\n")
                        break
                    else:
                        print("\n/////Senha incorreta. Tente novamente./////\n")
                else:
                    print("\n/////Usuário não encontrado/////\n")



        # Opção do cliente
    elif opcao == "2":
            pos = ["sim", "Sim", "S", "s", "Ss", "ss"]
            dec = None
            usuarios = {}

            # Cadastro do usuário
            while dec is None:
                print("Bem-vindo ao sistema de cadastro!")
                usuario = input("Digite seu nome de usuário: ")
                senha = input("Digite sua senha: ")
                if usuario in usuarios:
                    print("Usuário já existe. Por favor, tente novamente.")
                else:
                    usuarios[usuario] = senha
                    print("Usuário cadastrado com sucesso!")
                    break

            # Login do usuário
            while True:
                print("\n*****Bem-vindo ao sistema de login!******\n")
                usuario_login = input("Digite seu nome de usuário: ")
                senha_login = input("Digite sua senha: ")
                if usuario_login in usuarios and usuarios[usuario_login] == senha_login:
                    print("\n*****Login efetuado com sucesso!******\n")
                    dec = input("Você deseja realizar uma compra? Se sim, vamos para o cadastro! ")
                else:
                    print("\n//////Usuario não encontrado//////\n")
                    break
                    if dec in pos:
                        
                        nome = None
                        while nome is None:
                            nome = input("Digite seu primeiro nome: ")
                            if nome == "":
                                print("Por favor, preencha seu nome.")
                                nome = None

                        sobrenome = input("Digite seu sobrenome: ")
                        if sobrenome == "":
                            print("Por favor, preencha seu sobrenome.")
                            sobrenome = None

                        idade = None
                        while idade is None:
                            try:
                                idade = int(input("Digite sua idade: "))
                                if idade < 0:
                                    print("Por favor, digite uma idade válida.")
                                    idade = None
                                elif idade < 18:
                                    print("O site é apenas para maiores de 18 anos!")
                                    print(f"Obrigado, {msg}")
                                    exit()
                            except ValueError:
                                print("Por favor, digite um valor numérico para a idade.")
                                idade = None

                        # Cadastro de endereço
                        rua = None
                        while rua is None:
                            rua = input("Digite o nome da sua rua: ")
                            if rua == "":
                                print("Por favor, preencha o nome da rua.")
                                rua = None

                        bairro = None
                        while bairro is None:
                            bairro = input("Digite o bairro: ")
                            if bairro == "":
                                print("Por favor, preencha o nome do bairro.")
                                bairro = None

                        num = None
                        while num is None:
                            num = input("Digite o número da casa: ")
                            if num == "":
                                print("Por favor, preencha o número da casa.")
                                num = None

                        cep = None
                        while cep is None:
                            cep_str = input("Digite o CEP: ")
                            if cep_str == "":
                                print("Por favor, preencha o CEP.")
                                cep = None
                            else:
                                try:
                                    cep = int(cep_str)
                                except ValueError:
                                    print("Por favor, digite um CEP válido.")
                                    cep = None

                        comp = input("Digite o complemento (opcional): ")

                        print(f"Esses são seus dados:\nNome: {nome} {sobrenome}\nIdade: {idade}\nSeus dados de endereço são:\nRua: {rua}\nBairro: {bairro}\nNúmero: {num}\nCEP: {cep}\nComplemento: {comp}")     
                        break
                    else:
                        print(f"Tudo bem,{msg} ")
                        exit()
                
    else:
        print("\nOpção inválida. Tente novamente.")        
    
else:
            print(f"Obrigado, {msg}!")
######################### CADASTRO DE CLIENTE# #############################


