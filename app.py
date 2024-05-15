import os
import csv

restaurantes = (["Machado's Burgues"], ["BK"], ["Mac"], ["Bar do moe"])


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


def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))
    # opcao_escolhida = int(opcao_escolhida)

    if opcao_escolhida == 1:
        print("Cadastrar restaurante")
    elif opcao_escolhida == 2:
        print("Listar restaurantes")
    elif opcao_escolhida == 3:
        print("Ativar restaurante")
    else:
        finalizar_app()


def salva_restaurantes():
    with open("restaurantes.csv", "w") as arquivo:
        escritor = csv.writer(arquivo)
        for linha in restaurantes:
            escritor.writerow(linha)


def escreve_restaurantes():
    with open("restaurantes.csv") as restaurantes:
        leitor = csv.reader(restaurantes)
        for linha in leitor:
            print(linha)


def main():
    salva_restaurantes()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
