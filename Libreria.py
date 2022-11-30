from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import os
import yaml
from yaml.cyaml import CLoader


linkexpo="https://www.youtube.com"
MasterKey="S!nA*OS&NBsm!LaSfWuO"
Vendedores=[]
DemoinUse=False
Promedios=dict(PapaAmarilla=2.50, PapaBlanca=2.50, PapaYungay=1.50, CebollaRoja=2.50, CebollaBlanca=3.00, Tomate=5.00,
                BolsitaVerduras=1.00, Maracuya=3.00, BotellaJugo=5.00, PlatoComida=10.00)
Answ_Posicion=-1
Answ_Nombre=""
Answ_Apellido_Paterno=""
Answ_Apellido_Materno=""
Answ_Local_Number=""
Contador_Contraseña=0

#Modo Demo Variables
ProdEstandar=dict(PapaAmarilla=2.50, PapaBlanca=2.50, PapaYungay=1.50, CebollaRoja=2.50, CebollaBlanca=3.00, Tomate=5.00,
                BolsitaVerduras=1.00, Maracuya=3.00, BotellaJugo=5.00, PlatoComida=10.00)
Estandar=dict(Nombre="Estandar", ApPaterno="Estandarizado", ApMaterno="Promedio", Local=999, Contraseña="Admin", Productos=ProdEstandar)
ProdPepe=dict(PapaAmarilla=2.50, PapaBlanca=2.00, PapaYungay=1.75, CebollaRoja=2.75, CebollaBlanca=3.25, Tomate=4.50,
                BolsitaVerduras=0.80, Maracuya=2.25, BotellaJugo=5.10, PlatoComida=0.00)
Pepe=dict(Nombre="Pepe", ApPaterno="Gomez", ApMaterno="Rosas", Local=1000, Contraseña="PepeGomez", Productos=ProdPepe)
ProdJuana=dict(PapaAmarilla=2.15, PapaBlanca=2.90, PapaYungay=1.20, CebollaRoja=2.75, CebollaBlanca=2.64, Tomate=5.30,
                BolsitaVerduras=1.10, Maracuya=3.20, BotellaJugo=0.00, PlatoComida=0.00)
Juana=dict(Nombre="Juana", ApPaterno="Ramos", ApMaterno="Quispe", Local=1001, Contraseña="JuanaRamos", Productos=ProdJuana)
ProdRobert=dict(PapaAmarilla=0.00, PapaBlanca=0.00, PapaYungay=0.00, CebollaRoja=0.00, CebollaBlanca=0.00, Tomate=0.00,
                BolsitaVerduras=0.00, Maracuya=2.70, BotellaJugo=5.25, PlatoComida=11.30)
Robert=dict(Nombre="Robert", ApPaterno="Mamani", ApMaterno="Perales", Local=1002, Contraseña="RobertMamani", Productos=ProdRobert)
ProdMaria=dict(PapaAmarilla=0.00, PapaBlanca=0.00, PapaYungay=0.00, CebollaRoja=0.00, CebollaBlanca=0.00, Tomate=0.00,
                BolsitaVerduras=0.90, Maracuya=0.00, BotellaJugo=4.60, PlatoComida=12.20)
Maria=dict(Nombre="Maria", ApPaterno="Ramos", ApMaterno="Quispe", Local=1003, Contraseña="MariaRamos", Productos=ProdMaria)

VendedoresDEMO=[Estandar,Pepe,Juana,Robert,Maria]

def a(): #ALTAMENTE TEMPORAL
    print("funciona")

#Menú Principal
def W_Main_Menu():
    global ventana_Main_Menu
    ventana_Main_Menu=Tk()
    ventana_Main_Menu.geometry("780x580")
    ventana_Main_Menu.title("Mercado Santa Rosita")
    ventana_Main_Menu.resizable(False,False)

    Label(ventana_Main_Menu, text = "Menú Principal", font = "MesloLG 35").place(x=225, y= 10)
    Label(ventana_Main_Menu, text = "Mercado " '"Santa Rosita"', font = "MesloLG 28 ").place(x=180, y= 65)

    ImageHelp=PhotoImage(file="Button_Help.png")
    ImageONOFF=PhotoImage(file="Button_On_Off.png")

    Button(ventana_Main_Menu, image=ImageHelp,command=MB_Help).place(x=680, y=100)
    Label(ventana_Main_Menu, text = "Ayuda", font = "MesloLG 7").place(x=678, y= 131)
    Button(ventana_Main_Menu, image=ImageONOFF,command=A_On_Off).place(x=70, y=510)
    Button(ventana_Main_Menu, text = "Ver Promedios del Mercado", command=W_Average, width = 25, height = 2, font = "Consolas 20", fg="black", bg="light Gray").place(x=175, y= 160)
    #Button(ventana_Main_Menu, text = "Registrar nuevo Vendedor", command=W_New_Seller, width = 25, height = 2, font = "Consolas 20", fg="black", bg="light Gray").place(x=175, y= 255)
    Button(ventana_Main_Menu, text = "Registrar nuevo Vendedor", command=W_New_Seller, width = 25, height = 2, font = "Consolas 20", fg="black", bg="light Gray").place(x=175, y= 255)
    Button(ventana_Main_Menu, text = "Buscar un Vendedor", command=W_Search_Seller, width = 25, height = 2, font = "Consolas 20", fg="black", bg="light Gray").place(x=175, y= 350)
    Button(ventana_Main_Menu, text = "Activar modo Demo", command=W_Demo_Mode, width = 25, height = 2, font = "Consolas 20", fg="black", bg="light Gray").place(x=175, y= 445)
    Button(ventana_Main_Menu, text = "Pagina Web del Mercado", command=A_Web, width = 23, height = 0, font = "Consolas 8", fg="black", bg="white").place(x=591, y= 520)
    ventana_Main_Menu.mainloop()

