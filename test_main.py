from app.tarefas import (
    tarefas,
    adicionar_tarefa,
    concluir_tarefa
)


def limpar_tarefas():
    tarefas.clear()


def test_adicionar_tarefa():
    limpar_tarefas()

    adicionar_tarefa("Estudar Python")

    assert len(tarefas) == 1
    assert tarefas[0]["nome"] == "Estudar Python"
    assert tarefas[0]["concluida"] is False


def test_adicionar_duas_tarefas():
    limpar_tarefas()

    adicionar_tarefa("Estudar Python")
    adicionar_tarefa("Aprender Docker")

    assert len(tarefas) == 2


def test_tarefa_inicia_nao_concluida():
    limpar_tarefas()

    adicionar_tarefa("Fazer atividade")

    assert tarefas[0]["concluida"] is False


def test_concluir_tarefa():
    limpar_tarefas()

    adicionar_tarefa("Estudar pytest")
    concluir_tarefa(1)

    assert tarefas[0]["concluida"] is True


def test_concluir_tarefa_invalida():
    limpar_tarefas()

    adicionar_tarefa("Estudar GitHub Actions")
    concluir_tarefa(5)

    assert tarefas[0]["concluida"] is False