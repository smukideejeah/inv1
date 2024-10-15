from tkinter import ttk, messagebox
from utils.person import Person
def default(table: ttk.Treeview):
    selection = table.selection()
    if not selection:
        messagebox.showwarning("Advertencia", "Selecciona una fila para eliminar.")
        return
    
    item = selection[0]
    vals = table.item(item, "values")

    person = Person(vals[2], vals[3], vals[4], vals[0], vals[1])
    person.delete()
    table.delete(item)
    messagebox.showinfo("Éxito", "Datos eliminados correctamente.")