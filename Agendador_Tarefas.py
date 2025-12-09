# Sistema de Gerenciamento de Tarefas
# Autor: Mikael Pereira
# Projeto para portfólio

import json
import os

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)


def adicionar_tarefa():
    descricao = input("Descrição da tarefa: ")
    tarefas = carregar_tarefas()
    nova = {"descricao": descricao, "status": "pendente"}
    tarefas.append(nova)
    salvar_tarefas(tarefas)
    print("✓ Tarefa adicionada!")


def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n=== LISTA DE TAREFAS ===")
    for i, t in enumerate(tarefas):
        print(f"{i+1}. {t['descricao']} - {t['status']}")


def marcar_concluida():
    listar_tarefas()
    tarefas = carregar_tarefas()
    idx = int(input("Número da tarefa concluída: ")) - 1

    if 0 <= idx < len(tarefas):
        tarefas[idx]["status"] = "concluída"
        salvar_tarefas(tarefas)
        print("✓ Tarefa marcada como concluída!")
    else:
        print("Índice inválido.")


def remover_tarefa():
    listar_tarefas()
    tarefas = carregar_tarefas()
    idx = int(input("Número da tarefa para remover: ")) - 1

    if 0 <= idx < len(tarefas):
        tarefas.pop(idx)
        salvar_tarefas(tarefas)
        print("✓ Tarefa removida!")
    else:
        print("Índice inválido.")


def menu():
    while True:
        print("\n=== SISTEMA DE TAREFAS ===")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Marcar como concluída")
        print("4 - Remover tarefa")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_concluida()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()