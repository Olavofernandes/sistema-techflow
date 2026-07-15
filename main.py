class GerenciadorTarefas:
    def __init__(self):
        # Dicionário para armazenar as tarefas em memória
        self.tarefas = {}
        self.proximo_id = 1

    # RF01 - Cadastrar tarefa
    def cadastrar_tarefa(self, titulo, descricao):
        tarefa = {
            "id": self.proximo_id,
            "titulo": titulo,
            "descricao": descricao,
            "status": "To Do", # Status inicial padrão (Kanban)
            "prioridade": "Baixa" # Prioridade padrão (Mudança de Escopo)
        }
        self.tarefas[self.proximo_id] = tarefa
        self.proximo_id += 1
        return tarefa

    # RF02 - Editar tarefa
    def editar_tarefa(self, id_tarefa, novo_titulo, nova_descricao):
        if id_tarefa in self.tarefas:
            self.tarefas[id_tarefa]["titulo"] = novo_titulo
            self.tarefas[id_tarefa]["descricao"] = nova_descricao
            return self.tarefas[id_tarefa]
        return None

    # RF03 - Excluir tarefa
    def excluir_tarefa(self, id_tarefa):
        if id_tarefa in self.tarefas:
            return self.tarefas.pop(id_tarefa)
        return None

    # RF04 - Listar tarefas
    def listar_tarefas(self):
        return list(self.tarefas.values())

    # RF05 - Alterar status (Kanban: To Do, In Progress, Done)
    def alterar_status(self, id_tarefa, novo_status):
        status_permitidos = ["To Do", "In Progress", "Done"]
        if id_tarefa in self.tarefas and novo_status in status_permitidos:
            self.tarefas[id_tarefa]["status"] = novo_status
            return self.tarefas[id_tarefa]
        return None

    # RF06 - Definir prioridade (Mudança de Escopo: Alta, Média, Baixa)
    def definir_prioridade(self, id_tarefa, nova_prioridade):
        prioridades_permitidas = ["Alta", "Média", "Baixa"]
        if id_tarefa in self.tarefas and nova_prioridade in prioridades_permitidas:
            self.tarefas[id_tarefa]["prioridade"] = nova_prioridade
            return self.tarefas[id_tarefa]
        return None