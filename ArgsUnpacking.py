# uso de los operadores * y ** para desempaquetar lista y diccionarios
# respectivamente ya que las funciones pasan parametros de un solo valor normalmente
# y con estos operadores podemos pasar una secuencia de parametros o valores asignados

def vector(x,y,z):
    return '<%s, %s, %s>' % (x,y,z)

if __name__ == "__main__":

    tuple_vector = (1,0,-1)
    list_vector = [1,0,-1]
    dict_vector = {
        'x' : 1,
        'y' : 0,
        'z' : -1
    }

    #print(vector(tuple_vector[0],tuple_vector[1],tuple_vector[2]))
    print(vector(*tuple_vector))
    #print(vector(list_vector[0],list_vector[1],list_vector[2]))
    print(vector(*list_vector))
    #print(vector(dict_vector['x'],dict_vector['y'],dict_vector['z']))
    print(vector(**dict_vector))
    #-----------------------------------


