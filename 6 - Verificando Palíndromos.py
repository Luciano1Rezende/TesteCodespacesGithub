# Vamos testar se uma palavra é um palíndromo

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
palavra3 = input("Digite a terceira palavra: ")

def eh_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()  # Remover espaços e converter para minúsculas
    return palavra == palavra[::-1] # Verifica se a palavra é igual ao seu reverso

print(f"A palavra '{palavra1}' é um palíndromo? {'Sim' if eh_palindromo(palavra1) else 'Não'}")
print(f"A palavra '{palavra2}' é um palíndromo? {'Sim' if eh_palindromo(palavra2) else 'Não'}")
print(f"A palavra '{palavra3}' é um palíndromo? {'Sim' if eh_palindromo(palavra3) else 'Não'}")
