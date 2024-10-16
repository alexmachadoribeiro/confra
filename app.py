import os

votos = {}

if __name__ == "__main__":
    while True:
        print("0 - Encerrar programa.")
        print("1 - Cadastrar opção.")
        print("2 - Votar.")
        print("3 - Exibir votos.")

        operacao = input("Informe a operação: ")

        os.system("cls")

        match operacao:
            case "0":
                break
            case "1":
                nova_opcao = input("Informe o nome da opção: ").lower()
                votos[nova_opcao] = 0
                print(f"Opção {nova_opcao} cadastrada com sucesso.")
                continue
            case "2":
                # exibe a lista de opções de voto
                for opcao in votos:
                    print(f"{opcao}")

                # usuário informa a sua opção de voto
                voto = input("Informe o voto: ").lower()

                # verifica se a opção de voto foi cadastrada
                if voto in votos:
                    # computa voto
                    votos[voto] += 1
                    print(f"Voto computado em {voto}.")
                else:
                    # não computa voto em caso de erro
                    print("Voto não computado.")
                
                # volta para o início do loop
                continue
            case "3":
                # ordena os votos com base em seus valores e os exibe
                for opcao in sorted(votos, key=votos.get, reverse=True):
                    print(f"{opcao}: {votos[opcao]}.")
                
                # volta para o início do loop
                continue
            case _:
                print("Opção inválida.")
                continue