list = []
questions = [
    "Quantidade de valores: ",
    "Lista original: ",
    "Lista inversa: ",
    "Soma dos valores: ",
    "Média dos valores: ",
    "Valores acima da média: ",
    "Valores abaixo de 7: "
]
list_maior_que_a_media = []
lista_maior_que_7 = []
while True:
    enter = float(input("Enter: "))
    list.append(enter)
    if enter == -1:
        break
list.pop()
soma = sum(list)
media = soma / len(list)
for num in list:
    if num > media:
        list_maior_que_a_media.append(num)
    if num < 7:
        lista_maior_que_7.append(num)

print(questions[0], len(list))
print(questions[1], list)
list.reverse()
print(questions[2])
for n in list:
    print(n)
print(questions[3], soma)
print(questions[4], media)
print(questions[5], list_maior_que_a_media)
print(questions[6], lista_maior_que_7)
print("Obrigado e volte sempre!")
