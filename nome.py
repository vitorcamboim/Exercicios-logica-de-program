# %%

primeiro_nome = input("Digite seu primeiro nome: ")

print(primeiro_nome)

# %%

nome = input("Digite seu primeiro nome: ")

sobrenome = input("Digite seu sobrenome: ")

print(nome, sobrenome)

# %%

print("""
.\      /.
 .\    /.
  .\  /.
  . \/.
  . /\.
 . /  \.
 ./    \.
./      \.
 """)

# %%


size = int(input("Digite o tamanho desejado: "))
def X(size = 21):
    if size % 2 == 0:
        size += 1

for i in range(size):
    for j in range(size):
        if j == i or j == (size - i - 1):
            print("#", end="")
        else:
            print(" ", end="")
    print()

X() 

# %%

dia = int(input("Digite seu dia de aniversário: "))
mes = int(input("Digite seu mês de aniversário: "))
mes *= 30
hoje = 122

data = dia + mes
falta = data - hoje

if falta >= 1:
    print("Faltam", falta, "dias para o seu aniversário!")

elif falta == 0:
    print("Hoje é seu aniversário, parabéns!")

else:
    print("Se passaram", abs(falta), "dias do seu aniversário!")

# %%

produto = int(input("Digite o preço do seu produto: "))

desconto = produto * 0.2
total = produto - desconto

print("Preço original do produto:", produto)
print("Você ganhou", desconto, "reais de desconto!")
print("Seu produto agora custa", total, "reais!")

# %%

valor = int(input("Digite o valor do seu produto: "))
produto = int(input("Digite o desconto do seu produto sem o sinal de porcentagem: "))
produto /= 100
desconto = valor * produto
total = valor - desconto

print("Preço original do produto:", valor)
print("Você ganhou", desconto, "reais de desconto!")
print("Seu produto agora custa", total, "reais!")

# %%

lista = []

for i in range(0,4):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    
media = sum(lista) / len(lista)
variancia = (((lista[0] - media)**2) + ((lista[1] - media)**2) + ((lista[2] - media)**2) + ((lista[3] - media)**2)) / len(lista)

print("Média aritmédica simples:", sum(lista) / len(lista))

print("Média geométrica:", (lista[0] * lista[1] * lista[2] * lista[3])**(1/4))

print("Média harmônica:", len(lista) / ( (lista[0]**-1) + (lista[1]**-1) + (lista[2]**-1) + (lista[3]**-1) ) )

print("Variância:", (((lista[0] - media)**2) + ((lista[1] - media)**2) + ((lista[2] - media)**2) + ((lista[3] - media)**2)) / len(lista) )

print("Desvio padrão:", variancia ** 1/2)

# %%

lista = []

for i in range(0,3):
    numero = int(input("Digite um número para descobrir o maior e colocá-los em ordem: "))
    lista.append(numero)

print(max(lista))

lista.sort()

print(lista)

# %%

lista = []

for i in range(0,3):
    numero = input("Digite palavras para colocá-las em ordem: ")
    lista.append(numero)

lista.sort()

print(lista)

# %%

genero = int(input("Se você é homem, digite 1, se é mulher, digite 2."))
peso = float(input("Digite seu peso em quilos, dividindo o quilo e as gramas por um ponto: "))
altura = float(input("Digite sua altura em metros, dividindo o metro e os cm por um ponto: "))
idade = int(input("Digite sua idade: "))

if genero == 1:
    tmbhomem = 66.47 + (13.75 * peso) + (5.003 * altura) - (6.755 * idade)
    print("seu TBM é igual a", tmbhomem, "calorias")
elif genero == 2:
    tmbmulher = 655.09 + (9.563 * peso) + (1.85 * altura) - (4.676 * idade)
    print("seu TBM é igual a", tmbmulher, "calorias")
else:
    print("Digite o número do gênero corretamente!")

# %%

numero = int(input("Digite um número inteiro: "))

print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

# %%

numero = int(input("Digite um número: "))
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)

# %%











