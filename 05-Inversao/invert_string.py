print("###### PALAVRA INVERTIDA ########")
str = input("Digite uma palavra : ")
invertida = ""
for i in range(len(str) - 1, -1, -1):
    invertida += str[i]

print("String invertida:", invertida)
