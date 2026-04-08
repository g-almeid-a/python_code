nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"{nome}, você é maior de idade. Seja bem vindo(a)!")
elif idade >= 16:
    print(f"{nome}, você é menor de idade, mas pode entrar acompanhado dos pais. Seja bem vindo(a)!")
else: 
    print(f"{nome}, você é menor de idade e não pode entrar. Desculpe!")