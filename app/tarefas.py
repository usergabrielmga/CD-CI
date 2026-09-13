tarefas = []


def adicionar_tarefa(tarefa):
    tarefas.append({
        "nome": tarefa,
        "concluida": False
    })


def listar_tarefas():
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n========== MINHAS TAREFAS ==========")

    for i, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["concluida"] else " "

        print(f"{i}. [{status}] {tarefa['nome']}")


def concluir_tarefa(numero):
    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]["concluida"] = True
        print("\nTarefa concluída com sucesso!")
    else:
        print("\nTarefa não encontrada.")