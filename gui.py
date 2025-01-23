'''
Aplicación TKinter para gestión de menúss
'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import utilidades
import numpy as np
import random
from utilidades import fitness_function


class AppMenus(tk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)
        self.master = ventana
        self.pack()
        self.platos = utilidades.cargar_platos()

        self.crear_elementos()

    def crear_elementos(self):

        # Platos disponibles

        frame_platos = tk.Frame(self.master)
        
        frame_listado = tk.Frame(frame_platos)
        lbl_platos = tk.Label(frame_listado, text="Listado de platos", bg='black', fg='white')
        lbl_platos.pack(ipadx=5, ipady=5, fill=tk.X)
        self.lista_platos = tk.Listbox(frame_listado)
        self.cargar_platos()
        self.lista_platos.pack(expand=True, fill=tk.BOTH)
        self.lista_platos.bind("<<ListboxSelect>>", self.cargar_plato_form)

        frame_listado.pack(expand=True, fill=tk.X, side=tk.LEFT, anchor=tk.N)

        frame_formulario = tk.Frame(frame_platos)
        frame_formulario.columnconfigure(1, weight=1)
        lbl_nombre = tk.Label(frame_formulario, text="Nombre plato:", anchor="w")
        lbl_nombre.grid(row=0, column=0, sticky="EW")
        self.nombre = tk.StringVar()
        txt_nombre = tk.Entry(frame_formulario, textvariable=self.nombre)
        txt_nombre.grid(row=0, column=1, sticky="EW")
        lbl_tipo = tk.Label(frame_formulario, text="Tipo plato:", anchor="w")
        lbl_tipo.grid(row=1, column=0, sticky="EW")
        self.tipo = tk.StringVar()
        lista_tipos = ttk.Combobox(frame_formulario, textvariable=self.tipo)
        lista_tipos['values'] = ['1', '2', 'P']
        lista_tipos.grid(row=1, column=1, sticky="EW")
        lbl_coste = tk.Label(frame_formulario, text="Coste:", anchor="w")
        lbl_coste.grid(row=2, column=0, sticky="EW")
        self.coste = tk.StringVar()
        txt_coste = tk.Entry(frame_formulario, textvariable=self.coste)
        txt_coste.grid(row=2, column=1, sticky="EW")
        lbl_tiempo = tk.Label(frame_formulario, text="Tiempo (min):", anchor="w")
        lbl_tiempo.grid(row=3, column=0, sticky="EW")
        self.tiempo = tk.StringVar()
        txt_tiempo = tk.Entry(frame_formulario, textvariable=self.tiempo)
        txt_tiempo.grid(row=3, column=1, sticky="EW")
        lbl_calorias = tk.Label(frame_formulario, text="Calorías:", anchor="w")
        lbl_calorias.grid(row=4, column=0, sticky="EW")
        self.calorias = tk.StringVar()
        txt_calorias = tk.Entry(frame_formulario, textvariable=self.calorias)
        txt_calorias.grid(row=4, column=1, sticky="EW")
        btn_nuevo = tk.Button(frame_formulario, text="Añadir nuevo", bg='green', fg='white', command=self.nuevo_plato)
        btn_nuevo.grid(row=5, column=0, columnspan=2, sticky="EW")
        btn_modificar = tk.Button(frame_formulario, text="Modificar", bg='blue', fg='white', command=self.modificar_plato)
        btn_modificar.grid(row=6, column=0, columnspan=2, sticky="EW")
        frame_formulario.pack(expand=True, fill=tk.X, side=tk.LEFT, anchor=tk.N)

        frame_platos.pack(fill=tk.X)

        # Restricciones

        frame_restricciones = tk.Frame(self.master)

        lbl_restricciones = tk.Label(frame_restricciones, text="Restricciones del menú", bg='black', fg='white')
        lbl_restricciones.pack(ipadx=5, ipady=5, fill=tk.X)
        lbl_tiempo_max = tk.Label(frame_restricciones, text="Tiempo máx:")
        lbl_tiempo_max.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.txt_tiempo_max = tk.Entry(frame_restricciones)
        self.txt_tiempo_max.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        lbl_precio_max = tk.Label(frame_restricciones, text="Precio máx:")
        lbl_precio_max.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.txt_precio_max = tk.Entry(frame_restricciones)
        self.txt_precio_max.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        lbl_calorias_max = tk.Label(frame_restricciones, text="Calorías máx:")
        lbl_calorias_max.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.txt_calorias_max = tk.Entry(frame_restricciones)
        self.txt_calorias_max.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        frame_restricciones.pack(fill=tk.X)

        frame_algoritmo = tk.Frame(self.master)

        lbl_algoritmo = tk.Label(frame_algoritmo, text="Características algoritmo genético", bg='black', fg='white')
        lbl_algoritmo.pack(ipadx=5, ipady=5, fill=tk.X)
        lbl_iterac = tk.Label(frame_algoritmo, text="Iteraciones:")
        lbl_iterac.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.txt_iterac = tk.Entry(frame_algoritmo)
        self.txt_iterac.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        lbl_poblac = tk.Label(frame_algoritmo, text="Tam. población:")
        lbl_poblac.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.txt_poblac = tk.Entry(frame_algoritmo)
        self.txt_poblac.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        lbl_cruces = tk.Label(frame_algoritmo, text="Num. cruces:")
        lbl_cruces.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.txt_cruces = tk.Entry(frame_algoritmo)
        self.txt_cruces.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        lbl_mutac = tk.Label(frame_algoritmo, text="Prob. mutacion:")
        lbl_mutac.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.txt_mutac = tk.Entry(frame_algoritmo)
        self.txt_mutac.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        frame_algoritmo.pack(fill=tk.X)

        # Botones para calcular y limpiar

        frame_botones = tk.Frame(self.master)
        
        btn_calcular = tk.Button(frame_botones, text="Calcular", bg='blue', fg='white', command=self.calcular)
        btn_calcular.pack(expand=True, ipadx=10, side=tk.LEFT)
        btn_limpiar = tk.Button(frame_botones, text="Limpiar", bg='red', fg='white', command=self.limpiar)
        btn_limpiar.pack(expand=True, ipadx=10, side=tk.LEFT)

        frame_botones.pack(fill=tk.X)

        # Etiquetas para resultados

        lbl_primeros_titulo = tk.Label(self.master, text="Primeros", bg='yellow')
        lbl_primeros_titulo.pack(fill=tk.X)
        self.primeros = [tk.StringVar(), tk.StringVar(), tk.StringVar()]
        lbl_primeros1 = tk.Label(self.master, textvariable=self.primeros[0])
        lbl_primeros1.pack(fill=tk.X)
        lbl_primeros2 = tk.Label(self.master, textvariable=self.primeros[1])
        lbl_primeros2.pack(fill=tk.X)
        lbl_primeros3 = tk.Label(self.master,textvariable=self.primeros[2])
        lbl_primeros3.pack(fill=tk.X)

        lbl_segundos_titulo = tk.Label(self.master, text="Segundos", bg='yellow')
        lbl_segundos_titulo.pack(fill=tk.X)
        self.segundos = [tk.StringVar(), tk.StringVar(), tk.StringVar()]
        lbl_segundos1 = tk.Label(self.master, textvariable=self.segundos[0])
        lbl_segundos1.pack(fill=tk.X)
        lbl_segundos2 = tk.Label(self.master, textvariable=self.segundos[1])
        lbl_segundos2.pack(fill=tk.X)
        lbl_segundos3 = tk.Label(self.master, textvariable=self.segundos[2])
        lbl_segundos3.pack(fill=tk.X)

        lbl_postres_titulo = tk.Label(self.master, text="Postres", bg='yellow')
        lbl_postres_titulo.pack(fill=tk.X)
        self.postres = [tk.StringVar(), tk.StringVar(), tk.StringVar()]
        lbl_postres1 = tk.Label(self.master, textvariable=self.postres[0])
        lbl_postres1.pack(fill=tk.X)
        lbl_postres2 = tk.Label(self.master, textvariable=self.postres[1])
        lbl_postres2.pack(fill=tk.X)
        lbl_postres3 = tk.Label(self.master, textvariable=self.postres[2])
        lbl_postres3.pack(fill=tk.X)

        self.resultado = tk.StringVar()
        lbl_resultado = tk.Label(self.master, textvariable=self.resultado, bg='green', fg='white')
        lbl_resultado.pack(fill=tk.X)

    # Cargar platos en lista
    def cargar_platos(self):
        self.lista_platos.delete(0, tk.END)
        self.platos = self.platos.sort_values(by="Nombre")
        self.platos.reset_index(drop=True, inplace=True)
        for i in range(len(self.platos)):
            self.lista_platos.insert(i+1, self.platos.loc[i, 'Nombre'])

    # Carga el plato seleccionado en el formulario
    def cargar_plato_form(self, event):
        seleccion = self.lista_platos.curselection()
        if seleccion:
            self.nombre.set(self.platos.loc[seleccion[0], 'Nombre'])
            self.tipo.set(self.platos.loc[seleccion[0], 'Tipo'])
            self.coste.set(self.platos.loc[seleccion[0], 'Coste'])
            self.tiempo.set(self.platos.loc[seleccion[0], 'Tiempo'])
            self.calorias.set(self.platos.loc[seleccion[0], 'Calorias'])
    
    # Evento para añadir un nuevo plato
    def nuevo_plato(self):
        if self.nombre.get() == '' or self.tipo.get() == '' or \
           self.coste.get() == '' or self.tiempo.get() == '' or \
           self.calorias.get() == '':
            messagebox.showwarning("Cuidado", "Hay campos vacíos en el formulario")
        else:
            self.platos.loc[len(self.platos)] = [self.nombre.get(), \
                self.tipo.get(), float(self.coste.get()), int(self.tiempo.get()), \
                int(self.calorias.get())]
            utilidades.guardar_platos(self.platos)
            self.cargar_platos()

    # Evento para modificar un plato existente
    def modificar_plato(self):
        seleccion = self.lista_platos.curselection()
        if seleccion:
            if self.nombre.get() == '' or self.tipo.get() == '' or \
                self.coste.get() == '' or self.tiempo.get() == '' or \
                self.calorias.get() == '':
                messagebox.showwarning("Cuidado", "Hay campos vacíos en el formulario")
            else:
                self.platos.loc[seleccion[0]] = [self.nombre.get(), \
                    self.tipo.get(), float(self.coste.get()), int(self.tiempo.get()), \
                    int(self.calorias.get())]
                utilidades.guardar_platos(self.platos)
                self.cargar_platos()
        else:
            messagebox.showwarning("Cuidado", "No hay ningún plato seleccionado")

    # Limpia las etiquetas de resultados del final
    def limpiar(self):
        for texto in self.primeros:
            texto.set("")
        for texto in self.segundos:
            texto.set("")
        for texto in self.postres:
            texto.set("")
        self.resultado.set("")
    

    def calcular(self):
 
        # 1. Control de error para restricciones
        try:
            #1.1 Ingresar valores válidos
            tiempo_max = int(self.txt_tiempo_max.get())
            precio_max = float(self.txt_precio_max.get())
            calorias_max = int(self.txt_calorias_max.get())
            iteraciones = int(self.txt_iterac.get())
            tam_poblacion = int(self.txt_poblac.get())
            num_cruces = int(self.txt_cruces.get())
            prob_mutaciones = float(self.txt_mutac.get())

            #1.1 Configurar restricciones para pasarlas a fitness
            utilidades.set_restricciones(tiempo_max, precio_max, calorias_max)

            #1.2 prob_mutaciones entre 0 y 1
            if prob_mutaciones < 0 or prob_mutaciones > 1:
                messagebox.showwarning("Error", f"Prob. mutación:{prob_mutaciones} debe ser entre 0 y 1 inclusive")
                return
            
            #1.3 num_cruces no sea mayor que tam_poblacion
            if num_cruces > tam_poblacion:
                messagebox.showwarning("Error", f"Núm.cruces {num_cruces} no puede ser mayor que Tam.poblacion {tam_poblacion}")
                return        
        
            #1.4 Validar cantidad de platos antes de iniciar
            platos_disponibles = utilidades.cargar_platos()

            platos_1 = utilidades.filtrar_tipo(platos_disponibles, '1')
            platos_2 = utilidades.filtrar_tipo(platos_disponibles, '2')
            platos_3 = utilidades.filtrar_tipo(platos_disponibles, 'P')

            if len(platos_1) < 3 or len(platos_2) < 3 or len(platos_3) < 3:
                messagebox.showwarning("Error","No hay suficientes platos de cada tipo.")
                return

        except ValueError:
            messagebox.showwarning("Error", "Error en los datos ingresados")
            return

    
             
        #3. Generar Individuo
        class Individuo:
            def __init__(self, alelos, funcion_fitness):
                self.alelos = alelos #¿que valor se supone que son alelos? 9?
                self.fitness = funcion_fitness(self)

        #4. Generar Algoritmo
        class AlgoritmoGenetico:
            def __init__(self, tamano_poblacion, tamano_alelos, valores_discretos,
                funcion_fitness, num_cruces, prob_mutacion, num_mutaciones = 3):
                self.tamano_poblacion = tamano_poblacion
                self.tamano_alelos = tamano_alelos # 9 platos
                self.valores_discretos = valores_discretos 
                self.funcion_fitness = funcion_fitness 
                self.num_cruces = num_cruces 
                self.prob_mutacion = prob_mutacion 
                self.num_mutaciones = num_mutaciones #Número de mutaciones en un individuo (cantidad de alelos que mutan). Podemos indicar que por defecto será 1.
                self.poblacion = []
                self.generar_poblacion()
                
                
            #4.1. Generar Población: Generar población  de menús
            def generar_poblacion(self):
                #A. Verificamos si existen alelos suficientes
                if self.tamano_poblacion <= 0:
                    messagebox.showwarning("Error", "El tamaño de la población debe ser mayor a 0")
                    return

                #B. Cargar los platos desde el archivo CSV            
                platos = utilidades.cargar_platos()  
    
                #C. Dividir los platos según su tipo
                platos_1 = utilidades.filtrar_tipo(platos, '1')  # Primeros platos
                platos_2 = utilidades.filtrar_tipo(platos, '2')  # Segundos platos
                platos_3 = utilidades.filtrar_tipo(platos, 'P')  # Postres

                #D. Verificar que haya suficientes platos en cada categoría en el csv
                if len(platos_1) < 3 or len(platos_2) < 3 or len(platos_3) < 3:
                    messagebox.showwarning("Error", "No hay suficientes platos para generar un menú completo")
                    return

                #E. Generar la población de menús
                while len(self.poblacion) < self.tamano_poblacion:
                    #E.1 Generar valores de menú: Seleccionar 3 platos de cada tipo aleatoriamente
                    primeros = random.sample(platos_1, 3) #sample rectifica que sean diferentes
                    segundos = random.sample(platos_2, 3)
                    postres = random.sample(platos_3, 3)

                    #E.2 Crear un individuo (menú completo)
                    menu = primeros + segundos + postres

                    #E.3 Añade Individuo
                    self.poblacion.append(Individuo(menu, self.funcion_fitness))

           
            #4.2 Ordenar Población: Ordenamos por fitness en orden decreciente
            def ordenar_poblacion(self):
                self.poblacion.sort(key=lambda x: x.fitness, reverse=True)        

            #4.3 Selección de Individuos (Menús)
            def seleccionar_individuos(self):           
                #A. Indices de los individuos de la población
                indices = range(0, self.tamano_poblacion)
                #B. Peso para cada individuo según su fitness
                pesos = [x.fitness+0.0000001 for x in self.poblacion]
                #C. Elegimos el primer individuo
                individuo1 = random.choices(indices, weights=pesos, k = 1)[0]
                #D. Elegimos al segundo individuo de entre los restantes
                indices_restantes = [i for i in indices if i != individuo1]
                individuo2 = random.choices(indices_restantes, weights=[pesos[i] for i in indices_restantes], k=1)[0]
                return individuo1, individuo2 

            #4.4 .Cruzar: 2 menus, para generar otro.
            def cruzar(self, individuo1, individuo2):

                #A.Dividir los platos de cada menú (Individuo):
                primeros1 = self.poblacion[individuo1].alelos[:3] #En la población, seleccionamos el menu y sus platos
                segundos1 = self.poblacion[individuo1].alelos[3:6]
                postres1 = self.poblacion[individuo1].alelos[6:]
                
                #B. Individuo 2
                primeros2 = self.poblacion[individuo2].alelos[:3]
                segundos2 = self.poblacion[individuo2].alelos[3:6]
                postres2 = self.poblacion[individuo2].alelos[6:]
                
                #c. Mezclar platos de cada tipo sin repetirlos
                nuevos_primeros = random.sample(primeros1 + primeros2, 3) #Sample, Sin Repeticion
                nuevos_segundos = random.sample(segundos1 + segundos2, 3)
                nuevos_postres = random.sample(postres1 + postres2, 3)

                #D. Crear nuevos alelos: Nuevo Individuo(menu) cruzado
                nuevos_alelos = nuevos_primeros + nuevos_segundos + nuevos_postres
                return nuevos_alelos


            #4.5. Mutar: Alteramos al azar alelos(platos) del menú creado en "cruzar".
            def mutar_individuo(self, alelos):
 
                for _ in range(self.num_mutaciones):
                    # A. Seleccionamos un índice aleatorio (0 a 8)
                    index_plato = np.random.randint(len(alelos))

                    # B. Identificamos el tipo de plato actual (1, 2, o P)
                    tipo_plato = alelos[index_plato]["Tipo"]

                    # C. Seleccionamos nuestros candidatos: Es decir TODOS nuestros platos con el TIPO indicado
                    nuevos_candidatos = utilidades.filtrar_tipo(platos_disponibles, tipo_plato)
  
                    # D. Haremos la mutación , verificando duplicados
                    while True:
                        nuevo_plato = random.choice(nuevos_candidatos) #elegir un plato random de los candidatos

                        # D.1. Verificamos que el nuevo plato no esté ya en la misma categoría
                        if tipo_plato == '1':  # Primeros platos
                            if nuevo_plato not in alelos[:3]:  # Evitar duplicados en primeros
                                alelos[index_plato] = nuevo_plato
                                break
                        elif tipo_plato == '2':  # Segundos platos
                            if nuevo_plato not in alelos[3:6]:  # Evitar duplicados en segundos
                                alelos[index_plato] = nuevo_plato
                                break
                        elif tipo_plato == 'P':  # Postres
                            if nuevo_plato not in alelos[6:]:  # Evitar duplicados en postres
                                alelos[index_plato] = nuevo_plato
                                break

                            
            #4.6. Reemplazo: Se tomará un individuo, y una posición en la población, y directamente reemplazará el elemento de esa posición por el nuevo individuo.
            def reemplazar(self, hijo, indice):
                self.poblacion[indice] = hijo

            #4.7. Proceso
            def iniciar_proceso(self, iteraciones, verbose=False):
                for i in range(iteraciones):
                    self.ordenar_poblacion()

                    # Mostramos información de la iteración si procede
                    if verbose:
                        print(f"Iteración {i + 1}, mejor fitness: {self.poblacion[0].fitness}")
                    
                    for j in range(self.num_cruces):
                        #Se tomará 2 individuos(menú)                       
                        individuo1, individuo2 = self.seleccionar_individuos() #son 2 índices
                        
                        #Cruzar
                        nuevos_alelos = self.cruzar(individuo1, individuo2)

                        # Mutar. Mutamos si entra en la probabilidad
                        resultado_probabilidad = np.random.rand()
                        if resultado_probabilidad < self.prob_mutacion:
                            self.mutar_individuo(nuevos_alelos)

                       # Se conforma el nuevo individuo
                        hijo = Individuo(nuevos_alelos, self.funcion_fitness)

                        # Reemplazar población
                        self.reemplazar(hijo, len(self.poblacion) - 1 - j)
                self.ordenar_poblacion() #Ordenar poblacion por mejor fitness
                return self.poblacion[0]
            
        #5. Iniciar el  Algoritmo
        algoritmo = AlgoritmoGenetico(
            tamano_poblacion=tam_poblacion,
            tamano_alelos=9,
            valores_discretos=False,
            funcion_fitness= fitness_function,
            num_cruces=num_cruces,
            prob_mutacion=prob_mutaciones,
        )

        #6. Ejecutar el algoritmo genético
        mejor_individuo = algoritmo.iniciar_proceso(iteraciones=iteraciones, verbose=True)

        #7. Mostrar resultados
        print("\nMejor solución encontrada:")
        print("Platos:", mejor_individuo.alelos)
        print("Fitness:", mejor_individuo.fitness)

        #8. Mostrar resultados 
        if mejor_individuo:
            self.pintar_resultados(mejor_individuo) 
        else:
            messagebox.showwarning("Error", "No se encontró un menú válido.")



    def pintar_resultados(self, mejor_individuo): #Función para pintar por pantalla los resultados
        if mejor_individuo:
            # Dividir los platos según las posiciones en la lista
            primeros = mejor_individuo.alelos[:3]
            segundos = mejor_individuo.alelos[3:6]
            postres = mejor_individuo.alelos[6:9]

            # Pintar primeros platos
            for i, plato in enumerate(primeros):
                self.primeros[i].set(f"{plato['Nombre']}: {plato['Coste']} eur, {plato['Tiempo']} min, {plato['Calorias']} cal")

            # Pintar segundos platos
            for i, plato in enumerate(segundos):
                self.segundos[i].set(f"{plato['Nombre']}: {plato['Coste']} eur, {plato['Tiempo']} min, {plato['Calorias']} cal")

            # Pintar postres
            for i, plato in enumerate(postres):
                self.postres[i].set(f"{plato['Nombre']}: {plato['Coste']} eur, {plato['Tiempo']} min, {plato['Calorias']} cal")

            # Calcular máximos valores por categoría
            max_calorias = (
                max(primero["Calorias"] for primero in primeros)
                + max(segundo["Calorias"] for segundo in segundos)
                + max(postre["Calorias"] for postre in postres)
            )

            max_tiempo = (
                max(primero["Tiempo"] for primero in primeros)
                + max(segundo["Tiempo"] for segundo in segundos)
                + max(postre["Tiempo"] for postre in postres)
            )

            max_costo = (
                max(primero["Coste"] for primero in primeros)
                + max(segundo["Coste"] for segundo in segundos)
                + max(postre["Coste"] for postre in postres)
            )

            # Mostrar máximos en la etiqueta verde
            self.resultado.set(f"Máx coste = {max_costo:.2f} eur, Máx tiempo = {max_tiempo} min, Máx calorías = {max_calorias} cal")
        else:
            messagebox.showwarning("Error", "No se encontró un menú válido.")