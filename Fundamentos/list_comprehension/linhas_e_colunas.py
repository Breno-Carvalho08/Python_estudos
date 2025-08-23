#For aninhado - Normal
# for x in range(3):
#     for y in range(5):
#         print((x, y))

#For aninhado - List Comprehension
linhas_e_colunas = [
    (x, y)
    if y != 1 else (x * 10, y * 10)
    for x in range(3)
    for y in range(5)
    
]

print(linhas_e_colunas)