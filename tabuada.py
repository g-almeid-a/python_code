print(""" 
      === Bem-vindo à tabuada! === 
      
      """)

nome = input("Digite o seu nome: ")

input("Pressione Enter para iniciar...")

while True:
    try:    
        num = int(input("Digite um número para ver a sua tabuada: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if num <= 0:
        print("Por favor, digite um número positivo.")
        continue

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
        continue

    resposta = input("Deseja ver a tabuada de outro número? (y/n): ").lower()
    
    if resposta == 'n':
        print(f"""
              
              ===Obrigado, {nome}, por usar a nossa tabuada! Até a próxima!===
              
              """)
        break