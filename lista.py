# Item é obrigatório, lista é opcional
def adicionar_item(item, lista=None):
    # Cria uma lista vazia se nenhuma lista for fornecida
    if lista is None:
        lista = []
        # Adiciona o item ao final da lista
    lista.append(item)
    return lista

print(adicionar_item(1))
print(adicionar_item(2))

# Adiciona um item a uma lista existente
print(adicionar_item(item= 3, lista= [1, 2]))