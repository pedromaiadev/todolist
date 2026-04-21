# todo.py - Gerenciador de Tarefas simples em Python
 
tarefas = []
 
 
def adicionar_tarefa(descricao):
    """Adiciona uma nova tarefa à lista."""
    if not descricao or not descricao.strip():
        print("Erro: a descrição não pode ser vazia.")
        return False
    tarefa = {"id": len(tarefas) + 1, "descricao": descricao.strip(), "concluida": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")
    return True
 
 
def listar_tarefas():
    """Lista todas as tarefas."""
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    print("\n--- Lista de Tarefas ---")
    for tarefa in tarefas:
        status = "✓" if tarefa["concluida"] else "✗"
        print(f"[{status}] {tarefa['id']}. {tarefa['descricao']}")
    print("------------------------\n")
 
 
def concluir_tarefa(id_tarefa):
    """Marca uma tarefa como concluída."""
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            if tarefa["concluida"]:
                print(f"Tarefa {id_tarefa} já estava concluída.")
            else:
                tarefa["concluida"] = True
                print(f"Tarefa {id_tarefa} marcada como concluída!")
            return True
    print(f"Erro: tarefa com ID {id_tarefa} não encontrada.")
    return False
 
 
def remover_tarefa(id_tarefa):
    """Remove uma tarefa da lista."""
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefas.remove(tarefa)
            print(f"Tarefa {id_tarefa} removida com sucesso!")
            return True
    print(f"Erro: tarefa com ID {id_tarefa} não encontrada.")
    return False
 
 
def menu():
    """Exibe o menu principal."""
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(descricao)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            listar_tarefas()
            try:
                id_tarefa = int(input("Digite o ID da tarefa a concluir: "))
                concluir_tarefa(id_tarefa)
            except ValueError:
                print("ID inválido. Digite um número.")
        elif opcao == "4":
            listar_tarefas()
            try:
                id_tarefa = int(input("Digite o ID da tarefa a remover: "))
                remover_tarefa(id_tarefa)
            except ValueError:
                print("ID inválido. Digite um número.")
        elif opcao == "5":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
 
 
if __name__ == "__main__":
    menu()