#Promedio del Mercado
def A_Promediar():
    global Promedios
    PAmarilla=0
    lenghtPAmarilla=0
    PBlanca=0
    lenghtPBlanca=0
    PYungay=0
    lenghtPYungay=0
    CRoja=0
    lenghtCRoja=0
    CBlanca=0
    lenghtCBlanca=0
    Tmte=0
    lenghtTmte=0
    BolsVerduras=0
    lenghtBolsVerduras=0
    Mrcuya=0
    lenghtMrcuya=0
    BtllJugo=0
    lenghtBtllJugo=0
    PltComida=0
    lenghtPltComida=0
    global Vendedores
    lenght=len(Vendedores)
    if lenght>0:
        for i in range(0,lenght):
            if Vendedores[i]["Productos"]["PapaAmarilla"]>0:
                PAmarilla=PAmarilla+Vendedores[i]["Productos"]["PapaAmarilla"]
                lenghtPAmarilla=lenghtPAmarilla+1
            if Vendedores[i]["Productos"]["PapaBlanca"]>0:
                PBlanca=PBlanca+Vendedores[i]["Productos"]["PapaBlanca"]
                lenghtPBlanca=lenghtPBlanca+1
            if Vendedores[i]["Productos"]["PapaYungay"]>0:
                PYungay=PYungay+Vendedores[i]["Productos"]["PapaYungay"]
                lenghtPYungay=lenghtPYungay+1
            if Vendedores[i]["Productos"]["CebollaRoja"]>0:
                CRoja=CRoja+Vendedores[i]["Productos"]["CebollaRoja"]
                lenghtCRoja=lenghtCRoja+1
            if Vendedores[i]["Productos"]["CebollaBlanca"]>0:
                CBlanca=CBlanca+Vendedores[i]["Productos"]["CebollaBlanca"]
                lenghtCBlanca=lenghtCBlanca+1
            if Vendedores[i]["Productos"]["Tomate"]>0:
                Tmte=Tmte+Vendedores[i]["Productos"]["Tomate"]
                lenghtTmte=lenghtTmte+1
            if Vendedores[i]["Productos"]["BolsitaVerduras"]>0:
                BolsVerduras=BolsVerduras+Vendedores[i]["Productos"]["BolsitaVerduras"]
                lenghtBolsVerduras=lenghtBolsVerduras+1
            if Vendedores[i]["Productos"]["Maracuya"]>0:
                Mrcuya=Mrcuya+Vendedores[i]["Productos"]["Maracuya"]
                lenghtMrcuya=lenghtMrcuya+1
            if Vendedores[i]["Productos"]["BotellaJugo"]>0:
                BtllJugo=BtllJugo+Vendedores[i]["Productos"]["BotellaJugo"]
                lenghtBtllJugo=lenghtBtllJugo+1
            if Vendedores[i]["Productos"]["PlatoComida"]>0:
                PltComida=PltComida+Vendedores[i]["Productos"]["PlatoComida"]
                lenghtPltComida=lenghtPltComida+1
        if lenghtPAmarilla>0:
            PAmarilla=      round(PAmarilla/lenghtPAmarilla,2)
        if lenghtPBlanca>0:
            PBlanca=        round(PBlanca/lenghtPBlanca,2)
        if lenghtPYungay>0:
            PYungay=        round(PYungay/lenghtPYungay,2)
        if lenghtCRoja>0:
            CRoja=          round(CRoja/lenghtCRoja,2)
        if lenghtCBlanca>0:
            CBlanca=        round(CBlanca/lenghtCBlanca,2)
        if lenghtTmte>0:
            Tmte=           round(Tmte/lenghtTmte,2)
        if lenghtBolsVerduras>0:
            BolsVerduras=   round(BolsVerduras/lenghtBolsVerduras,2)
        if lenghtMrcuya>0:
            Mrcuya=         round(Mrcuya/lenghtMrcuya,2)
        if lenghtBtllJugo>0:
            BtllJugo=       round(BtllJugo/lenghtBtllJugo,2)
        if lenghtPltComida>0:
            PltComida=      round(PltComida/lenghtPltComida,2)
    Promedios=dict(PapaAmarilla=PAmarilla, PapaBlanca=PBlanca, PapaYungay=PYungay, CebollaRoja=CRoja, CebollaBlanca=CBlanca, Tomate=Tmte,
                BolsitaVerduras=BolsVerduras, Maracuya=Mrcuya, BotellaJugo=BtllJugo, PlatoComida=PltComida)

def W_Average():
    A_Promediar()
    global Promedios
    global ventana_Promedio
    Icon_Home=PhotoImage(file="Home_Icon.png")
    ventana_Promedio=Toplevel(ventana_Main_Menu)
    ventana_Main_Menu.withdraw()
    ventana_Promedio.geometry("520x525")
    ventana_Promedio.title("Mercado Santa Rosita-Promedios de Mercado")
    ventana_Promedio.resizable(False,True)
    scroll=Scrollbar(ventana_Promedio)
    wind=Canvas(ventana_Promedio, yscrollcommand=scroll.set)
    scroll.config(command=wind.yview)
    scroll.pack(side=RIGHT, fill=Y)
    window_Promedio=Frame(wind)
    wind.pack(fill="both",expand=True)
    wind.create_window(0,0,window=window_Promedio,anchor="nw")
    Label(window_Promedio, text = "Promedios del Mercado", font = "MesloLG 35 underline").pack()
    Label(window_Promedio, text = "Mercado " '"Santa Rosita"\n', font = "MesloLG 28 underline").pack()

    #Productos
    Label(window_Promedio, text="Papa Amarilla= S/."+str(Promedios["PapaAmarilla"]), font = "MesloLG 20 ").pack()
    Label(window_Promedio, text="Papa Blanca= S/."+str(Promedios["PapaBlanca"]), font = "MesloLG 20 ").pack()
    Label(window_Promedio, text="Papa Yungay= S/."+str(Promedios["PapaYungay"]), font = "MesloLG 20 ").pack()
    Label(window_Promedio, text="Cebolla Roja= S/."+str(Promedios["CebollaRoja"]), font = "MesloLG 20 ").pack()
    Label(window_Promedio, text="Cebolla Blanca= S/."+str(Promedios["CebollaBlanca"]), font = "MesloLG 20 ").pack()
    Label(window_Promedio, text="Tomate= S/."+str(Promedios["Tomate"]), font = "MesloLG 20 ").pack()
    Label(window_Promedio, text="Bolsita de Verduras= S/."+str(Promedios["BolsitaVerduras"]), font = "MesloLG 20 ").pack()
    Label(window_Promedio, text="Maracuya= S/."+str(Promedios["Maracuya"]), font = "MesloLG 20 ").pack()
    Label(window_Promedio, text="Botella de Jugo= S/."+str(Promedios["BotellaJugo"]), font = "MesloLG 20 ").pack()
    Label(window_Promedio, text="Plato de Comida= S/."+str(Promedios["PlatoComida"]), font = "MesloLG 20 ").pack()
    Home=Button(window_Promedio,image=Icon_Home, bg="Gray",command=A_Exit_W_Average)
    Home.image=Icon_Home
    Home.place(x=20,y=450)
    ventana_Promedio.update()
    wind.config(scrollregion=wind.bbox("all"))

def A_Exit_W_Average():
    ventana_Main_Menu.deiconify()
    ventana_Promedio.destroy()
