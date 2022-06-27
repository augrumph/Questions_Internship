numero = int(input("Digite aqui o numero desejado : "))
termos = 11
lista = []

n1, n2 = 0, 1
contador = 0

while contador < termos:
    lista.append(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    contador += 1

if numero in lista:
    print("O numero {} se encontra dentro da sequencia !!".format(numero))
else:
    print("O numero {} NÃO esta dentro da sequencia !!".format(numero))
