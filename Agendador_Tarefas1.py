import json
import os

ARQ_TAREFA = "tarefas.json"

def carregar_tarefas():
    if not os.path.exists(ARQ_TAREFA):
        return []
    with open(ARQ_TAREFA, "r", encoding="utf-8") as f:
        return json.load(f)
    
def salvar_tarefas(tarefas):
    with open (ARQ_TAREFA, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)       

def adicionar_tarefa():
    descricao = input("Descrição da tarefa: ")
    tarefas = carregar_tarefas()
    nova = {"descrição": descricao, "status": "pendente"}
    tarefas.append(nova)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")


def listar_tarefa():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("\n===LISTA DE TAREFAS===\n")
    for i, t in enumerate(tarefas):
        print(f"{i+1}. {t['descrição']} - {t['status']}")

def marcar_concluida():
    listar_tarefa()
    tarefas = carregar_tarefas()
    idx = int(input("Número da tarefa concluída: ")) - 1

    if 0 <= idx < len(tarefas):
        tarefas[idx]["status"] = "concluída"
        salvar_tarefas(tarefas)
        print("Tarefa concluída com sucesso!")
    else:
        print("Número invalído")

def remover_tarefa():
    listar_tarefa()
    tarefas = carregar_tarefas()
    idx = int(input("Número da tarefa para remover: ")) - 1

    if 0 <= idx < len(tarefas):
        tarefas.pop(idx)
        salvar_tarefas(tarefas)
        print("Tarefas removida com sucesso!")
    else:
        print("Número inválido!") 
        
def menu():
    while True:
        print("\n===AGENDADOR DE TAREFAS===\n")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefa")
        print("3 - Marcar como concluída")
        print("4 - Remover Tarefa")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefa()
        elif opcao == "3":
            marcar_concluida()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            print("Saindo do sistema")
            break
        else:
            print("opção inválida")
        
if __name__ == "__main__":
    menu()