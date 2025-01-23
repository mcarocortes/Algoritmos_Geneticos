Algoritmos Genéticos
Encontrar el Menú Óptimo con Algoritmos Genéticos
Explicación Científica
En esta práctica, desarrollaremos un algoritmo genético para crear menús de restaurante que cumplan una serie de restricciones. El proyecto tiene la siguiente estructura de archivos:

utilidades.py: Contiene funciones de utilidad.

gui.py: Aplicación gráfica en TKinter.

main.py: Programa principal que carga la ventana de la App.

Los platos disponibles están en el archivo platos.csv. Cada plato tiene las siguientes características:

Nombre del plato (por ejemplo, "Ensalada César")

Tipo de plato (1 = primero, 2 = segundo, P = postre)

Coste de preparación en euros

Tiempo de preparación en minutos

Calorías

Las funciones cargar_platos y guardar_platos en utilidades.py gestionan este archivo.

Cada menú debe cumplir las siguientes restricciones:

Tres platos de cada tipo (primeros, segundos y postres).

La combinación de un plato de cada tipo no debe exceder el número de calorías especificado en el cuadro "Máx calorías" de la aplicación.

El tiempo de preparación de un plato de cada tipo no debe exceder el tiempo total especificado en el cuadro "Máx tiempo".

El precio de un plato de cada tipo no debe exceder el precio total especificado en el cuadro "Máx precio".

Los menús se ordenarán de mayor a menor beneficio (diferencia entre el precio máximo y el coste total de preparación de la combinación más cara de platos).

Desarrollaremos un algoritmo genético para determinar los menús óptimos. El algoritmo se activará al pulsar "Calcular" en la App. Los parámetros del algoritmo (iteraciones, individuos de población, cruces y probabilidad de mutación) son configurables. Al finalizar, se mostrará el menú seleccionado con la información de los platos y un resumen del coste, tiempo de preparación y calorías.

Para lograr esto, completa el evento calcular en gui.py y define una función de fitness en utilidades.py.
