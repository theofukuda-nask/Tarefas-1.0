def calcularTotalGols(gols):
    total = 0
    for gol in gols:
        total += gol
    return total

def calcularMediaGols(gols):
    total = calcularTotalGols(gols)
    return total / len(gols)

def encontrarArtilheiros(jogadores, gols):
    maior = gols[0]
    artilheiros = []
    for gol in gols:
        if gol > maior:
            maior = gol
    for i in range(len(jogadores)):
        if gols[i] == maior:
            artilheiros.append(jogadores[i])
    return artilheiros

def mostrarRelatorio(jogadores, gols):
    total = calcularTotalGols(gols)
    media = calcularMediaGols(gols)
    artilheiros = encontrarArtilheiros(jogadores, gols)

    print("\n--- RELATÓRIO ---")
    print("Jogadores:")
    for i in range(len(jogadores)):
        print(jogadores[i], "-", gols[i], "gols")
        
    print("Total de gols:", total)
    print("Média de gols:", media)
    print("\nJogadores acima da média:")
    for i in range(len(jogadores)):
        if gols[i] > media:
            print(jogadores[i])

    if len(artilheiros) == 1:
        print("\nArtilheiro:", artilheiros[0])
    else:
        print("\nHouve empate na artilharia.")
        print("Artilheiros:", artilheiros)

    print("-----------------\n")


def registrarJogadores():
    jogadores = []
    gols = []

    for i in range(5):
        nome = input("Nome do jogador: ").strip()

        while nome == "":
            print("Erro: digite um nome.")
            nome = input("Nome do jogador: ").strip()

        quantidade = input("Quantidade de gols: ")

        while not quantidade.isdigit():
            print("Erro: digite um número inteiro.")
            quantidade = input("Quantidade de gols: ")

        quantidade = int(quantidade)

        jogadores.append(nome)
        gols.append(quantidade)

    return jogadores, gols


def menu():
    jogadores = []
    gols = []

    while True:
        print("1 - Registrar jogadores")
        print("2 - Mostrar relatório")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            jogadores, gols = registrarJogadores()
            print("Jogadores registrados!\n")

        elif opcao == "2":
            if len(jogadores) == 0:
                print("Nenhum jogador foi registrado.\n")
            else:
                mostrarRelatorio(jogadores, gols)

        elif opcao == "3":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.\n")


menu()
