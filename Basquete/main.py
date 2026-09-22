def registrarTentativas():
    tentativas = []

    for i in range(10):
        valor = input("Digite o resultado da tentativa " + str(i + 1) + ": ")

        while valor != "0" and valor != "1" and valor != "2" and valor != "3":
            print("Valor inválido. Digite 0, 1, 2 ou 3.")
            valor = input("Digite o resultado da tentativa " + str(i + 1) + ": ")

        tentativas.append(int(valor))

    return tentativas


def calcularPontuacao(tentativas):
    total = 0

    for tentativa in tentativas:
        total += tentativa

    return total


def calcularConvertidos(tentativas):
    convertidos = 0

    for tentativa in tentativas:
        if tentativa > 0:
            convertidos += 1

    return convertidos


def calcularErrados(tentativas):
    errados = 0

    for tentativa in tentativas:
        if tentativa == 0:
            errados += 1

    return errados


def calcularAproveitamento(convertidos):
    return (convertidos / 10) * 100


def encontrarCestaMaisFrequente(tentativas):
    cesta1 = 0
    cesta2 = 0
    cesta3 = 0

    for tentativa in tentativas:
        if tentativa == 1:
            cesta1 += 1
        elif tentativa == 2:
            cesta2 += 1
        elif tentativa == 3:
            cesta3 += 1

    maior = cesta1

    if cesta2 > maior:
        maior = cesta2

    if cesta3 > maior:
        maior = cesta3

    if maior == 0:
        return "Nenhuma cesta foi convertida."

    tipos = []

    if cesta1 == maior:
        tipos.append("1 ponto")

    if cesta2 == maior:
        tipos.append("2 pontos")

    if cesta3 == maior:
        tipos.append("3 pontos")

    if len(tipos) > 1:
        return "Empate entre: " + ", ".join(tipos)

    return "Cesta de " + tipos[0]


def mostrarRelatorio(tentativas):
    pontos = calcularPontuacao(tentativas)
    convertidos = calcularConvertidos(tentativas)
    errados = calcularErrados(tentativas)
    aproveitamento = calcularAproveitamento(convertidos)
    maisFrequente = encontrarCestaMaisFrequente(tentativas)

    print("\n--- RELATÓRIO ---")

    print("Tentativas:", tentativas)
    print("Pontuação total:", pontos)
    print("Arremessos convertidos:", convertidos)
    print("Arremessos errados:", errados)
    print("Aproveitamento:", aproveitamento, "%")
    print("Cesta mais frequente:", maisFrequente)

    print("-----------------\n")


def menu():
    while True:
        print("1 - Registrar tentativas")
        print("2 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tentativas = registrarTentativas()
            mostrarRelatorio(tentativas)

        elif opcao == "2":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.\n")


menu()