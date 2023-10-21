from modulo import *
import pickle
import random
import os.path
def script():
    op = -1
    registros = []
    fd = "lotes.dat"
    while op != 0:
        print("-- MENU --")
        print("1-")
        print("2-")
        print("3-")
        print("4-")
        print("5-")
        print("0-")
        op = entre(0, 5)
        if op == 1:
            cant = mayor_que(0)
            for i in range(cant):
                nom_ape = "Nombre " + str(random.randint(0, 50)) + " Apellido " + str(random.randint(0, 50))
                n_manz = random.randint(1, 35)
                n_lote = random.randint(1, 20)
                orient = random.randint(1, 4)
                superf = random.randint(10, 2000)
                monto = random.randint(1000, 50000)
                lote = Lote(nom_ape, n_manz, n_lote, orient, superf, monto)
                add_in_order(registros, lote)

        elif op == 2:
            for reg in registros:
                print(reg)
                
        elif op == 3:
            #4 orientaciones, 35 manzanas
            matriz = [[0, 0, 0, 0] for l in range(35)]
            for reg in registros:
                matriz[reg.n_manz - 1][reg.orient - 1] += reg.superf
            #PRINT
            for fila in matriz:
                # Iterar a través de las columnas en cada fila
                for elemento in fila:
                    print(elemento, end=' ')
                print()  # Salto de línea al final de cada fila
            #BUSQUEDA Y ACUMULACION
            manzana = entre(0, 35)
            acum = 0
            for x in range(4):
                acum += matriz[manzana - 1][x]
            print("Superficie acumulada en manzana {} : {}".format(manzana, acum))

        elif op == 4:
            extremo1 = entre(1, 20)
            extremo2 = entre(1, 20)
            while extremo1 > extremo2:
                extremo1 = entre(1, 20)
                extremo2 = entre(1, 20)
            cumplen = []
            for reg in registros:
                if reg.n_lote > extremo1:
                    if reg.n_lote < extremo2:
                        cumplen.append(reg)
            m = open(fd, "wb")
            for lote in cumplen:
                pickle.dump(lote, m)
            m.close()

        elif op == 5:
            m = open(fd, "rb")
            tamaño = os.path.getsize(fd)
            cont = 0
            sum = 0
            while m.tell() < tamaño:
                lote = pickle.load(m)
                print(lote)
                cont += 1
                sum += lote.monto
            m.close()
            m = open(fd, "ab")
            if cont != 0:
                promedio = sum / cont
            else:
                promedio = 0
            ultima_línea = "Promedio de monto: {}".format(promedio)
            pickle.dump(ultima_línea, m)
            m.close()

    else:
        print("Programa finalizado")
        return 0


if __name__ == "__main__":
    script()

