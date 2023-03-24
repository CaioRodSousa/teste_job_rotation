# Questão 1
print("Questão 1")

indice = 13
soma = 0
k = 0

while k < indice :
    k = k+1

    soma = soma+k

print("a resposta da questão é: ")
print(soma)

#Questão 2
print("Questão 2")
# Pede ao usuário para informar um número
numero = int(input("Digite um número inteiro positivo: "))

# Inicializa as variáveis de Fibonacci
fib1 = 0
fib2 = 1
fib = fib1 + fib2

# Calcula a sequência de Fibonacci até o número informado pelo usuário
while fib <= numero:
    if fib == numero:
        print(f"O número {numero} pertence à sequência de Fibonacci!")
        break
    fib1 = fib2
    fib2 = fib
    fib = fib1 + fib2
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

#Questão 3
print("Questão 3")
print("a: o proximo numero será 9")
print("b: o proximo numero será 128")
print("c: o proximo numero será 49")
print("d: o proximo numero será 100")
print("e: o proximo numero será 13")
print("b: o proximo numero será 20")

#Questão 4
print("Questão 4")
"""
primeiro irei calcular quanto tempo cada um demora para pecorrer os 50 km
que é a metade do percuso completo(100km):

tempo do carro: distância/velocidade
tempo do carro: 50 / 110
tempo do carro: 0,4545 horas

agora o caminhão terá um tempo pouco maior por causa dos dois pedágios, somando
os dois pedágios da 10 min, convertendo pra horas da 0,1667 logo:

tempo do caminhão: distância/velocidade
tempo do caminhão: 50 / 80 + 0,1667
tempo do caminhão: 0,7083 horas

Como o carro leva menos tempo para percorrer a distância até o ponto de encontro, 
ele estará mais próximo da cidade de Ribeirão Preto no momento em que se cruzarem.
"""
print("o carro estará mais proximo de ribeirão preto quando ocorrer o encontro")

#Questão 5
print("Questão 5")

# Definindo a string a ser invertida
string = "flamengo"

# Convertendo a string para uma lista de caracteres
lista = list(string)

# Invertendo a lista de caracteres
tamanho = len(lista)
for i in range(tamanho // 2):
    temp = lista[i]
    lista[i] = lista[tamanho - i - 1]
    lista[tamanho - i - 1] = temp

# Convertendo a lista de volta para uma string
string_invertida = "".join(lista)

# Imprimindo a string invertida
print(string_invertida)