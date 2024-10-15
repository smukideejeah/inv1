from tkinter import ttk, Entry

def default(id: Entry, typeId: ttk.Combobox, name: Entry, age: Entry, province: ttk.Combobox, table: ttk.Treeview):
    selection = table.selection()
    item = selection[0]
    vals = table.item(item, "values")

    from utils.person import Person
    person = Person(vals[2], vals[3], vals[4], vals[0], vals[1])
    id.delete(0, "end")
    id.insert(0, person.id)
    typeId.set(person.typeId)
    name.delete(0, "end")
    name.insert(0, person.name)
    age.delete(0, "end")
    age.insert(0, person.age)
    province.set(person.province)
