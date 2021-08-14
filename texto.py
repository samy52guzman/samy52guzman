c = "la tutoria de la mayoria de los abogados no es cien por ciento efectiva debido que es suministrada por alguien " \
    "que no tiene la total capacidad con el tema "


def buscar():
    search = input("que palabra desea buscar: ")

    if search in c:
        print("si")
    else:
        print("no se encuentra")


def cantidad_de_palabras():
    cantidad = 0
    for x in c:
        if x == " ":
            cantidad += 1
    return cantidad


def palabra_que_comienza():
    k = []
    f = 0
    k.append(c[0])
    for m in c:
        if m == " ":
            k.append(c[f + 1])
        elif f == (len(c) - 2):
            break
        f += 1
    print(k)


def palabra_que_termina():
    t = 0
    s = []
    for v in c:
        if t < (len(c) -1):
            if c[t + 1] == " ":
                s.append(v)
        elif t == (len(c) - 2):
            break
        t += 1
    print(s)

def vocales_en_parrafo():
    p =["a","e","i","o","u","A","E","I","O","U"]
    t = []
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for w in c:
        if w in p:
            if w == p[0]:
                a += 1

            elif w == p[1]:
                e += 1

            elif w == p[2]:
                i += 1

            elif w == p[3]:
                o += 1

            elif w == p[4]:
                u += 1

    t.append(f'Hay {a} a en el texto')
    t.append(f'Hay {e} e en el texto')
    t.append(f'Hay {i} i en el texto')
    t.append(f'Hay {o} o en el texto')
    t.append(f'Hay {u} u en el texto')
    print(t)
