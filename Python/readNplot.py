import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
La función recibe como entrada un string que será el nombre del archivo (o su PATH),
extraerá la información del archivo y la graficará. Para esta función, el archivo debe tener
una estructura de la siguiente forma (Las etiquetas deben estár separadas por '_', '-' o utilizar
nomenclatura Camel Case, no se pueden usar espacios.):

medicion_1: dato1  medicion_2: dato2
medicion_1: dato3  medicion_2: dato4
.
.
.
"""
def readNplot_data(fileName):
    file = open(fileName, "r")

    datos = []

    for line in file:
        #Omitir comentarios de LAMMPS
        if line[0] != "#":
            data = line.split()
            dict = {}
            dict[data[0]] = float(data[1])
            dict[data[2]] = float(data[3])
            datos.append(dict)
            df = pd.DataFrame(datos)
    df.plot(x=data[0], y=data[2], xlabel=data[0][:-1], ylabel=data[2][:-1])
    file.close()
    return df