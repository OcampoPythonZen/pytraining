import json

dict_ = {}
dict_.update({
    'a': {
        'val1' : 1,
        'val2' : 2,
        #b'val1' : 1, demostracion del bytecode para dict no es permitido
        #b'val2' : 2,
        }
    })

lista_palabras = ['pepe','pecas','pica','papas','con','un']

nuevo_dicc = {}

for word in lista_palabras:
    print('iteracion')
    if str(len(word)) not in nuevo_dicc:
        nuevo_dicc[str(len(word))] = []
    nuevo_dicc[str(len(word))].append(word)

# print(nuevo_dicc)

def word_in_letter(n):
    new_lista = []
    for i in lista_palabras:
        print('iteracion')
        if len(i) == n:
            new_lista.append(i)   
    return new_lista

def dict_in_letter(n):
    if str(n) in nuevo_dicc:
        return nuevo_dicc[str(n)]
    else:
        return 'No hay palabras!'

#La rápidez de los diccionarios
print(dict_in_letter(5))
print(dict_in_letter(4))
print(dict_in_letter(3))

print(dict_in_letter(2))

# Esta es la lentitud de las listas
# print(word_in_letter(4))
# print(word_in_letter(5))
# print(word_in_letter(3))

# print(dict_)
# print(json.dumps(dict_))