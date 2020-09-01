questions = ["Telefonou para a vítima?",
            "Esteve no local do crime?",
            "Mora perto da vítima?",
            "Devia para a vítima?",
            "Já trabalhou com a vítima?"]
cont_yes = 0
for question in questions:
    resp = str(input(question )).upper()
    if resp == "S":
        cont_yes += 1

list_class = ["Suspeito", "Cúmplice", "Assassino", "Inocente"]
if cont_yes == 2:
    print("Você é: " + list_class[0])
elif cont_yes == 3 or cont_yes == 4:
    print("Você é: " + list_class[1])
elif cont_yes == 5:
    print("Você é: " + list_class[2])
else:
    print("Você é: " + list_class[3])

