"""
Gerenciador de Tarefas (Task Manager)

Este programa implementa um gerenciador simples de tarefas no terminal.
Ele permite ao usuário adicionar, visualizar e remover tarefas de uma lista utilizando um menu interativo.

Funcionalidades:
- Adicionar novas tarefas
- Visualizar tarefas armazenadas
- Remover tarefas pelo número correspondente
- Encerrar o programa

Conceitos praticados:
- Manipulação de listas
- Estruturas de repetição (loops)
- Estruturas condicionais
- Organização de código com funções
- Validação de entrada do usuário

Este projeto foi desenvolvido como exercício prático para treinar lógica de programação e boas práticas em Python.
"""
TITULO = "Gerenciador de Tarefas"
TAMANHO_LINHA = 78


def exibir_menu():
    """Exibe o menu principal do gerenciador de tarefas."""
    print(TAMANHO_LINHA * "=")
    print(TITULO.center(TAMANHO_LINHA))
    print(TAMANHO_LINHA * "=")
    print(
"""
1. Adicionar tarefa
2. Visualizar tarefas
3. Remover tarefa
4. Sair
"""
)
    print(TAMANHO_LINHA * "=")


def adicionar_tarefa(tarefas: list):
    """Solicita uma nova tarefa ao usuário e adiciona à lista de tarefas."""
    tarefa = input("Digite a tarefa: ").strip()

    if tarefa == "":
        print("Erro: A tarefa não pode ser vazia.")
        return

    tarefas.append(tarefa)
    print("Tarefa adicionada!")


def visualizar_tarefas(tarefas: list):
    """Lista todas as tarefas ao usuário."""
    if not tarefas:
        print("Não há tarefas cadastradas.")
        return

    print("Tarefas:")

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice}. {tarefa}")


def remover_tarefa(tarefas: list):
    """Solicita ao usuário o número de uma tarefa e a remove da lista."""
    if not tarefas:
        print("Erro: Nenhuma tarefa para remover.")
        return

    try:
        numero_tarefa = int(input("Digite o número da tarefa a ser removida: "))
        indice_real = numero_tarefa - 1

        if indice_real < 0 or indice_real >= len(tarefas):
            print("Erro: Número de tarefa inválido.")
            return

        tarefa_removida = tarefas.pop(indice_real)
        print(f"Tarefa '{tarefa_removida}' removida!")

    except ValueError:
        print("Erro: Entrada inválida! Digite um número.")


def main():
    """Função principal que executa o fluxo do programa."""
    tarefas = []

    while True:
        exibir_menu()
        opcao_usuario = input("Escolha uma opção: ").strip()

        if opcao_usuario == "1":
            adicionar_tarefa(tarefas)

        elif opcao_usuario == "2":
            visualizar_tarefas(tarefas)

        elif opcao_usuario == "3":
            remover_tarefa(tarefas)

        elif opcao_usuario == "4":
            print("Saindo do gerenciador de tarefas. Até mais!")
            break

        else:
            print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")


if __name__ == '__main__':
    main()