#Nuevo Vendedor
def W_New_Seller():
    global V_Nuevo_Nombre
    global V_Nuevo_Apellido_Paterno
    global V_Nuevo_Apellido_Materno
    global V_Nuevo_Local
    global V_Nueva_Contraseña
    global V_Nueva_Contraseña_Confirmar
    global V_Nuevo_PapaAmarilla
    global V_Nuevo_PapaBlanca
    global V_Nuevo_PapaYungay
    global V_Nuevo_CebollaRoja
    global V_Nuevo_CebollaBlanca
    global V_Nuevo_Tomate
    global V_Nuevo_BolsitaVerduras
    global V_Nuevo_Maracuya
    global V_Nuevo_BotellaJugo
    global V_Nuevo_PlatoComida

    global ventana_Registro
    ventana_Registro = Toplevel(ventana_Main_Menu)
    ventana_Main_Menu.withdraw()
    ventana_Registro.title("Mercado Santa Rosita-Registro de Vendedor")
    ventana_Registro.geometry("500x500")
    ventana_Registro.resizable(False,False)

    Icon_Home=PhotoImage(file="Home_Icon.png")


    V_Nuevo_Nombre = StringVar()
    V_Nuevo_Apellido_Paterno = StringVar()
    V_Nuevo_Apellido_Materno = StringVar()
    V_Nuevo_Local = IntVar()
    V_Nueva_Contraseña = StringVar()
    V_Nueva_Contraseña_Confirmar = StringVar()

    Label(ventana_Registro, text="Nombre:").place(x=30,y=23)
    Entry(ventana_Registro, textvariable=V_Nuevo_Nombre).place(x=100,y=25)

    Label(ventana_Registro, text="Apellido Paterno:").place(x=230,y=23)
    Entry(ventana_Registro, textvariable=V_Nuevo_Apellido_Paterno).place(x=330,y=25)
    
    Label(ventana_Registro, text="Apellido Materno:").place(x=230,y=53)
    Entry(ventana_Registro, textvariable=V_Nuevo_Apellido_Materno).place(x=330,y=55)
    
    Label(ventana_Registro, text="Local:").place(x=30,y=53)
    Entry(ventana_Registro, textvariable=V_Nuevo_Local).place(x=100,y=55)
    
    Label(ventana_Registro, text="Contraseña:").place(x=30,y=83)
    Entry(ventana_Registro, textvariable=V_Nueva_Contraseña,show="•").place(x=100,y=85)
    
    Label(ventana_Registro, text="Repetir\ncontraseña :").place(x=250,y=73)
    Entry(ventana_Registro, textvariable=V_Nueva_Contraseña_Confirmar,show="•").place(x=330,y=85)

    V_Nuevo_PapaAmarilla=StringVar()
    V_Nuevo_PapaBlanca=StringVar()
    V_Nuevo_PapaYungay=StringVar()
    V_Nuevo_CebollaRoja=StringVar()
    V_Nuevo_CebollaBlanca=StringVar()
    V_Nuevo_Tomate=StringVar()
    V_Nuevo_BolsitaVerduras=StringVar()
    V_Nuevo_Maracuya=StringVar()
    V_Nuevo_BotellaJugo=StringVar()
    V_Nuevo_PlatoComida=StringVar()

    V_Nuevo_PapaAmarilla.set("0")
    V_Nuevo_PapaBlanca.set("0")
    V_Nuevo_PapaYungay.set("0")
    V_Nuevo_CebollaRoja.set("0")
    V_Nuevo_CebollaBlanca.set("0")
    V_Nuevo_Tomate.set("0")
    V_Nuevo_BolsitaVerduras.set("0")
    V_Nuevo_Maracuya.set("0")
    V_Nuevo_BotellaJugo.set("0")
    V_Nuevo_PlatoComida.set("0")
    
    Label(ventana_Registro,text="• Papa Amarilla").place(x=30,y=118)
    Label(ventana_Registro,text="S/.").place(x=150,y=118)
    Entry(ventana_Registro,width=10,textvariable=V_Nuevo_PapaAmarilla).place(x=170,y=120)
    Label(ventana_Registro,text="/Kg").place(x=235,y=118)
    Label(ventana_Registro,text="• Papa Blanca").place(x=30,y=148)
    Label(ventana_Registro,text="S/.").place(x=150,y=148)
    Entry(ventana_Registro,width=10,textvariable=V_Nuevo_PapaBlanca).place(x=170,y=150)
    Label(ventana_Registro,text="/Kg").place(x=235,y=148)
    Label(ventana_Registro,text="• Papa Yungay").place(x=30,y=178)
    Label(ventana_Registro,text="S/.").place(x=150,y=178)
    Entry(ventana_Registro,width=10,textvariable=V_Nuevo_PapaYungay).place(x=170,y=180)
    Label(ventana_Registro,text="/Kg").place(x=235,y=178)
    Label(ventana_Registro,text="• Cebolla Roja").place(x=30,y=208)
    Label(ventana_Registro,text="S/.").place(x=150,y=208)
    Entry(ventana_Registro,width=10,textvariable=V_Nuevo_CebollaRoja).place(x=170,y=210)
    Label(ventana_Registro,text="/Kg").place(x=235,y=208)
    Label(ventana_Registro,text="• Cebolla Blanca").place(x=30,y=238)
    Label(ventana_Registro,text="S/.").place(x=150,y=238)
    Entry(ventana_Registro,width=10,textvariable=V_Nuevo_CebollaBlanca).place(x=170,y=240)
    Label(ventana_Registro,text="/Kg").place(x=235,y=238)
    Label(ventana_Registro,text="• Tomate").place(x=30,y=268)
    Label(ventana_Registro,text="S/.").place(x=150,y=268)
    Entry(ventana_Registro,width=10,textvariable=V_Nuevo_Tomate).place(x=170,y=270)
    Label(ventana_Registro,text="/Kg").place(x=235,y=268)
    Label(ventana_Registro,text="• Bolsita de Verduras").place(x=30,y=298)
    Label(ventana_Registro,text="S/.").place(x=150,y=298)
    Entry(ventana_Registro,width=10,textvariable=V_Nuevo_BolsitaVerduras).place(x=170,y=300)
    Label(ventana_Registro,text="/Kg").place(x=235,y=298)
    Label(ventana_Registro,text="• Maracuyá").place(x=30,y=328)
    Label(ventana_Registro,text="S/.").place(x=150,y=328)
    Entry(ventana_Registro,width=10,textvariable=V_Nuevo_Maracuya).place(x=170,y=330)
    Label(ventana_Registro,text="/Kg").place(x=235,y=328)
    Label(ventana_Registro,text="• Botella de Jugo").place(x=30,y=358)
    Label(ventana_Registro,text="S/.").place(x=150,y=358)
    Entry(ventana_Registro,width=10,textvariable=V_Nuevo_BotellaJugo).place(x=170,y=360)
    Label(ventana_Registro,text="/Kg").place(x=235,y=358)
    Label(ventana_Registro,text="• Plato de Comida").place(x=30,y=388)
    Label(ventana_Registro,text="S/.").place(x=150,y=388)
    Entry(ventana_Registro,width=10,textvariable=V_Nuevo_PlatoComida).place(x=170,y=390)
    Label(ventana_Registro,text="/Kg").place(x=235,y=388)
    Button(ventana_Registro,text="Continuar",bg="Light gray",command=A_New_Seller).place(x=390,y=450)
    Home=Button(ventana_Registro,image=Icon_Home, bg="Gray",command=A_Exit_W_New_Seller)
    Home.image=Icon_Home
    Home.place(x=30,y=420)

def A_Exit_W_New_Seller():
    ventana_Main_Menu.deiconify()
    ventana_Registro.destroy()
    
def A_New_Seller():
    global V_Nuevo_Nombre
    global V_Nuevo_Apellido_Paterno
    global V_Nuevo_Apellido_Materno
    global V_Nuevo_Local
    global V_Nueva_Contraseña
    global V_Nueva_Contraseña_Confirmar
    global V_Nuevo_PapaAmarilla
    global V_Nuevo_PapaBlanca
    global V_Nuevo_PapaYungay
    global V_Nuevo_CebollaRoja
    global V_Nuevo_CebollaBlanca
    global V_Nuevo_Tomate
    global V_Nuevo_BolsitaVerduras
    global V_Nuevo_Maracuya
    global V_Nuevo_BotellaJugo
    global V_Nuevo_PlatoComida
    global Vendedores
    Contador_Locales=0

    print("Registrando...")

    if V_Nuevo_Nombre.get()!=""and V_Nuevo_Apellido_Paterno.get()!=""and V_Nuevo_Local.get()!=""and V_Nueva_Contraseña.get()!="":
        lenght=len(Vendedores)
        if int(V_Nuevo_Local.get())>=999:
            Contador_Locales=Contador_Locales+1
        for i in range(0,lenght):
            if str(Vendedores[i]["Local"])==str(V_Nuevo_Local.get()) or int(V_Nuevo_Local.get())>=999:                
                Contador_Locales=Contador_Locales+1
        if Contador_Locales==0:
            if V_Nueva_Contraseña.get()==V_Nueva_Contraseña_Confirmar.get():
                Productos_Temporales=dict(PapaAmarilla=float(V_Nuevo_PapaAmarilla.get()), PapaBlanca=float(V_Nuevo_PapaBlanca.get()), PapaYungay=float(V_Nuevo_PapaYungay.get()), CebollaRoja=float(V_Nuevo_CebollaRoja.get()), CebollaBlanca=float(V_Nuevo_CebollaBlanca.get()), Tomate=float(V_Nuevo_Tomate.get()),
                        BolsitaVerduras=float(V_Nuevo_BolsitaVerduras.get()), Maracuya=float(V_Nuevo_Maracuya.get()), BotellaJugo=float(V_Nuevo_BotellaJugo.get()), PlatoComida=float(V_Nuevo_PlatoComida.get()))
                Vendedor_Temporal=dict(Nombre=str(V_Nuevo_Nombre.get()), ApPaterno=str(V_Nuevo_Apellido_Paterno.get()), ApMaterno=str(V_Nuevo_Apellido_Materno.get()), Local=int(V_Nuevo_Local.get()), Contraseña=str(V_Nueva_Contraseña.get()), Productos=Productos_Temporales)
                Vendedores.append(Vendedor_Temporal)
                messagebox.showinfo("Exito","Registro Exitoso")
                A_Exit_W_New_Seller()
            else:
                messagebox.showerror("Contraseñas no coinciden","Las contraseñas no coinciden")
        else:
            messagebox.showerror("Local ya Registrado","Para modificar datos de un local ya existente contacte a Administración, elimine con ellos o actualice los datos por medio del inicio de sesión")
    else:
        messagebox.showerror("Casillas Vacías","No dejes ninguna casilla importante vacía")

