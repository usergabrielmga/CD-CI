from app.tarefas import (
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa
)


def iniciar_aplicacao():

    print("=" * 40)
    print("       GERENCIADOR DE TAREFAS")
    print("=" * 40)

    adicionar_tarefa("Estudar Python")
    adicionar_tarefa("Aprender Docker")
    adicionar_tarefa("Enviar atividade da faculdade")

    listar_tarefas()

    print("\nConcluindo a segunda tarefa...")
    concluir_tarefa(2)

    listar_tarefas()

    print("\nAplicação executada com sucesso!")
    print("Projeto funcionando dentro do Docker.")

