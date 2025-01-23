'''
Programa principal
'''

import tkinter as tk
from gui import AppMenus

ventana = tk.Tk()
ventana.title("Gestión de menús")
ventana.geometry("800x600+200+200")
app = AppMenus(ventana)
ventana.mainloop()