#Buscar Datos Vendedor
def W_Search_Seller():
    global ventana_Buscar_Vendedor
    global V_Search_Nombre
    global V_Search_Apellido_Paterno
    global V_Search_Apellido_Materno
    global V_Search_Local_Number
    global Contador_Contraseña
    Contador_Contraseña=0
    V_Search_Nombre=StringVar()
    V_Search_Apellido_Paterno=StringVar()
    V_Search_Apellido_Materno=StringVar()
    V_Search_Local_Number=StringVar()
    Icon_Home=PhotoImage(file="Home_Icon.png")
    ventana_Buscar_Vendedor=Toplevel(ventana_Main_Menu)
    ventana_Main_Menu.withdraw()
    ventana_Buscar_Vendedor.geometry("250x275")
    ventana_Buscar_Vendedor.title("Mercado Santa Rosita-Buscar un Vendedor")
    ventana_Buscar_Vendedor.resizable(False,False)
    Label(ventana_Buscar_Vendedor,text="Nombre").pack()
    Entry(ventana_Buscar_Vendedor,textvariable=V_Search_Nombre).pack()
    Label(ventana_Buscar_Vendedor,text="Apellido Paterno").pack()
    Entry(ventana_Buscar_Vendedor,textvariable=V_Search_Apellido_Paterno).pack()
    Label(ventana_Buscar_Vendedor,text="Apellido Materno").pack()
    Entry(ventana_Buscar_Vendedor,textvariable=V_Search_Apellido_Materno).pack()
    Label(ventana_Buscar_Vendedor,text="Número de Local").pack()
    Entry(ventana_Buscar_Vendedor,textvariable=V_Search_Local_Number).pack()
    Button(ventana_Buscar_Vendedor,text="Continuar",command=A_Show_Seller).pack()
    Home=Button(ventana_Buscar_Vendedor,image=Icon_Home, bg="Gray",command=A_Exit_W_Search_Seller)
    Home.image=Icon_Home
    Button(ventana_Buscar_Vendedor,text=" Log \nIn", bg="Gray",command=A_Login_Search,font="Consolas 11",fg="white").place(x=180,y=200)    
    Home.place(x=20,y=200)
    
def A_Show_Seller():
    global Answ_Posicion
    global Answ_Nombre
    global Answ_Apellido_Paterno
    global Answ_Apellido_Materno
    global Answ_Local_Number
    if A_Locate_Seller(1)==True:
        Answ_Nombre=Vendedores[Answ_Posicion]["Nombre"]
        Answ_Apellido_Paterno=Vendedores[Answ_Posicion]["ApPaterno"]
        Answ_Apellido_Materno=Vendedores[Answ_Posicion]["ApMaterno"]
        Answ_Local_Number_Interger=int(Vendedores[Answ_Posicion]["Local"])
        Answ_Local_Number=str(Answ_Local_Number_Interger)

        Question=messagebox.askquestion("Confirmación","El nombre que busca es: " +str(Answ_Nombre)+" "+str(Answ_Apellido_Paterno)+" "+str(Answ_Apellido_Materno)+"\n del local: "+str(Answ_Local_Number) )
        if Question=="yes":
            W_Show_Seller()            
        else:
            messagebox.showerror("Vuelva a intentarlo", "Vuelva a introducir datos, el mas importante es el número de Local")
    elif A_Locate_Seller(2)>3:
        if A_Locate_Seller(4)==True:
            messagebox.showerror("Vuelva a intentarlo", "Vuelva a introducir datos, encontramos un duplicado con los datos ingresados, sea más especifico, el mas importante es el número de Local")
        else:
            messagebox.showerror("Vuelva a intentarlo", "Vuelva a introducir datos, el mas importante es el número de Local")
    else:
        print("ERROR SHOW SELLER")

def W_Show_Seller():
    global Vendedores
    global ventana_Mostrar_Vendedor
    global Answ_Posicion
    Icon_Home=PhotoImage(file="Home_Icon.png")
    ventana_Mostrar_Vendedor=Toplevel(ventana_Main_Menu)
    ventana_Main_Menu.withdraw()
    ventana_Buscar_Vendedor.destroy()
    ventana_Mostrar_Vendedor.geometry("520x525")
    ventana_Mostrar_Vendedor.title("Mercado Santa Rosita-Promedios de Mercado")
    ventana_Mostrar_Vendedor.resizable(False,True)
    scroll=Scrollbar(ventana_Mostrar_Vendedor)
    wind=Canvas(ventana_Mostrar_Vendedor, yscrollcommand=scroll.set)
    scroll.config(command=wind.yview)
    scroll.pack(side=RIGHT, fill=Y)
    window_Mostrar_Vendedor=Frame(wind)
    wind.pack(fill="both",expand=True)
    wind.create_window(0,0,window=window_Mostrar_Vendedor,anchor="nw")
    Label(window_Mostrar_Vendedor, text = Answ_Nombre+" "+Answ_Apellido_Paterno, font = "MesloLG 35 underline").pack()
    Label(window_Mostrar_Vendedor, text = "Mercado " '"Santa Rosita", local:'+str(Answ_Local_Number), font = "MesloLG 25 underline").pack()
    
    #Productos
    if Vendedores[Answ_Posicion]["Productos"]["PapaAmarilla"]>0:
        Label(window_Mostrar_Vendedor, text="Papa Amarilla= S/."       +str(Vendedores[Answ_Posicion]["Productos"]["PapaAmarilla"])     , font = "MesloLG 20 ").pack()
    if Vendedores[Answ_Posicion]["Productos"]["PapaBlanca"]>0:
        Label(window_Mostrar_Vendedor, text="Papa Blanca= S/."         +str(Vendedores[Answ_Posicion]["Productos"]["PapaBlanca"])       , font = "MesloLG 20 ").pack()
    if Vendedores[Answ_Posicion]["Productos"]["PapaYungay"]>0:
        Label(window_Mostrar_Vendedor, text="Papa Yungay= S/."         +str(Vendedores[Answ_Posicion]["Productos"]["PapaYungay"])       , font = "MesloLG 20 ").pack()
    if Vendedores[Answ_Posicion]["Productos"]["CebollaRoja"]>0:
        Label(window_Mostrar_Vendedor, text="Cebolla Roja= S/."        +str(Vendedores[Answ_Posicion]["Productos"]["CebollaRoja"])      , font = "MesloLG 20 ").pack()
    if Vendedores[Answ_Posicion]["Productos"]["CebollaBlanca"]>0:
        Label(window_Mostrar_Vendedor, text="Cebolla Blanca= S/."      +str(Vendedores[Answ_Posicion]["Productos"]["CebollaBlanca"])    , font = "MesloLG 20 ").pack()
    if Vendedores[Answ_Posicion]["Productos"]["Tomate"]>0:
        Label(window_Mostrar_Vendedor, text="Tomate= S/."              +str(Vendedores[Answ_Posicion]["Productos"]["Tomate"])           , font = "MesloLG 20 ").pack()
    if Vendedores[Answ_Posicion]["Productos"]["BolsitaVerduras"]>0:
        Label(window_Mostrar_Vendedor, text="Bolsita de Verduras= S/." +str(Vendedores[Answ_Posicion]["Productos"]["BolsitaVerduras"])  , font = "MesloLG 20 ").pack()
    if Vendedores[Answ_Posicion]["Productos"]["Maracuya"]>0:
        Label(window_Mostrar_Vendedor, text="Maracuya= S/."            +str(Vendedores[Answ_Posicion]["Productos"]["Maracuya"])         , font = "MesloLG 20 ").pack()
    if Vendedores[Answ_Posicion]["Productos"]["BotellaJugo"]>0:
        Label(window_Mostrar_Vendedor, text="Botella de Jugo= S/."     +str(Vendedores[Answ_Posicion]["Productos"]["BotellaJugo"])      , font = "MesloLG 20 ").pack()
    if Vendedores[Answ_Posicion]["Productos"]["PlatoComida"]>0:
        Label(window_Mostrar_Vendedor, text="Plato de Comida= S/."     +str(Vendedores[Answ_Posicion]["Productos"]["PlatoComida"])      , font = "MesloLG 20 ").pack()
    Home=Button(window_Mostrar_Vendedor,image=Icon_Home, bg="Gray",command=A_Exit_W_Show_Seller)
    Label(window_Mostrar_Vendedor,text="                                                                \n \n \n \n \n \n \n ", font = "MesloLG 20 ").pack()
    Home.image=Icon_Home
    Home.place(x=15,y=100)
    Button(window_Mostrar_Vendedor,text=" Log \nIn", bg="Gray",command=A_Login_Show,font="Consolas 11",fg="white").place(x=435,y=100)
    ventana_Mostrar_Vendedor.update()
    wind.config(scrollregion=wind.bbox("all"))

