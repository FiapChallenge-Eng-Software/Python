import datetime
import getpass

# Lista de feedbacks
feedbacks = {
    'Zona Norte': {
        'Vaso 1': {'notas': [], 'comentarios': []},
        'Vaso 2': {'notas': [], 'comentarios': []},
        # Adicione mais vasos da Zona Norte, se necessário
    },
    'Zona Sul': {
        'Vaso 1': {'notas': [], 'comentarios': []},
        'Vaso 2': {'notas': [], 'comentarios': []},
        # Adicione mais vasos da Zona Sul, se necessário
    },
    'Zona Leste': {
        'Vaso 1': {'notas': [], 'comentarios': []},
        'Vaso 2': {'notas': [], 'comentarios': []},
        # Adicione mais vasos da Zona Leste, se necessário
    },
    'Zona Oeste': {
        'Vaso 1': {'notas': [], 'comentarios': []},
        'Vaso 2': {'notas': [], 'comentarios': []},
        # Adicione mais vasos da Zona Oeste, se necessário
    }
}

# Lista de zonas
zonas = ['Zona Norte', 'Zona Sul', 'Zona Leste', 'Zona Oeste']

hora = datetime.datetime.now().time()

if hora.hour < 12:
    msg = "Bom dia!"
elif hora.hour < 18:
    msg = "Boa tarde!"
else:
    msg = "Boa noite!"

adm = "administrador12"
admpass = "adm123"

while True:
    opc = input(
        f"{msg} Você deseja fazer login como:\n1. Administrador\n2. Cliente\n3. Sair\n")

    if opc == "1":
        while True:
            adm_input = None
            while adm_input is None:
                adm_input = input("Digite seu nome de usuário: ")
                if adm_input.lower() == "voltar":
                    break
                if adm_input == adm:
                    adm_passinput = getpass.getpass("Digite sua senha: ")
                    if adm_passinput == admpass:
                        print("\n***** Login efetuado com sucesso! *****\n")

                        while True:
                            esc = input(
                                "Digite a região que você gostaria de verificar:\n1. Zona Norte\n2. Zona Oeste\n3. Zona Sul\n4. Zona Leste\n5. Adicionar Vaso\n6. Voltar ao Menu Inicial\n7. Sair\n")
                            def exibir_feedbacks_ordem(zona):
                                print(f"Feedbacks para a zona: {zona}")
                                for vaso, feedback in feedbacks[zona].items():
                                    notas = feedback['notas']
                                    comentarios = feedback['comentarios']
                                    if notas:
                                        media = sum(notas) / len(notas)
                                        print(f"Vaso: {vaso} - Média de nota: {media:.2f}")
                                    else:
                                        print(f"Vaso: {vaso} - Nenhum feedback registrado")
                                    if comentarios:
                                        print(f"Comentários para o vaso {vaso}:")
                                        for comentario in comentarios:
                                            print(comentario)
                                    else:
                                        print(f"Nenhum comentário registrado para o vaso {vaso}")

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
                                zona = input("Digite o nome da zona em que deseja adicionar o vaso: ")
                                if zona in zonas:
                                    vaso = input("Digite o nome do vaso: ")
                                    feedbacks[zona][vaso] = {'notas': [], 'comentarios': []}
                                    print("Vaso adicionado com sucesso!")
                                else:
                                    print("Zona inválida. Tente novamente.")
                            elif esc == "6":
                                break
                            elif esc == "7":
                                print(f"{msg}, muito obrigado!")
                                exit()
                            else:
                                print("Opção inválida. Tente novamente.")

                    else:
                        print("Senha incorreta!")
                    break
                break
            break

    elif opc == "2":
        # Aqui começa a parte do cliente
        print("Olá, cliente!")
        zona_escolhida = None

        # Exibir lista de zonas disponíveis
        print("Zonas disponíveis:")
        for i, zona in enumerate(zonas):
            print(f"{i + 1}. {zona}")

        while True:
            esc = input("Digite o número da zona que você deseja fornecer feedback (ou 'sair' para voltar ao menu): ")

            if esc.lower() == "sair":
                break

            if esc.isdigit() and 1 <= int(esc) <= 4:
                zona_escolhida = zonas[int(esc) - 1]
                break
            else:
                print("Opção inválida. Tente novamente.")

        if zona_escolhida:
            print(f"\nVocê selecionou a zona: {zona_escolhida}\n")
            print("Vasos disponíveis:")
            for i, vaso in enumerate(feedbacks[zona_escolhida].keys()):
                print(f"{i + 1}. {vaso}")

            while True:
                esc_vaso = input(
                    "Digite o número do vaso que você deseja fornecer feedback (ou 'sair' para voltar ao menu): ")

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
