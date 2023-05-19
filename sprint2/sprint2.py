import datetime
import getpass

# Lista de feedbacks
feedbacks = {
    'Região Norte': {
        'Vaso 1': {'notas': [], 'comentarios': []},
        'Vaso 2': {'notas': [], 'comentarios': []},
        # Adicione mais vasos da Zona Norte, se necessário
    },
    'Região Nordeste': {
        'Vaso 1': {'notas': [], 'comentarios': []},
        'Vaso 2': {'notas': [], 'comentarios': []},
        # Adicione mais vasos da Zona Nordeste , se necessário
    },
    'Região Centro-Oeste': {
        'Vaso 1': {'notas': [], 'comentarios': []},
        'Vaso 2': {'notas': [], 'comentarios': []},
        # Adicione mais vasos da Zona Centro-Oeste, se necessário
    },
    'Região Sudeste': {
        'Vaso 1': {'notas': [], 'comentarios': []},
        'Vaso 2': {'notas': [], 'comentarios': []},
        # Adicione mais vasos da Zona Sudeste, se necessário
    },
    'Região Sul': {
        'Vaso 1': {'notas': [], 'comentarios': []},
        'Vaso 2': {'notas': [], 'comentarios': []},
        # Adicione mais vasos da Zona Sul, se necessário
    }
}

# Lista de zonas
zonas = ['Região Norte', 'Região Nordeste', 'Região Centro-Oeste', 'Região Sudeste', 'Região Sul']

hora = datetime.datetime.now().time()

if hora.hour < 12:
    msg = "Bom dia!"
elif hora.hour < 18:
    msg = "Boa tarde!"  #código para mensagem ao usuário
else:
    msg = "Boa noite!"

adm = "administrador12" #login do admministrador
admpass = "adm123"      #senha do admministrador

while True:
    opc = input(
        f"{msg} Você deseja fazer login como:\n1. Administrador\n2. Cliente\n3. Sair\n") #Menu inicial

    if opc == "1": #login de administrador
        while True:
            adm_input = None
            while adm_input is None:
                adm_input = input("Digite seu nome de usuário: ")
                if adm_input.lower() == "voltar":
                    break
                if adm_input == adm:
                    adm_passinput = input("Digite sua senha: ")
                    if adm_passinput == admpass:
                        print("\n***** Login efetuado com sucesso! *****\n")
                        #Após login realizado
                        while True:
                            esc = input(
                                "\nDigite a região que você gostaria de verificar:\n1. Região Norte\n2. Região Nordeste\n3. Região Centro-Oeste \n4. Região Sudeste\n5. Região Sul\n6. Adicionar Vaso\n7. Voltar ao Menu Inicial\n8. Sair\n")
                            def exibir_feedbacks_ordem(zona):
                                #tela dos feedbacks e comentários
                                print(f"\n******Feedbacks para a região: {zona}*******")
                                for vaso, feedback in feedbacks[zona].items():
                                    
                                    notas = feedback['notas']
                                    comentarios = feedback['comentarios']
                                    if notas:
                                        media = sum(notas) / len(notas)
                                        print(f"\nVaso: {vaso} - Média de nota: {media:.2f}")
                                    else:
                                        print(f"-Vaso: {vaso} - Nenhum feedback registrado-")
                                    if comentarios:
                                        print(f"Comentários para o vaso {vaso}:")
                                        for comentario in comentarios:
                                            print(f"{comentario}\n")
                                    else:
                                        print(f"Nenhum comentário registrado para o vaso {vaso}\n")
                            #selecão do usuário
                            if esc == "1":
                                zona_escolhida = zonas[0]
                                exibir_feedbacks_ordem(zona_escolhida)
                            elif esc == "2":
                                zona_escolhida = zonas[1]
                                exibir_feedbacks_ordem(zona_escolhida)
                            elif esc == "3":
                                zona_escolhida = zonas[2]
                                exibir_feedbacks_ordem(zona_escolhida)
                            elif esc == "4":
                                zona_escolhida = zonas[3]
                                exibir_feedbacks_ordem(zona_escolhida)
                            elif esc == "5":
                                zona_escolhida = zonas[4]
                                exibir_feedbacks_ordem(zona_escolhida)
                            elif esc == "6": #Adicionar vaso
                                zona = input("Digite o nome da região em que deseja adicionar o vaso: ")
                                if zona in zonas:
                                    vaso = input("Digite o nome do vaso: ")
                                    feedbacks[zona][vaso] = {'notas': [], 'comentarios': []}
                                    print("Vaso adicionado com sucesso!")
                                else:
                                    print("Região inválida. Tente novamente. Atente a escrita, digite igual o exemplo: (Região Sul)")
                            elif esc == "7":#retornar
                                break
                            elif esc == "8":#Finaliza o programa
                                print(f"{msg}, muito obrigado!")
                                exit()
                            else:#qualquer resposta errada do usuário
                                print("Opção inválida. Tente novamente.")
                    #senha errada no login
                    else:
                        print("Senha incorreta! Tente Novamente.")
                    break 
                break
            break

    elif opc == "2":
        # Aqui começa a parte do cliente
        print("Olá, cliente!")
        zona_escolhida = None

        # Exibir lista de regiões disponíveis
        print("Regiões disponíveis:")
        for i, zona in enumerate(zonas):
            print(f"{i + 1}. {zona}")
        #tela dos feedbacks
        while True:
            esc = input("Digite o número da região que você deseja fornecer feedback (ou 'sair' para voltar ao menu): \n")

            if esc.lower() == "sair":
                break

            if esc.isdigit() and 1 <= int(esc) <= 5:
                zona_escolhida = zonas[int(esc) - 1]
                break
            else:
                print("Opção inválida. Tente novamente.")

        if zona_escolhida:
            print(f"\nVocê selecionou a região: {zona_escolhida}\n")
            print("Vasos disponíveis:")
            for i, vaso in enumerate(feedbacks[zona_escolhida].keys()):
                print(f"{i + 1}. {vaso}")

            while True:
                esc_vaso = input(
                    "\nDigite o número do vaso que você deseja fornecer feedback (ou 'sair' para voltar ao menu): ")

                if esc_vaso.lower() == "sair":
                    break
                
                if esc_vaso.isdigit() and 1 <= int(esc_vaso) <= len(feedbacks[zona_escolhida]):
                    vaso_escolhido = list(feedbacks[zona_escolhida].keys())[int(esc_vaso) - 1]
                    nota = input("Digite uma nota de 0 a 5 para o vaso: ")
                    comentario = input("Digite um comentário para o vaso: ")

                    if nota.isdigit() and 0 <= int(nota) <= 5:
                        feedbacks[zona_escolhida][vaso_escolhido]['notas'].append(int(nota))
                        feedbacks[zona_escolhida][vaso_escolhido]['comentarios'].append(comentario)
                        print("Feedback registrado com sucesso!")
                    else:
                        print("Nota inválida. Tente novamente.")

                else:
                    print("Opção inválida. Tente novamente.")

    elif opc == "3":
        print(f"{msg}, muito obrigado!")
        exit()

    else:
        print("Opção inválida. Tente novamente.")