def A_Exit_W_Search_Seller():
    ventana_Main_Menu.deiconify()
    ventana_Buscar_Vendedor.destroy()

def A_Exit_W_Show_Seller():
    ventana_Main_Menu.deiconify()
    ventana_Mostrar_Vendedor.destroy()

def A_Locate_Seller(Devolver):
    
    global Vendedores
    global Answ_Posicion
    global Answ_Nombre
    global Answ_Apellido_Paterno
    global Answ_Apellido_Materno
    global Answ_Local_Number

    V_Nombre=V_Search_Nombre.get()
    V_Apellido_Paterno=V_Search_Apellido_Paterno.get()
    V_Apellido_Materno=V_Search_Apellido_Materno.get()
    if str(V_Search_Local_Number.get())=="":
        V_Local_Number=-1
    else:
        V_Local_Number=str(int(V_Search_Local_Number.get()))
    length=len(Vendedores)
    i=0

    Contador_Comprobaciones=0
    Bool_Comprobaciones=False
    Contador_NombreApellido=0
    Bool_NombreApellido=True
    Contador_ApellidoPaternoMaterno=0
    Bool_ApellidoPaternoMaterno=False
    Contador_Numero_Local=0
    Bool_Numero_Local=False
    ErrorDuplicado=False

    posicion=-1
    
    while Contador_Comprobaciones<=3 and Bool_Comprobaciones==False:
        if Contador_NombreApellido>1 and Bool_NombreApellido==True:
            i=0
            Bool_NombreApellido=False
            Bool_ApellidoPaternoMaterno=True                
        if Contador_ApellidoPaternoMaterno>1 and Bool_ApellidoPaternoMaterno==True:
            i=0
            Bool_ApellidoPaternoMaterno=False
            Bool_Numero_Local=True
        if Contador_Numero_Local>1 and Bool_Numero_Local==True:
            Bool_Numero_Local=False
            posicion=-1
        while i<length+1:
            if i<length:
                if Bool_NombreApellido==True:
                    if V_Nombre.lower()+V_Apellido_Paterno.lower()==str(Vendedores[i]["Nombre"]).lower()+str(Vendedores[i]["ApPaterno"]).lower():
                        Contador_NombreApellido=Contador_NombreApellido+1
                        posicion=i
                        if Contador_NombreApellido<2:
                            Bool_Comprobaciones=True
                        else:
                            Bool_Comprobaciones=False
                            print("Encontramos un Duplicado")
                            ErrorDuplicado=True
                    print("Comprobando NOMBRE")
                elif Bool_ApellidoPaternoMaterno==True:
                    if V_Apellido_Paterno.lower()+V_Apellido_Materno.lower()==str(Vendedores[i]["ApPaterno"]).lower()+str(Vendedores[i]["ApMaterno"]).lower():
                        Contador_ApellidoPaternoMaterno=Contador_ApellidoPaternoMaterno+1
                        posicion=i
                        if Contador_ApellidoPaternoMaterno<2:
                            Bool_Comprobaciones=True
                        else:
                            Bool_Comprobaciones=False
                            print("Encontramos un Duplicado")
                            ErrorDuplicado=True
                    print("Comprobando APELLIDO")
                elif Bool_Numero_Local==True:
                    if str(V_Local_Number).lower()==str(Vendedores[i]["Local"]).lower():
                        Contador_Numero_Local=Contador_Numero_Local+1
                        posicion=i
                        if Contador_Numero_Local<2:
                            Bool_Comprobaciones=True
                        else:
                            Bool_Comprobaciones=False
                            print("Encontramos un Duplicado")
                            ErrorDuplicado=True
                    print("Comprobando LOCAL")
            i=i+1
            print(i)        
        print(Contador_Comprobaciones)
        i=0
        if Contador_Comprobaciones==0:
            Contador_NombreApellido=1000
        elif Contador_Comprobaciones==1:
            Contador_ApellidoPaternoMaterno=1000
        elif Contador_Comprobaciones==2:
            Contador_Numero_Local=1000
        Contador_Comprobaciones=Contador_Comprobaciones+1
    if posicion!=-1:
        Answ_Posicion=posicion
    else:
        Bool_Comprobaciones=False
        Contador_Comprobaciones>1000
        print("No Encontramos Coincidencias")
    if Devolver==1:
        print("Bool Comprobaciones"+str(Bool_Comprobaciones))
        return Bool_Comprobaciones
    if Devolver==2:
        print("Contador Comprobaciones"+str(Contador_Comprobaciones))
        return Contador_Comprobaciones
    if Devolver==3:
        return posicion
    if Devolver==4:
        print("Error Duplicado"+str(ErrorDuplicado))
        return ErrorDuplicado

def A_Login_Search():
    A_Login("Search")

def A_Login_Show():
    A_Login("Show")

def A_Login(variable):
    global ventana_Buscar_Vendedor
    global ventana_Mostrar_Vendedor
    global Answ_Posicion
    global Answ_Nombre
    global Answ_Apellido_Paterno
    global Answ_Apellido_Materno
    global Answ_Local_Number
    if A_Locate_Seller(1)==True:
        Answ_Nombre=Vendedores[Answ_Posicion]["Nombre"]
        Answ_Apellido_Paterno=Vendedores[Answ_Posicion]["ApPaterno"]
        Answ_Apellido_Materno=Vendedores[Answ_Posicion]["ApMaterno"]
        Answ_Local_Number=Vendedores[Answ_Posicion]["Local"]

        Question=messagebox.askquestion("Confirmación","El nombre que busca es: " +str(Answ_Nombre)+" "+str(Answ_Apellido_Paterno)+" "+str(Answ_Apellido_Materno)+"\n del local: "+str(Answ_Local_Number) )
        if Question=="yes":
            W_Login(Answ_Nombre,Answ_Apellido_Paterno,Answ_Apellido_Materno,Answ_Local_Number)
            if variable=="Search":
                ventana_Buscar_Vendedor.destroy()
            elif variable=="Show":
                ventana_Mostrar_Vendedor.destroy()          
        else:
            Confirmation=messagebox.askquestion("Confirmación","¿Desea continuar con el inicio de sesión?, igualmente podrá continuar con el llenado de datos en la siguiente página")
            if Confirmation=="yes":
                W_Login()
                if variable=="Search":
                    ventana_Buscar_Vendedor.destroy()
                elif variable=="Show":
                    ventana_Mostrar_Vendedor.destroy()
    elif A_Locate_Seller(2)>3:
        W_Login()
        if variable=="Search":
            ventana_Buscar_Vendedor.destroy()
        elif variable=="Show":
            ventana_Mostrar_Vendedor.destroy()
    else:
        print("ERROR SHOW SELLER")

