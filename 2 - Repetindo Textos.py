#Vamos solicitar uma string e um número inteiro como entrada. 
#Depois teremos que retornar a string repetida o número de vezes informado.

texto = input("Digite um texto para ser repetido:")
num = int(input("Digite um número de vezes que o texto deve ser repetido:"))

resultado = texto * num
print("O texto repetido é:", resultado)