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
                for opcao in votos:
                    print(f"{opcao}")
                voto = input("Informe o voto: ").lower()
                if voto in votos:
                    votos[voto] += 1
                    print(f"Voto computado em {voto}.")
                else:
                    print("Voto não computado.")
                continue
            case "3":
                for opcao in sorted(votos, key=votos.get, reverse=True):
                    print(f"{opcao}: {votos[opcao]}.")
                continue
            case _:
                print("Opção inválida.")
                continue