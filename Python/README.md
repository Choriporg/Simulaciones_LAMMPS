# Funcionalidad:
- Esta función lee y realiza un gráfico de los archivos generados por LAMMPS cuyo formato sea: 

<p style="text-align:center;">medida_1: dato_1 medida_2: dato_2</p>

---

# Dependencias:

- Para ejecutar este script es necesario tener instaladas las siguientes dependencias:

    - Pandas: <code> pip install pandas </code>

    - Numpy: <code> pip install numpy

    - MatPlotLib: <code> pip install matplotlib </code>

# Ejecución:

- Invoque la función (agregando la linea al final del script) entregando como parámetro el nombre del archivo que se busca leer. 

- __*Nota:*__ Es necesario que el archivo y el script se encuentren en el mismo directorio.

__*Ejemplo de uso:*__

<code> readNplot(totalE.data) </code>