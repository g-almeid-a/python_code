import random

menu = """

SORTEIO DE NOMES

[1] Inserir nome na lista
[2] Sortear um nome
[3] Remover um nome inserido
[4] Sair

=> """

lista_nome = []

def remove_lista():
    global lista_nome
    del lista_nome

def remove_nome():
    global lista_nome
    nome = input("Digite o nome a ser removido: ")
    if nome not in lista_nome:
        print(f"\n{nome} não está na lista.")
    else:
        lista_nome.remove(nome)
    print(f"\n{nome} foi removido do sorteio. \n\nLista atual: {lista_nome}")

while True:
    opcao = input(menu)

    if opcao == '1':
        nome = input("Digite o nome a ser inserido: ")
        lista_nome.append(nome)
        print(f"\n{nome} foi adicionado à lista.")
        print(f"\nLista atual: {lista_nome}")
        continue

    elif opcao == '2':
        if not lista_nome:
            print("A lista de nomes está vazia. Insira nomes antes de sortear.")
        elif len(lista_nome) == 1:
            print(f"\nQuantidade de nomes mínimos para sortear: 2! Insira mais um nome para realizar o sorteio.")
        else:
            nome_sorteado = random.choice(lista_nome)
            print(f"\nO nome sorteado é: {nome_sorteado}")
            lista_nome.remove(nome_sorteado)
            print(f"\nLista atual: {lista_nome}")
            if not lista_nome:
                print("\nTodos os nomes foram sorteados. A lista está vazia.")
                remove_lista()
            continue
    
    elif opcao == '3':
        if not lista_nome:
            print("\nNão há nomes na lista para remover.")
            continue
        remove_nome()

    elif opcao == '4':
        print("\nEncerrando o programa. Até mais!")
        remove_lista()
        break