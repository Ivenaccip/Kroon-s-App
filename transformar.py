import json
from tkinter import *

def escribir(n_obj, dic):
    pass

with open("perfiles.txt", "r") as f:
    variable = f.read()
objeto = json.loads(variable)
dic = {}
var = BooleanVar()
dic[objeto]
for node in objeto:
    n_obj = objeto[node]
    escribir(n_obj, dic)