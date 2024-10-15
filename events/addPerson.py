from tkinter import ttk, messagebox
from utils.person import Person
def default(name: str, age: int, province: str, id: str, typeId: str, table: ttk.Treeview):
    person = Person(name, age, province, id, typeId)
    append = person.upsert()

    if(append):
        table.insert("", "end", values=(id, typeId, name, age, province))
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")
    else:
        children = table.get_children()
        for child in children:
            values = table.item(child, "values")
            if(values[0] == id):
                table.item(child, values=(id, typeId, name, age, province))
                break

        messagebox.showinfo("Éxito", "Datos actualizados correctamente.")