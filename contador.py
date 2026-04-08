texto = input("Digite um texto: ")
vogais = "aeiouAEIOU"
contador = 0
vogais_encontradas = []

for letra in texto:
    if letra in vogais:
        contador += 1
        vogais_encontradas.append(letra)

print(f"O texto '{texto}' tem {contador} vogais: {', '.join(vogais_encontradas)}.")