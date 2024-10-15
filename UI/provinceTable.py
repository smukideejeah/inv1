from tkinter import ttk, messagebox
from typing import List
from utils.findByProvince import default as findByProvince
from utils.person import Person


def default(window: ttk, data: List[Person]):
    table = ttk.Treeview(window, columns=("Cédula", "Tipo", "Nombre", "Edad", "Provincia"), show="headings")

    table.heading("Cédula", text="Cédula")
    table.heading("Tipo", text="Tipo")
    table.heading("Nombre", text="Nombre")
    table.heading("Edad", text="Edad")
    table.heading("Provincia", text="Provincia")

    table.column("Cédula", width=100)
    table.column("Tipo", width=50)
    table.column("Nombre", width=100)
    table.column("Edad", width=30)
    table.column("Provincia", width=100)

    table.bind("<Double-1>", lambda e: messagebox.showinfo("Información", table.item(table.selection())['values']))

    for person in data:
        table.insert("", "end", values=(person.id, person.typeId, person.name, person.age, person.province))

    table.pack(pady=10, padx=10, fill="both", expand=True)
    return table 