def W_Login(Log_Nombre="",Log_ApPaterno="",Log_ApMaterno="",Log_Local=""):
    global ventana_Login
    global V_Login_Nombre
    global V_Login_Apellido_Paterno
    global V_Login_Apellido_Materno
    global V_Login_Local_Number
    global V_Login_Contraseña
    V_Login_Nombre=StringVar()
    V_Login_Apellido_Paterno=StringVar()
    V_Login_Apellido_Materno=StringVar()
    V_Login_Local_Number=StringVar()
    V_Login_Contraseña=StringVar()
    V_Login_Nombre.set(Log_Nombre)
    V_Login_Apellido_Paterno.set(Log_ApPaterno)
    V_Login_Apellido_Materno.set(Log_ApMaterno)
    V_Login_Local_Number.set(Log_Local)
    Icon_Home=PhotoImage(file="Home_Icon.png")
    ventana_Login=Toplevel(ventana_Main_Menu)
    ventana_Main_Menu.withdraw()
    ventana_Login.geometry("250x275")
    ventana_Login.title("Mercado Santa Rosita-LogIn")
    ventana_Login.resizable(False,False)
    Label(ventana_Login,text="Nombre").pack()
    Entry(ventana_Login,textvariable=V_Login_Nombre).pack()
    Label(ventana_Login,text="Apellido Paterno").pack()
    Entry(ventana_Login,textvariable=V_Login_Apellido_Paterno).pack()
    Label(ventana_Login,text="Apellido Materno").pack()
    Entry(ventana_Login,textvariable=V_Login_Apellido_Materno).pack()
    Label(ventana_Login,text="Número de Local").pack()
    Entry(ventana_Login,textvariable=V_Login_Local_Number).pack()
    Label(ventana_Login,text="Contraseña").pack()
    Entry(ventana_Login,textvariable=V_Login_Contraseña,show="•").pack()
    Button(ventana_Login,text="Continuar",command=A_Login_Comparate).pack()
    Home=Button(ventana_Login,image=Icon_Home, bg="Gray",command=A_Exit_W_Login)
    Home.image=Icon_Home
    Home.place(x=20,y=215)

def A_Login_Comparate(): #MasterKey Aplicada
    global MasterKey
    global Login_Position
    global Contador_Contraseña
    global Encontrado
    Login_Nombre=V_Login_Nombre.get()
    Login_Apellido_Paterno=V_Login_Apellido_Paterno.get()
    Login_Apellido_Materno=V_Login_Apellido_Materno.get()
    Login_Local_Number=V_Login_Local_Number.get()
    Login_Contraseña=V_Login_Contraseña.get()
    Encontrado=False
    length=len(Vendedores)
    for i in range(0,length):
        if str(Login_Nombre).lower()+str(Login_Apellido_Paterno).lower()+str(Login_Apellido_Materno).lower()+str(Login_Local_Number).lower()==str(Vendedores[i]["Nombre"]).lower()+str(Vendedores[i]["ApPaterno"]).lower()+str(Vendedores[i]["ApMaterno"]).lower()+str(Vendedores[i]["Local"]).lower():
            Login_Position=i
            Encontrado=True
    if Encontrado==True:
        if str(Login_Contraseña)==Vendedores[Login_Position]["Contraseña"] or str(Login_Contraseña)==MasterKey:
            W_Update_Seller()
            ventana_Login.destroy()
        else:
            messagebox.showerror("Datos Errados","Contraseña Incorrecta")
            Contador_Contraseña=Contador_Contraseña+1
    elif Encontrado==False:
        messagebox.showerror("Datos Errados","No Hemos Encontrado Coincidencias, Verifica los Datos")
    if Contador_Contraseña>=3:
        A_Exit_W_Login()
        messagebox.showerror("Fallo Reiterado","Fallaste la contraseña 3 veces")

def A_Exit_W_Login():
    ventana_Login.destroy()
    ventana_Main_Menu.deiconify()

