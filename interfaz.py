import sqlite3
from tkinter import ttk
from tkinter import *

class Turnos:
    def __init__(self, window):
        self.win = window
        self.win.title("Turnos Voar")
        self.win.geometry("2000x2000")
      

        #Creando el frame
        frame = LabelFrame(self.win, text= "Turnos")
        frame.grid(row = "0", column = "0", columnspan = 10, sticky= W + E)

        #Input de día
        dia = Label( text="Día:")
        dia.grid(row=1, column=0)
        self.dia = Entry()
        self.dia.grid(row=1,column=1)

        #Input de fecha
        fecha = Label( text = "Fecha:")
        fecha.grid(row=2, column=0)
        self.fecha = Entry()
        self.fecha.grid(row=2, column=1)

        #Input de mes
        mes = Label( text="Mes:")
        mes.grid(row=3, column=0)
        self.mes = Entry()
        self.mes.grid(row = 3, column = 1)

        #Input de año
        año = Label( text = "Año:")
        año.grid(row = 4, column= 0)
        self.año = Entry()
        self.año.grid(row = 4, column = 1)

        #Input de horario
        horario = Label( text = "Horario:")
        horario.grid(row = 5, column = 0)
        self.horario = Entry()
        self.horario.grid(row = 5, column = 1)

        #Input de cliente
        cliente = Label( text="Cliente:")
        cliente.grid(row = 6, column = 0)
        self.cliente = Entry()
        self.cliente.grid(row = 6, column = 1)

        #Input de servicio
        servicio = Label( text= "Servicio:")
        servicio.grid(row = 7, column = 0)
        self.servicio = Entry()
        self.servicio.grid(row = 7, column = 1)

        #Input Empleado
        empleado = Label( text="Empleado:")
        empleado.grid(row = 8, column = 0)
        self.empleado = Entry()
        self.empleado.grid(row = 8, column= 1)

        #Boton agregar turno 
        ttk.Button(text="Agregar turno", command= self.agregar_turno).grid(row = 9, column = 0,columnspan= 15, sticky = W + E)

        #Output 
        self.mensaje = Label(text = "hola soy un texto a ver que onda", fg= "blue" )
        self.mensaje.grid(row = 10, column= 0, columnspan= 15, sticky = W + E)

        #Buscar por fecha input
        buscar_dia = Label( text = "Dia:")
        buscar_dia.grid(row = 11, column = 0)
        self.buscar_dia = Entry()
        self.buscar_dia.grid(row = 11, column = 1)
        buscar_fecha = Label( text = "Fecha:")
        buscar_fecha.grid(row= 12, column = 0)
        self.buscar_fecha = Entry()
        self.buscar_fecha.grid(row=12, column = 1)
        buscar_mes = Label( text="Mes:")
        buscar_mes.grid(row = 13, column = 0)
        self.buscar_mes = Entry()
        self.buscar_mes.grid(row = 13, column = 1)
        buscar_año = Label(text="Año:")
        buscar_año.grid(row=14, column = 0)
        self.buscar_año = Entry()
        self.buscar_año.grid(row= 14, column = 1)

        #Boton buscar por fecha
        ttk.Button(text="Buscar turno por fecha", command= self.get_turnos_fecha).grid(row= 15, column = 0, columnspan= 15, sticky = W + E)

        #Buscar turnos por mes 
        buscar_turno_por_mes = Label(text = "Mes:")
        buscar_turno_por_mes.grid(row = 16, column = 0)
        self.buscar_turno_por_mes = Entry()
        self.buscar_turno_por_mes.grid(row = 16, column = 1)
        ttk.Button(text = "Buscar por mes", command = self.get_turnos_mes).grid(row = 17, column = 0, columnspan= 15, sticky = W + E)

        #creando las tablas 

        #Etiquetas 
        Label(text= "Ruben").grid(row = 18, column = 0)
        Label(text= "Empleado 2").grid(row = 18, column = 5)

        #Tabla 1 
        self.tree1=  ttk.Treeview(height = 10, columns =[f"#{n}" for n in range(1, 3)]  )
        self.tree1.grid(row= 19, column = 0)
        self.tree1.heading("#0", text = "Horario", anchor = "center")
        self.tree1.heading("#1", text = "Cliente", anchor = "center")
        self.tree1.heading("#2", text = "Servicio", anchor = "center")

        #Tabla 2 
        self.tree2=  ttk.Treeview(height = 10, columns =[f"#{n}" for n in range(1, 3)]  )
        self.tree2.grid(row= 19, column = 5)
        self.tree2.heading("#0", text = "Horario", anchor = "center")
        self.tree2.heading("#1", text = "Cliente", anchor = "center")
        self.tree2.heading("#2", text = "Servicio", anchor = "center")

        #Boton eliminar 
        ttk.Button(text= "Eliminar", command = self.eliminar).grid(row = 33, column = 0, columnspan= 15, sticky = W + E)
        #Inputs eliminar
        eliminar_dia = Label(text="Dia:")
        eliminar_dia.grid(row = 29, column = 0)
        self.eliminar_dia = Entry()
        self.eliminar_dia.grid(row=29, column = 1)
        eliminar_fecha = Label(text="fecha:")
        eliminar_fecha.grid(row = 30, column = 0)
        self.eliminar_fecha = Entry()
        self.eliminar_fecha.grid(row= 30, column = 1)
        eliminar_mes = Label(text="Mes:")
        eliminar_mes.grid(row = 31, column = 0)
        self.eliminar_mes = Entry()
        self.eliminar_mes.grid(row =31, column=1)
        eliminar_cliente = Label(text="Cliente:")
        eliminar_cliente.grid(row=32, column = 0)
        self.eliminar_cliente = Entry()
        self.eliminar_cliente.grid(row=32, column=1)


    #Funcion de conexion a la base de datos y consultas 
    def run_query(self, query, parametros = ()):
        con = sqlite3.connect("voar.db")
        cursor = con.cursor()
        datos = cursor.execute(query, parametros)
        con.commit()
        return datos

    


    #Funcion para obtener datos por fecha 
    def get_turnos_fecha(self): 
        #limpiando las tablas
        records= self.tree1.get_children()
        for element in records:
            self.tree1.delete(element)
         
        records= self.tree2.get_children()
        for element in records:
            self.tree2.delete(element)
        #consultando los datos
        query = "select * from turnos where dia = ? and fecha = ? and mes = ? and año = ? and empleado = 'Ruben'"
        parametros = (self.buscar_dia.get(), self.buscar_fecha.get(), self.buscar_mes.get(), self.buscar_año.get())
        db_rows = self.run_query(query, parametros)
        for row in db_rows:
            self.tree1.insert("", 0, text = row[5], value= (row[6],row[7]))
        query1 = "select * from turnos where dia = ? and fecha = ? and mes = ? and año =? and empleado = 'Empleado 2'"
        parametros1 = (self.buscar_dia.get(), self.buscar_fecha.get(), self.buscar_mes.get(), self.buscar_año.get())
        db_rows = self.run_query(query1, parametros1)
        for row in db_rows:
            self.tree2.insert("", 0, text = row[5], value= (row[6],row[7]))
            print(row)
        self.mensaje["text"] = "Se muestran los turnos del dia {}".format(self.buscar_mes.get())
        
        
    #Funcion para obtener datos por mes
    def get_turnos_mes(self): 
        #limpiando las tablas
        records= self.tree1.get_children()
        for element in records:
            self.tree1.delete(element)
         
        records= self.tree2.get_children()
        for element in records:
            self.tree2.delete(element)   
        #consultando los datos
        query = "select * from turnos where mes = ? and empleado = 'Ruben'"
        parametros = (self.buscar_turno_por_mes.get(),)
        db_rows = self.run_query(query, parametros)
        for row in db_rows:
            self.tree1.insert("", 0, text = row[5], value= (row[6],row[7]))
        query1 = "select * from turnos where mes = ? and empleado = 'Empleado 2'"
        parametros1 = (self.buscar_turno_por_mes.get(),)
        db_rows = self.run_query(query1, parametros1)
        for row in db_rows:
            self.tree2.insert("", 0, text = row[5], value= (row[6],row[7]))
        self.mensaje["text"] = "Se muestran los turnos del mes {}".format(self.buscar_turno_por_mes.get())

    #Funcion para agregar turnos 
    def agregar_turno (self):
        if len(self.dia.get()) !=0 and len(self.fecha.get())!=0 and len(self.mes.get()) !=0 and len(self.año.get())!=0 and len(self.horario.get()) !=0 and len(self.cliente.get())!=0 and len(self.servicio.get()) !=0 and len(self.empleado.get())!=0:
            query = "insert into turnos values(null,?,?,?,?,?,?,?,?)"
            parametros = (self.dia.get(), self.fecha.get(), self.mes.get(), self.año.get(), self.horario.get(), self.cliente.get(),self.servicio.get(), self.empleado.get())
            self.run_query(query, parametros)
            self.mensaje["text"]= "El turno de {} fue cargado correctamente".format(self.cliente.get())

        else:
            self.mensaje["text"]= "Por favor complete todos los parametros"

    #Funcion para eliminar un turno 
    def eliminar (self):
        if len(self.eliminar_dia.get())!=0 and len(self.eliminar_fecha.get())!= 0 and len(self.eliminar_mes.get())!=0 and  len(self.eliminar_cliente.get())!=0:
            query = "delete from turnos where dia = ? and fecha =? and mes =? and cliente =?"
            parametros= (self.eliminar_dia.get(), self.eliminar_fecha.get(), self.eliminar_mes.get(),self.eliminar_cliente.get())
            self.run_query(query, parametros)
            self.mensaje["text"]= "El turno ha sido eliminado correctamente"
        else:
            self.mensaje["text"]= "Por favor complete los campos correctamente"
     
     
         
        





        
if __name__ == "__main__":
    window = Tk()
    aplicacion = Turnos(window)
    window.mainloop()