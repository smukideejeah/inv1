from tkinter import ttk, Menu
from conf.env import PROVINCES
from UI.searchByProvince import default as searchByProvince

def default(window: ttk):
    menu = Menu(window)
    window.config(menu=menu)

    provincesMenu = Menu(menu, tearoff=0)

    for province in PROVINCES:
        provincesMenu.add_command(label=province, command=lambda p = province: searchByProvince(window, p))

    menu.add_cascade(label="Buscar por Provincia", menu=provincesMenu)