def W_Update_Seller():
    global V_Update_Nombre
    global V_Update_Apellido_Paterno
    global V_Update_Apellido_Materno
    global V_Update_Local
    global V_Update_Contraseña
    global V_Update_Contraseña_Confirmar
    global V_Update_PapaAmarilla
    global V_Update_PapaBlanca
    global V_Update_PapaYungay
    global V_Update_CebollaRoja
    global V_Update_CebollaBlanca
    global V_Update_Tomate
    global V_Update_BolsitaVerduras
    global V_Update_Maracuya
    global V_Update_BotellaJugo
    global V_Update_PlatoComida

    global ventana_Actualizar
    ventana_Actualizar = Toplevel(ventana_Main_Menu)
    ventana_Main_Menu.withdraw()
    ventana_Actualizar.title("Mercado Santa Rosita-Actualizar Vendedor")
    ventana_Actualizar.geometry("500x500")
    ventana_Actualizar.resizable(False,False)
    Icon_Home=PhotoImage(file="Home_Icon.png")


    V_Update_Nombre = StringVar()
    V_Update_Apellido_Paterno = StringVar()
    V_Update_Apellido_Materno = StringVar()
    V_Update_Local = IntVar()
    V_Update_Contraseña = StringVar()
    V_Update_Contraseña_Confirmar = StringVar()

    V_Update_Nombre.set(Vendedores[Login_Position]["Nombre"])
    V_Update_Apellido_Paterno.set(Vendedores[Login_Position]["ApPaterno"])
    V_Update_Apellido_Materno.set(Vendedores[Login_Position]["ApMaterno"])
    V_Update_Local.set(int(Vendedores[Login_Position]["Local"]))


    Label(ventana_Actualizar, text="Nombre:").place(x=30,y=23)
    Entry(ventana_Actualizar, textvariable=V_Update_Nombre).place(x=100,y=25)

    Label(ventana_Actualizar, text="Apellido Paterno:").place(x=230,y=23)
    Entry(ventana_Actualizar, textvariable=V_Update_Apellido_Paterno).place(x=330,y=25)
    
    Label(ventana_Actualizar, text="Apellido Materno:").place(x=230,y=53)
    Entry(ventana_Actualizar, textvariable=V_Update_Apellido_Materno).place(x=330,y=55)
    
    Label(ventana_Actualizar, text="Local:").place(x=30,y=53)
    Entry(ventana_Actualizar, textvariable=V_Update_Local).place(x=100,y=55)
    
    Label(ventana_Actualizar, text="Contraseña:").place(x=30,y=83)
    Entry(ventana_Actualizar, textvariable=V_Update_Contraseña,show="•").place(x=100,y=85)
    
    Label(ventana_Actualizar, text="Repetir\ncontraseña :").place(x=250,y=73)
    Entry(ventana_Actualizar, textvariable=V_Update_Contraseña_Confirmar,show="•").place(x=330,y=85)

    V_Update_PapaAmarilla=StringVar()
    V_Update_PapaBlanca=StringVar()
    V_Update_PapaYungay=StringVar()
    V_Update_CebollaRoja=StringVar()
    V_Update_CebollaBlanca=StringVar()
    V_Update_Tomate=StringVar()
    V_Update_BolsitaVerduras=StringVar()
    V_Update_Maracuya=StringVar()
    V_Update_BotellaJugo=StringVar()
    V_Update_PlatoComida=StringVar()
    
    V_Update_PapaAmarilla.set(Vendedores[Login_Position]["Productos"]["PapaAmarilla"])
    V_Update_PapaBlanca.set(Vendedores[Login_Position]["Productos"]["PapaBlanca"])
    V_Update_PapaYungay.set(Vendedores[Login_Position]["Productos"]["PapaYungay"])
    V_Update_CebollaRoja.set(Vendedores[Login_Position]["Productos"]["CebollaRoja"])
    V_Update_CebollaBlanca.set(Vendedores[Login_Position]["Productos"]["CebollaBlanca"])
    V_Update_Tomate.set(Vendedores[Login_Position]["Productos"]["Tomate"])
    V_Update_BolsitaVerduras.set(Vendedores[Login_Position]["Productos"]["BolsitaVerduras"])
    V_Update_Maracuya.set(Vendedores[Login_Position]["Productos"]["Maracuya"])
    V_Update_BotellaJugo.set(Vendedores[Login_Position]["Productos"]["BotellaJugo"])
    V_Update_PlatoComida.set(Vendedores[Login_Position]["Productos"]["PlatoComida"])

    Label(ventana_Actualizar,text="Cualquier dato que altere afectará\n a su PERFIL de vendedor.\nTenga cuidado manipulando,\n Si no desea cambiar la contraseña,\n deje las casillas en blanco",relief=RIDGE).place(x=285,y=200)
    Label(ventana_Actualizar,text="• Papa Amarilla").place(x=30,y=118)
    Label(ventana_Actualizar,text="S/.").place(x=150,y=118)
    Entry(ventana_Actualizar,width=10,textvariable=V_Update_PapaAmarilla).place(x=170,y=120)
    Label(ventana_Actualizar,text="/Kg").place(x=235,y=118)
    Label(ventana_Actualizar,text="• Papa Blanca").place(x=30,y=148)
    Label(ventana_Actualizar,text="S/.").place(x=150,y=148)
    Entry(ventana_Actualizar,width=10,textvariable=V_Update_PapaBlanca).place(x=170,y=150)
    Label(ventana_Actualizar,text="/Kg").place(x=235,y=148)
    Label(ventana_Actualizar,text="• Papa Yungay").place(x=30,y=178)
    Label(ventana_Actualizar,text="S/.").place(x=150,y=178)
    Entry(ventana_Actualizar,width=10,textvariable=V_Update_PapaYungay).place(x=170,y=180)
    Label(ventana_Actualizar,text="/Kg").place(x=235,y=178)
    Label(ventana_Actualizar,text="• Cebolla Roja").place(x=30,y=208)
    Label(ventana_Actualizar,text="S/.").place(x=150,y=208)
    Entry(ventana_Actualizar,width=10,textvariable=V_Update_CebollaRoja).place(x=170,y=210)
    Label(ventana_Actualizar,text="/Kg").place(x=235,y=208)
    Label(ventana_Actualizar,text="• Cebolla Blanca").place(x=30,y=238)
    Label(ventana_Actualizar,text="S/.").place(x=150,y=238)
    Entry(ventana_Actualizar,width=10,textvariable=V_Update_CebollaBlanca).place(x=170,y=240)
    Label(ventana_Actualizar,text="/Kg").place(x=235,y=238)
    Label(ventana_Actualizar,text="• Tomate").place(x=30,y=268)
    Label(ventana_Actualizar,text="S/.").place(x=150,y=268)
    Entry(ventana_Actualizar,width=10,textvariable=V_Update_Tomate).place(x=170,y=270)
    Label(ventana_Actualizar,text="/Kg").place(x=235,y=268)
    Label(ventana_Actualizar,text="• Bolsita de Verduras").place(x=30,y=298)
    Label(ventana_Actualizar,text="S/.").place(x=150,y=298)
    Entry(ventana_Actualizar,width=10,textvariable=V_Update_BolsitaVerduras).place(x=170,y=300)
    Label(ventana_Actualizar,text="/Kg").place(x=235,y=298)
    Label(ventana_Actualizar,text="• Maracuyá").place(x=30,y=328)
    Label(ventana_Actualizar,text="S/.").place(x=150,y=328)
    Entry(ventana_Actualizar,width=10,textvariable=V_Update_Maracuya).place(x=170,y=330)
    Label(ventana_Actualizar,text="/Kg").place(x=235,y=328)
    Label(ventana_Actualizar,text="• Botella de Jugo").place(x=30,y=358)
    Label(ventana_Actualizar,text="S/.").place(x=150,y=358)
    Entry(ventana_Actualizar,width=10,textvariable=V_Update_BotellaJugo).place(x=170,y=360)
    Label(ventana_Actualizar,text="/Kg").place(x=235,y=358)
    Label(ventana_Actualizar,text="• Plato de Comida").place(x=30,y=388)
    Label(ventana_Actualizar,text="S/.").place(x=150,y=388)
    Entry(ventana_Actualizar,width=10,textvariable=V_Update_PlatoComida).place(x=170,y=390)
    Label(ventana_Actualizar,text="/Kg").place(x=235,y=388)
    Button(ventana_Actualizar,text="Actualizar Datos",bg="Light gray",command=A_Continue_Update_Seller).place(x=390,y=450)
    Home=Button(ventana_Actualizar,image=Icon_Home, bg="Gray",command=A_Exit_W_Update_Seller)
    Home.image=Icon_Home
    Home.place(x=30,y=420)

def A_Exit_W_Update_Seller():
    ventana_Actualizar.destroy()
    ventana_Main_Menu.deiconify()

def A_Continue_Update_Seller():
    Update_Question=messagebox.askquestion("¿Continuar?","Cualquier dato que altere afectará a su PERFIL de vendedor. Tenga cuidado manipulando, si no desea cambiar la contraseña, deje las casillas en blanco")
    if Update_Question=="yes":
        A_Update_Seller()

def A_Update_Seller():
    Contador_Locales=0
    lenght=len(Vendedores)
    if V_Update_Nombre.get()!=""and V_Update_Apellido_Paterno.get()!=""and V_Update_Local.get()!="":
        if int(V_Update_Local.get())>=999:
            Contador_Locales=Contador_Locales+1
        for i in range(0,lenght):
            if str(Vendedores[i]["Local"])!=str(Vendedores[Login_Position]["Local"]):
                if str(Vendedores[i]["Local"])==str(V_Update_Local.get()) or int(V_Update_Local.get())>=999:
                    Contador_Locales=Contador_Locales+1
        if Contador_Locales==0:
            if V_Update_Contraseña.get()!=""and V_Update_Contraseña_Confirmar.get()!="":
                if V_Update_Contraseña.get()==V_Update_Contraseña_Confirmar.get():
                    Productos_Temporales=dict(PapaAmarilla=float(V_Update_PapaAmarilla.get()), PapaBlanca=float(V_Update_PapaBlanca.get()), PapaYungay=float(V_Update_PapaYungay.get()), CebollaRoja=float(V_Update_CebollaRoja.get()), CebollaBlanca=float(V_Update_CebollaBlanca.get()), Tomate=float(V_Update_Tomate.get()),
                            BolsitaVerduras=float(V_Update_BolsitaVerduras.get()), Maracuya=float(V_Update_Maracuya.get()), BotellaJugo=float(V_Update_BotellaJugo.get()), PlatoComida=float(V_Update_PlatoComida.get()))
                    Vendedor_Temporal=dict(Nombre=str(V_Update_Nombre.get()), ApPaterno=str(V_Update_Apellido_Paterno.get()), ApMaterno=str(V_Update_Apellido_Materno.get()), Local=int(V_Update_Local.get()), Contraseña=str(V_Update_Contraseña.get()), Productos=Productos_Temporales)
                    Vendedores[Login_Position]=Vendedor_Temporal
                    messagebox.showinfo("Exito","Registro Exitoso")
                    A_Exit_W_Update_Seller()
                else:
                    messagebox.showerror("Contraseñas no coinciden","Las contraseñas no coinciden")
            else:
                Productos_Temporales=dict(PapaAmarilla=float(V_Update_PapaAmarilla.get()), PapaBlanca=float(V_Update_PapaBlanca.get()), PapaYungay=float(V_Update_PapaYungay.get()), CebollaRoja=float(V_Update_CebollaRoja.get()), CebollaBlanca=float(V_Update_CebollaBlanca.get()), Tomate=float(V_Update_Tomate.get()),
                        BolsitaVerduras=float(V_Update_BolsitaVerduras.get()), Maracuya=float(V_Update_Maracuya.get()), BotellaJugo=float(V_Update_BotellaJugo.get()), PlatoComida=float(V_Update_PlatoComida.get()))
                Vendedor_Temporal=dict(Nombre=str(V_Update_Nombre.get()), ApPaterno=str(V_Update_Apellido_Paterno.get()), ApMaterno=str(V_Update_Apellido_Materno.get()), Local=int(V_Update_Local.get()), Contraseña=str(Vendedores[Login_Position]["Contraseña"]), Productos=Productos_Temporales)
                Vendedores[Login_Position]=Vendedor_Temporal
                messagebox.showinfo("Exito","Registro Exitoso")
                A_Exit_W_Update_Seller()
        else:
            messagebox.showerror("Local ya Registrado","Para modificar datos de un local ya existente contacte a Administración, elimine con ellos o actualice los datos por medio del inicio de sesión")    

