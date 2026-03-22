arquivo_tarefas = "tarefas.txt"

def adicionar_tarefa():
    tarefa = input("Digite uma tarefa: ")
    tarefa_lower = tarefa.lower()

    palavras_alta = ["estudar", "trabalhar"]
    palavras_baixa = ["jogar", "assistir"]

    prioridade = "MEDIA"

    for palavra in palavras_alta:
        if palavra in tarefa_lower:
            prioridade = "ALTA"

    for palavra in palavras_baixa:
        if palavra in tarefa_lower and prioridade != "ALTA":
            prioridade = "BAIXA"

    with open(arquivo_tarefas, "a") as arquivo:
        arquivo.write(f"[{prioridade}] {tarefa}\n")

    print("Tarefa adicionada com prioridade:", prioridade)


def ver_tarefas():
    try:
        with open(arquivo_tarefas, "r") as arquivo:
            tarefas = arquivo.readlines()

        if not tarefas:
            print("Nenhuma tarefa encontrada.")
            return

        for i, t in enumerate(tarefas):
            print(i + 1, "-", t.strip())

    except:
        print("Erro ao ler tarefas.")


def remover_tarefa():
    try:
        with open(arquivo_tarefas, "r") as arquivo:
            tarefas = arquivo.readlines()

        for i, t in enumerate(tarefas):
            print(i + 1, "-", t.strip())

        numero = int(input("Digite o número da tarefa para remover: "))

        confirmar = input("Tem certeza? (s/n): ")

        if confirmar == "s":
            tarefas.pop(numero - 1)

            with open(arquivo_tarefas, "w") as arquivo:
                for t in tarefas:
                    arquivo.write(t)

            print("Tarefa removida!")

    except:
        print("Erro ao remover tarefa.")


def analisar():
    try:
        with open(arquivo_tarefas, "r") as arquivo:
            tarefas = arquivo.readlines()

        pontuacao = 0

        for linha in tarefas:
            if "[ALTA]" in linha:
                pontuacao += 2
            elif "[BAIXA]" in linha:
                pontuacao -= 1

        if pontuacao >= 5:
            nivel = "FOCADO"
        elif pontuacao >= 2:
            nivel = "PRODUTIVO"
        else:
            nivel = "DESORGANIZADO"

        print("\nPontuação:", pontuacao)
        print("Nível:", nivel)

    except:
        print("Erro ao analisar tarefas.")


while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Analisar")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        ver_tarefas()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        analisar()
    elif opcao == "0":
        break
    else:
        print("Opção inválida")
