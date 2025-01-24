my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for numero in my_list:
    if numero not in new_list:
        new_list.append(numero)
new_list.sort()
print("A lista com os elementos exclusivos aqui")
print (new_list)