#Modo Demo
def A_Demo_Mode():
    global VendedoresDEMO
    global Vendedores
    global DemoinUse
    if DemoinUse==False:
        length=len(VendedoresDEMO)
        for i in range(0,length):
            Vendedores.append(VendedoresDEMO[i])
        DemoinUse=True
        messagebox.showinfo("Éxito","Datos Cargados Exitosamente")
    else:
        print("Ya se aplicaron los valores")
        messagebox.showerror("Error","No podemos cargar los datos 2 veces seguidas.\nEvitamos duplicación de datos")
    A_Close_W_DM()

def A_Delete_Data():
    global Vendedores
    global DemoinUse
    Vendedores=[]
    DemoinUse=False
    messagebox.showinfo("Éxito","Datos Eliminados Exitosamente")
    A_Close_W_DM()

def A_Close_W_DM():
    ventana_Demo_Mode.destroy()

def A_Save_State():
    file=open("Data.txt","w")
    file.write(str(Vendedores))
    file.close()    
    messagebox.showinfo("Exito","Datos Guardados")
    A_Close_W_DM()

def A_Load_State():
    global Vendedores
    file=open("Data.txt","r")
    answer=file.read()
    file.close()
    answer2=yaml.load(answer,CLoader)
    Vendedores=answer2
    messagebox.showinfo("Exito","Datos Cargados")
    A_Close_W_DM()

def A_Create_Backup():
    file=open("BackupsQuantity.txt","r")
    Quantity=int(file.read())
    file.close()
    file=open("BackupsQuantity.txt","w")
    file.write(str(Quantity+1))
    file.close()
    file=open("Backup_"+str(Quantity)+".txt","w")
    file.write(str(Vendedores))
    file.close()
    messagebox.showinfo("Exito","Backup Creado con el nombre "+"Backup_"+str(Quantity)+".txt")
    A_Close_W_DM()

def A_Delete_Backups():
    question=messagebox.askquestion("¿Seguro?","¿Desea Eliminar los datos guardados?")
    if question=="yes":
        file=open("BackupsQuantity.txt","r")
        Quantity=int(file.read())
        file.close()
        for i in range(0,Quantity):
            filename= "Backup_"+str(i)+".txt"      
            if os.path.exists(filename):
                os.remove(filename)                
            else:
                print("The file does not exist")
        file=open("BackupsQuantity.txt","w")
        file.write(str(0))
        file.close()    
    messagebox.showinfo("Exito","Backups Eliminados con Exito")
    A_Close_W_DM()

def A_Delete_State():
    question=messagebox.askquestion("¿Seguro?","¿Desea Eliminar los datos guardados?")
    if question=="yes":
        file=open("Data.txt","w")
        file.write("")
        file.close()    
        messagebox.showinfo("Exito","Datos Borrados")
        A_Close_W_DM()

def W_Demo_Mode():
    global ventana_Demo_Mode
    ventana_Demo_Mode=Toplevel(ventana_Main_Menu)
    ventana_Demo_Mode.title("¿Que Hacemos?")
    ventana_Demo_Mode.geometry("425x305")
    ventana_Demo_Mode.resizable(False,False)
    ImageHelp=PhotoImage(file="Button_Help.png")
    Label(ventana_Demo_Mode,text="¿Que desea hacer?",font="MesloLG 20").pack()
    Question_Label=Label(ventana_Demo_Mode,image=ImageHelp)
    Question_Label.image=ImageHelp
    Question_Label.place(x=30,y=75)
    Label(ventana_Demo_Mode,text="Cargar Datos=Cargar Datos demostración\nBorrar Datos=Borrar Datos actuales\nGuardar Datos=Exportar al almacenamiento los datos\nRecuperar Datos=Importar Datos del almacenamiento\nEliminar Datos=Eliminar Datos del almacenamiento\nCrear un Respaldo=Hacer un respaldo en el directorio",font="MesloLG 10", justify=LEFT).place(x=75,y=45)
    Button(ventana_Demo_Mode,text="Cargar Datos",command=A_Demo_Mode,bg="light gray",font="Consolas 11").place(x=50,y=155)
    Button(ventana_Demo_Mode,text="Borrar Datos",command=A_Delete_Data,bg="light gray",font="Consolas 11").place(x=175,y=155)
    Button(ventana_Demo_Mode,text="Cancel",command=A_Close_W_DM,bg="light gray",font="Consolas 11").place(x=300,y=155)
    Button(ventana_Demo_Mode,text="Guardar Datos",command=A_Save_State,bg="light gray",font="Consolas 11").place(x=50,y=205)
    Button(ventana_Demo_Mode,text="Recuperar Datos",command=A_Load_State,bg="light gray",font="Consolas 11").place(x=190,y=205)
    Button(ventana_Demo_Mode,text="Crear un Respaldo",command=A_Create_Backup,bg="light gray",font="Consolas 11").place(x=50,y=255)
    Button(ventana_Demo_Mode,text="Eliminar Datos",command=A_Delete_State,bg="light gray",font="Consolas 11").place(x=220,y=255)
    Button(ventana_Demo_Mode,text="Eliminar\nRespaldos",command=A_Delete_Backups,bg="light gray",font="Consolas 9").place(x=345,y=200)
#Botones Main Menu
def A_Web():
    WebPage=messagebox.askquestion("Pagina Web","Disculpa, por el momento nuestra pagina esta en proceso.\nSerá redireccionado a 'Youtube' para ver exposición del proyecto\n\n¿Está de Acuerdo?")
    if WebPage== "yes":
        webbrowser.open(linkexpo)

def MB_Help():
    messagebox.showinfo("Ayuda", "Para contactar con el Soporte, puede dirigirse a la seleccion de administracion del mercado.\nPara eliminar, acceder o modificar su usuario ante cualquier problema, contactar con el Soporte Tecnico.")

def A_On_Off():
    apagar = messagebox.askquestion("Apagar aplicacion", "¿Desea terminar  y cerrar la ventana de la aplicacion?")
    if apagar== "yes":
        ventana_Main_Menu.quit()
        ventana_Main_Menu.destroy()
