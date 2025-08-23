#While - else

string = 'Breno Carvalho'

i = 0

while i < len(string):
    lerta = string[i]
    i += 1

    if lerta == ' ':
        continue
    #break dentro do while o else não é executado.

    print(lerta)
else: 
    print('Acabou')