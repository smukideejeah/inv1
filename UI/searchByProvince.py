import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from UI.provinceTable import default as initTable
from utils.findByProvince import default as findByProvince

def default(main: tk, province: str):
    init = findByProvince(province)

    if(len(init) == 0):
        messagebox.showwarning("Advertencia", f"No hay registros en la provincia de {province}")
        return

    window = tk.Toplevel(main)
    window.title(f"Registro de {province}")
    window.geometry("800x400")

    table = initTable(window, init)

    frameTable = tk.Frame(window)
    frameTable.pack(pady=10)
