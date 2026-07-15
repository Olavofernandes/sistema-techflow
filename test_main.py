import pytest
from main import GerenciadorTarefas

# Cria uma nova instância do gerenciador para cada teste, garantindo que um teste não interfira no outro
@pytest.fixture
def gerenciador():
    return GerenciadorTarefas()

# Teste do RF01 e RF04 - Cadastrar e Listar Tarefas
def test_cadastrar_e_listar_tarefa(gerenciador):
    tarefa = gerenciador.cadastrar_tarefa("Fazer o trabalho da faculdade", "Terminar a documentação")
    
    assert tarefa["id"] == 1
    assert tarefa["titulo"] == "Fazer o trabalho da faculdade"
    assert tarefa["status"] == "To Do"  # Verifica o status padrão
    assert len(gerenciador.listar_tarefas()) == 1

# Teste do RF02 - Editar Tarefa
def test_editar_tarefa(gerenciador):
    gerenciador.cadastrar_tarefa("Estudar Python", "Revisar listas")
    tarefa_editada = gerenciador.editar_tarefa(1, "Estudar PyTest", "Revisar testes automatizados")
    
    assert tarefa_editada["titulo"] == "Estudar PyTest"
    assert tarefa_editada["descricao"] == "Revisar testes automatizados"

# Teste do RF03 - Excluir Tarefa
def test_excluir_tarefa(gerenciador):
    gerenciador.cadastrar_tarefa("Tarefa para excluir", "Descrição qualquer")
    gerenciador.excluir_tarefa(1)
    
    assert len(gerenciador.listar_tarefas()) == 0

# Teste do RF05 - Alterar Status (Fluxo Kanban)
def test_alterar_status(gerenciador):
    gerenciador.cadastrar_tarefa("Tarefa Kanban", "Testar status")
    tarefa = gerenciador.alterar_status(1, "In Progress")
    
    assert tarefa["status"] == "In Progress"

# Teste do RF06 e Mudança de Escopo - Definir Prioridade
def test_definir_prioridade(gerenciador):
    gerenciador.cadastrar_tarefa("Tarefa Urgente", "Testar prioridade")
    tarefa = gerenciador.definir_prioridade(1, "Alta")
    
    assert tarefa["prioridade"] == "Alta"