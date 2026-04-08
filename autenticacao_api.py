# Biblioteca para geração de tokens seguros
import secrets
import string

def gerar_token_seguro(tamanho=32):
    # Define os caracteres permitidos para o token
    caracteres = string.ascii_letters + string.digits + "!@#$%_"
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))

print(gerar_token_seguro())