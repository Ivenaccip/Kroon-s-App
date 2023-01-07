from tkinter import *
import json

class Seccion:

    def __init__(self):
        self.color_0 = "green"
        self.color_1 = "blue"
        self.color_2 = "red"
        self.stickyrow = 0
        self.sticky_brands = 'ew'
        self.profiles_tosearch = "buscar.txt"
        self.list_profiles = "perfiles.txt"

    def marco(self, ventana, texto, m_col, m_row):
        self.ventana = ventana
        ventana.columnconfigure(m_col,weight=1)
        ventana.rowconfigure(m_row,weight=0)

        if m_col == 0:
            color = self.color_0
        elif m_col == 1:
            color = self.color_1
        elif m_col == 2:
            color = self.color_2

        # Influencers con checkbox
        espacio_1 = Label(
            ventana,
            text=texto, 
            bg = color,
            fg = "white",
            font=("Arial","20"),
            bd = 2,
            relief="solid"
            )
        espacio_1.grid(
            row = m_row, 
            column = m_col,
            sticky=EW
            )

    def frames(self, ventana, texto, m_col, m_row):
        if m_col != 2:
            self.ventana = ventana
            ventana.columnconfigure(m_col,weight=1)
            ventana.rowconfigure(m_row,weight=0)

            marco_padre = Frame(
                ventana,
                relief="solid"
                )
            marco_padre.grid(
                row = m_row, 
                column = m_col,
                sticky=EW
                )
            if texto == "All Influencers":
                marco = Label(marco_padre, text=texto)
                marco.grid(sticky=EW)
            else:
                marco = Label(marco_padre, text=texto)
                marco.grid(sticky=EW)
        else:
            self.ventana = ventana
            ventana.columnconfigure(m_col,weight=1)
            ventana.rowconfigure(m_row,weight=0)

            marco_padre = Frame(
                ventana,
                relief="solid"
                )
            marco_padre.grid(
                row = m_row, 
                column = m_col,
                sticky=EW
                )

            marco1 = Checkbutton(marco_padre, text="# 1")
            marco2 = Checkbutton(marco_padre, text="# 2")
            marco3 = Checkbutton(marco_padre, text="# 3")
            marco1.grid(row=self.stickyrow, column=0, sticky=self.sticky_brands)
            marco2.grid(row=self.stickyrow, column=1, sticky=self.sticky_brands)
            marco3.grid(row=self.stickyrow, column=2, sticky=self.sticky_brands)

    def influencer(self, ventana):

        """
        def scroll(self, ventana, node, num):
            self.ventana = ventana
            checkbtn = Checkbutton(ventana, text=node)
            listbox.insert(num, checkbtn)
        
        v_s = Scrollbar(ventana)
        scroll_frame =Frame(ventana)
        v_s.grid(row=3, column=1, sticky="nsew")
        listbox.grid(row=3, column=0, sticky="ns", columnspan=2)
        v_s.config(command=listbox.yview)
        v_s.config(command = scroll_frame.yview)
        """
        int_inf = IntVar()
        str_inf = StringVar()
        def add_list():
            int_inf.get()
            print(str_inf.set(objeto[node]))
            with open(self.profiles_tosearch, "w") as b:
                b.write(str_inf.set(objeto[node]))

        
        def UI_inf(self, ventana, node):

            self.ventana = ventana
            inf = Checkbutton(
                ventana, 
                text=node,
                variable=int_inf,
                onvalue=1,
                offvalue=0,
                command=add_list
                )
            inf.grid(row = inf_row, column=0, sticky='w')
        
        
        num = 0

        inf_row = 3
        with open(self.list_profiles, "r") as f:
            variable = f.read()
        objeto = json.loads(variable)
        print(len(objeto))
        for node in objeto:
            
            inf_obj = StringVar()
            inf_obj.set(node)
            #scroll(self, ventana, node, num)
            UI_inf(self, ventana, node)
            inf_row += 1
            num += 1

    def infl(self, ventana):

        def UI_inf(self, ventana, node):
            self.ventana = ventana
            inf = Label(ventana, text=node)
            inf.grid(row = inf_row, column=0, sticky='w')

        inf_row = 3
        with open(self.list_profiles, "r") as f:
            variable = f.read()
        objeto = json.loads(variable)
        for node in objeto:
            UI_inf(self, ventana, node)
            inf_row += 1
    #Corregir
    def links_influencer(self, ventana):

        def UI_inf(self, ventana, n_obj):
            self.ventana = ventana
            inf = Label(ventana, text=n_obj)
            inf.grid(row = inf_row, column=1, sticky='w')

        inf_row = 3
        with open(self.list_profiles, "r") as f:
            variable = f.read()
        objeto = json.loads(variable)
        for node in objeto:
            n_obj = objeto[node]
            UI_inf(self, ventana, n_obj)
            inf_row += 1

    #Corregir
    def chatgpt3(self, ventana):

        def UI_chat(self, ventana, node, inf_row):
            self.ventana = ventana
            checkbutton = Checkbutton(ventana, text=node, variable=Bool_chat)
            checkbutton.grid(row = inf_row, column=0, sticky='w')


        Bool_chat = BooleanVar()
        inf_row = 3
        with open(self.list_profiles, "r") as f:
            variable = f.read()
        objeto = json.loads(variable)
        print(len(objeto))
        for node in objeto:
            n_obj = objeto[node]
            UI_chat(self, ventana, node ,inf_row)
            inf_row += 1

        def guardar():
            seleccionados = [text for text in n_obj if Bool_chat.get()]
            with open("seleccionados.txt", "w") as f:
                f.write("\n".join(seleccionados))

        boton_guardar = Button(ventana, text="Save", command=guardar)
        boton_guardar.grid(row = 0, column=0, sticky='w')

    # Funciona, pero es saple
    def prefab(self, ventana, row_p, nombre, link):

        self.ventana = ventana
        inf = Label(ventana, text = nombre)
        inf.grid(row = row_p, column= 0, sticky='w')
        bool_var = BooleanVar()
        btn = Checkbutton(ventana, text=link, variable=bool_var)
        btn.grid(row = row_p, column=1, sticky='w')

        def guardar():
            if bool_var.get():
                with open("seleccionados.txt", "w") as f:
                    f.write(link)

        boton_guardar = Button(ventana, text="Save", command=guardar)
        boton_guardar.grid(row  = 150,column = 0,sticky=S)
        boton_guardar.config(padx = 20)

    def correccion(self, ventana):
        self.ventana = ventana

        

