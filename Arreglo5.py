
class Arreglo5:
    __Arreglo = []
    __sumafilas = int(0)
    __sumacolumnas = int(0)
    __columnas = ''
    __filas = int(0)
    f = int(0)
    c = int(0)

    def crearDimensiones(self, f, c):
        for a in range(f):
            self.__Arreglo.append([0] * c)
        print(self.__Arreglo)

    def RellenarArreglo(self, f, c):
        try:
            for a1 in range(f):
                for b1 in range(c):
                    var1 = int(input('Ingrese un número para rellenar el arreglo: '))
                    self.__Arreglo[a1][b1] = var1
        except: ValueError

    def SumaFilas(self):
        for f in range(0, len(self.__Arreglo)):
            self.__sumafilas = 0
            for c in range(0, len(self.__Arreglo[f])):
                self.__sumafilas = self.__sumafilas + self.__Arreglo[f][c]
                self.__filas = self.__filas, self.__sumafilas
                print(self.__Arreglo[f][c], '\t', end="")
            print('Suma de la fila No.', f, '=', self.__sumafilas)
            print('\n')

    def SumaColumnas(self):
        for f2 in range(0, len(self.__Arreglo)):
            self.__sumacolumnas = 0
            for c2 in range(0, len(self.__Arreglo[f2])):
                self.__sumacolumnas = self.__sumacolumnas + self.__Arreglo[c2][f2]
                print(self.__Arreglo[c2][f2], '\t', end="")
            print('Suma de la columna No.', f2, '=', self.__sumacolumnas)
            print('\n')

codigo = Arreglo5()
codigo.crearDimensiones(10, 10)
codigo.RellenarArreglo(10, 10)
codigo.SumaFilas()
codigo.SumaColumnas()