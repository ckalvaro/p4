class Lote:
    def __init__(self, nom_ape, n_manz, n_lote, orient, superf, monto):
        self.nombre = nom_ape
        self.n_manz = n_manz
        self.n_lote = n_lote
        self.orient = orient
        self.superf = superf
        self.monto = monto
        self.orient_string = self.orient_str(orient)


    def __str__(self):
        linea = "Dueño : {} - Manzana {} , Lote {} - Orientacion {} - Superf {} - Monto {}".format(self.nombre, self.n_manz, self.n_lote, self.orient_string, self.superf, self.monto)
        return linea

    def orient_str(self, orient):
        #(1: Norte, 2: Sur, 3: Este, 4:Oeste
        tupla = ("Norte", "Sur", "Este", "Oeste")
        return tupla[orient - 1]

def add_in_order(vec, lote):
    izq, der = 0, len(vec)-1
    while izq <= der:
        c = (izq+der)//2
        if vec[c].nombre == lote.nombre:
            pos = c
            break
        elif vec[c].nombre > lote.nombre:
            der = c-1
        else:
            izq = c+1
    if izq > der:
        pos = izq
    vec[pos:pos] = [lote]


def mayor_que(num):
    x = int(input("Ingrese un num mayor a {}: ".format(num)))
    while x < num:
        x = int(input("Ingrese un num mayor a {}: ".format(num)))
    return x


def entre(num1, num2):
    x = int(input("Ingrese un num entre {} y {}: ".format(num1, num2)))
    while x < num1 or x > num2:
        x = int(input("Ingrese un num entre {} y {}: ".format(num1, num2)))
    return x
