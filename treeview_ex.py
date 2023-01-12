import tkinter as tk
from tkinter import ttk
import json
class TreeviewFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.treeview = ttk.Treeview(
            self,
            yscrollcommand=self.vscrollbar.set
        )
        self.vscrollbar.config(command=self.treeview.yview)
        self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeview.pack()
root = tk.Tk()
root.geometry("400x300")
treeview_frame = TreeviewFrame()
treeview = ttk.Treeview()
treeview.config(columns=("name", "ligas"), show="headings")
treeview.heading("name", text="Influencers")
treeview.heading("ligas", text="Links")

with open("perfiles.txt", "r") as f:
    var = f.read()
objeto = json.loads(var)
for node in objeto:
    treeview.insert("", tk.END, values=(node, objeto[node]))

treeview.pack()
treeview_frame.pack()
root.mainloop()