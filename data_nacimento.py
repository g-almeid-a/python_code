# Bibliotexa para manipulação de datas
from datetime import datetime

while True:
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

    try:
        #Converte a string de data de nasciimento para um objeto datetime para calcular a idade
        nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        hoje = datetime.today()

        idade = hoje.year - nascimento.year

        # Verifica se o aniversário já ocorreu este ano, caso contrário, subtrai um ano da idade
        if hoje < nascimento.replace(year=hoje.year):
            idade -= 1

        print(f"A idade do usuário é: {idade} anos.")
        break
    except ValueError:
        print("Data de nascimento inválida. Por favor, tente novamente.")