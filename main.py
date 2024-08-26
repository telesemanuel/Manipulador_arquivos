import os

def mostrar_menu():
    print("1 - Ler arquivo")
    print("2 - Gravar novos dados")
    print("3 - Sair Programa")

def gravar_arquivos(dados, nome, email, profissao):
    dados += f"\n\n{"-"*30}\n\nNome: {nome}\nE-mail: {email}\nProfissão: {profissao}"
    with open("arquivo.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)


# funcao leitura
def ler_arquivos():
    with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
        dados = arquivo.read()
    return dados


# Programa Principal
if __name__ == "__main__":
    while True:
        dados = ler_arquivos()
        mostrar_menu()
        opcao = input("Escolha uma Opção: ")
        os.system("cls")
        match opcao:
            case "1":
                print(f"\n{dados}\n")
                continue
            case "2":
                print("NOVO CADASTRO:\n")
                novo_nome = input("Informe o nome do usúario: ")
                novo_email = input("Informe o email do usúario: ")
                nova_profissao = input("Informe a profissao do usúario: ")
                print(" ")
                gravar_arquivos(dados, novo_nome, novo_email, nova_profissao)
                continue
            case"3":
                print("saindo...")
                break
            case _:
                print("Opção Inválida")
                continue