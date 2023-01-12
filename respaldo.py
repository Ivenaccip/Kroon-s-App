import tkinter as tk
from tkinter import ttk
import json
import os
class TreeviewFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.treeview = ttk.Treeview(
            self,
            selectmode="extended",
            yscrollcommand=self.vscrollbar.set
        )
        self.vscrollbar.config(command=self.treeview.yview)
        self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeview.pack(fill="x")

def selectItem():
    links_list = []
    names_list = []
    selected_item = treeview_frame.treeview.selection()
    for item in selected_item:
        current_item = treeview_frame.treeview.item(item)
        company = current_item.get("values")[0]
        link = current_item.get("values")[1]
        links_list.append(link)
        names_list.append(company)

    json_str_links = json.dumps(links_list)
    with open("links_seleccionados.txt", "w") as f:
        f.write(json_str_links)
    json_str_names = json.dumps(names_list)
    with open("names_seleccionados.txt", "w") as g:
        g.write(json_str_names)

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d"  %(width, height))

treeview_frame = TreeviewFrame()
treeview_frame.pack(fill="x")
treeview_frame.treeview.config(columns=("name", "ligas"), show="headings")
treeview_frame.treeview.heading("name", text="Influencers")
treeview_frame.treeview.heading("ligas", text="Links")
#treeview_frame.treeview.bind('<ButtonRelease-1>', selectItem())

with open("perfiles.txt", "r") as f:
    var = f.read()
objeto = json.loads(var)
for node in objeto:
    treeview_frame.treeview.insert("", tk.END, values=(node, objeto[node]))

#Botón seleccionados
btn_get = tk.Button(root, text="Get data", command=selectItem)
btn_get.pack()
root.mainloop()