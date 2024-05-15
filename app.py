import os
import csv

restaurantes = [
    {"nome": "Praça", "categoria": "Japonesa", "ativo": "Inativo"},
    {"nome": "Pizza Superma", "categoria": "Pizza", "ativo": "Ativo"},
    {"nome": "Cantina", "categoria": "Italiano", "ativo": "Inativo"},
]


def exibir_nome_do_programa():
    print(
        """
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
"""
    )


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")


def finalizar_app():
    # Verifica se o sistema operacional é windows ou linux pelo nome dado ao sistema
    if os.name == "nt":  # nt para windows
        os.system("cls")
        print("This is a Windows system.")
        print(os.name)
    if os.name == "posix":  # posix para linux ou mac os
        os.system("clear")
        print("This is a Linux or MacOS system.")
        print(os.name)
    # os.system('clear')
    print("Finalizando o app")


def opcao_invalida():
    print("Opção inválida!\n")
    voltar_ao_menu_principal()


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu ")
    main()


def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")

    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)
    print()


def salva_restaurantes():
    with open("restaurantes.csv", "w") as arquivo:
        nome_do_campo = []
        for campo_restaurante in restaurantes[0].keys():
            nome_do_campo.append(campo_restaurante)

        print("nome do campo: {}".format(nome_do_campo))
        escritor = csv.DictWriter(arquivo, nome_do_campo)
        for restaurante in restaurantes:
            print("restaurante: {}".format(restaurante))
            escritor.writerow(restaurante)


def escreve_restaurantes():
    with open("restaurantes.csv") as restaurantes:
        leitor = csv.DictReader(restaurantes)
        for linha in leitor:
            print(linha)


def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes")

    for restaurante in restaurantes:
        print(f".{restaurante}")

    escreve_restaurantes()
    voltar_ao_menu_principal()


def main():
    os.system("clear")
    salva_restaurantes()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
