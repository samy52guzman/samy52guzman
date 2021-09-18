from logging import root
from mysql.connector import connect
import time

data = connect(
    host="localhost",
    user="root",
    database="almacen"

)
mycursor = data.cursor()


def col_insertar():
    tipos = ["smallint", "VARCHAR", "int"]
    name_table = str(input("name of the table: "))
    name_column = str(input("The table should have at least one column, insert the name of the column: "))
    kind_column = int(
        input("Insert the kind of data you desire your column hold: \n 1 for words. \n 2 for numbers. \n answer: "))
    crear_tabla = f'CREATE TABLE {name_table}({name_column} {tipos[kind_column]}(50));'
    mycursor.execute(crear_tabla)


def borrar_table():
    name_table = str(input("name of the table you want to delete: "))
    erase_table = f'DROP TABLE {name_table};'
    mycursor.execute(erase_table)


def examinar():
    name = str(input("nombre de la tabla que desea examinar: "))
    mycursor.execute(f"SHOW COLUMNS FROM {name}; ")
    for x in mycursor:
        print(x[0])
        time.sleep(5)


# Añadir una colugna
def añadir_colugna():
    seguir = "si"
    while seguir == "si":
        seguir = str(input("Desea añadir una nueva colugna? "))
        if seguir == "si":
            tabla = str(input("Escriba el nombre de la tabla a la cual le desea añadir una colugna? "))
            tipo = str(input("Escriba: letra o numero. dependiendo de lo que quiera introducir ? "))
            if tipo in ("letra", "letras", "Letra", "Letras"):
                nombre_colugna = str(input("Digite el nombre de la colugna: "))

                mycursor.execute(f"ALTER TABLE {tabla} ADD COLUMN {nombre_colugna} VARCHAR(50) NOT NULL")
                header3 = []
                mycursor.execute(f"DESCRIBE {tabla}")
                for x in mycursor:
                    header3.append(x[0])
                print(header3)
            elif tipo in ("numeros", "numero", "Numeros", "Numero"):
                nombre_colugna = str(input("Digite el nombre de la colugna: "))
                mycursor.execute(f'ALTER TABLE {tabla} ADD COLUMN {nombre_colugna} smallint')
                header3 = []
                mycursor.execute(f"DESCRIBE {tabla}")
                for x in mycursor:
                    header3.append(x[0])
                print(header3)

        else:
            break


# Inormacion de cada colugna en un database
def informacion():
    elegir = str(input("desea saber que la informacion de una tabla? "))
    tabla = str(input("dinserte en nombre de la tabla: "))

    if elegir == "si":
        mycursor.execute(f"DESCRIBE {tabla}")
        for x in mycursor:
            print(x)
        elegir2 = str(input("desea saber que la informacion de las colugnas? "))
        if elegir2 == "si":
            mycursor.execute(f"SELECT * FROM {tabla}")
            for x in mycursor:
                print(x)
    elegir2 = str(input("desea saber que la informacion de las colugnas? "))
    if elegir2 == "si":
        mycursor.execute("SELECT * FROM alaska")
        for x in mycursor:
            print(x)
            nombres = x[0]
            print(nombres)
    else:
        return


# Elimina la colugna seleccionada.
def eliminar_colugna():
    deseo = str(input("Desea eliminar una colugna? (si o no): "))
    if deseo in ("si", "Si"):
        tabla = str(input("Inserte el nombre de la tabla a la cual le desea borrar una colugna: "))
        header = []
        mycursor.execute(f"DESCRIBE {tabla} ")
        for x in mycursor:
            header.append(x[0])
        print("Estos son los headers de las colugnas. ")
        print(header)
        eliminar = str(input("Cual desea eliminar: "))
        if eliminar in header:
            mycursor.execute(f'ALTER TABLE {tabla} DROP {eliminar}')
        else:
            print("Este nombre no existe, intente de nuevo.")
    elif deseo in ("no", "No"):
        print("adios")
        time.sleep(3)
    else:
        print("Mal escrito")
        time.sleep(3)


# cambiar el nombre del header de las colugnas.
def editar_header():
    deseo = str(input("Desea editar el header de una colugna: "))
    if deseo == "si":
        header = []
        nombre = str(input("Digite la tabla en donde esta la colugna que desea editar el header: "))
        mycursor.execute(f"DESCRIBE {nombre}")
        for x in mycursor:
            header.append(x[0])
        print(header)
        editar = str(input("Cual header desea editar: "))
        editado = str(input("Que  nuevo nombre le desea poner al header: "))
        if editar in header:
            mycursor.execute(f'ALTER TABLE {nombre} change {editar} {editado} VARCHAR(50)')
            header2 = []
            mycursor.execute(f"DESCRIBE {nombre}")
            for l in mycursor:
                header2.append(l[0])
            print(header2)
        else:
            print("el nombre que usted introdujo para editar no puede ser encontrado, por favor intente de nuevo.")


# para saber la cantidad de filas en una tabla.
def count_rows():
    desicion = str(input("desea saber cuantas filas hay? "))
    tabla = str(input("nombre de la tabla: "))
    if desicion == "si":
        mycursor.execute(f"SELECT COUNT(*) FROM {tabla}; ")
        for x in mycursor:
            print(x)
    time.sleep(5)


# ver todas las tablas en el database
def ver_tablas():
    tablas = []
    mycursor.execute(f"SHOW TABLES;")
    for x in mycursor:
        tablas.append(x)
    print(tablas)
    time.sleep(5)


def insertar_index():
    tablas = []
    header = []
    mycursor.execute(f"SHOW TABLES;")
    for x in mycursor:
        tablas.append(x)
    print(tablas)
    tabla = str(input("Seleccione la tabla correspondiente: "))
    mycursor.execute(f"DESCRIBE {tabla}")
    for x in mycursor:
        header.append(x[0])
    print(header)
    colugna = str(input("Seleccione la colugna correspondiente: "))
    valor = str(input("Inserte el valor que quiera introducir: "))

    mycursor.execute(f"CREATE INDEX {valor} ON {tabla}({colugna});")
    mycursor.execute(f"SHOW INDEX FROM almacen.{tabla};")
    for c in mycursor:
        print(c[2])
    time.sleep(5)
    return


def selecter():
    while True:
        desicion = int(input(
            "digite el numero de lo que desea hacer.\n1) agregar una tabla de datos. \n2) borrar una tabla de datos. \n"
            "3) ver las colugnas que hay. \n4) agregar colugna.\n5) informacion. \n6) eliminar colugna. \n7) editar nombre de colugna. \n"
            "8) contar filas.\n9) ver tablas en almacen. \n10) insertar index. \npara salir solo digite el cero (0),"
            "respuesta: "))
        if desicion == 1:
            col_insertar()
        elif desicion == 2:
            borrar_table()
        elif desicion == 3:
            examinar()
        elif desicion == 4:
            añadir_colugna()
        elif desicion == 5:
            informacion()
        elif desicion == 6:
            eliminar_colugna()
        elif desicion == 7:
            editar_header()
        elif desicion == 8:
            count_rows()
        elif desicion == 9:
            ver_tablas()
        elif desicion == 10:
            insertar_index()
        elif desicion == 0:
            break
        else:
            print("intente de nuevo.")


selecter()
"""------------------------------------------------------------------------------------------"""

# para crear un database
# cursor.execute("CREATE DATABASE python")

# para crear una tabla
"""cursor.execute("CREATE TABLE persona (nombre VARCHAR(50), edad smallint UNSIGNED,personID int PRIMARY KEY AUTO_INCREMENT)")"""
# cursor.execute("INSERT INTO persona (nombre, edad) VALUES (%s,%s)", ("Samuel", 27))
# db.commit()

# añadir una colugna
# cursor.execute("ALTER TABLE persona ADD COLUMN genero VARCHAR(10) NOT NULL")

# para saber que esta en la tabla
# cursor.execute("DESCRIBE persona")

# Para saber lo que esta adentro del header de la tabla
# cursor.execute("SELECT * FROM persona")

# PARA BORRAR COLUGNAS
# cursor.execute("ALTER TABLE persona DROP genero")

# para cambiar el nombre del header de una colugna y tambien se pueden cambiar propiedades
# cursor.execute(f'ALTER TABLE persona change {editar} {editado} VARCHAR(50)')

# PARA AñADIR VARIAS INFORMACIONES A LA VEZ EN UNA TABLA
# cursor.execute("INSERT INTO Users(name, passwd) VALUES(%s,%s)", users)


Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"

Q2 = "CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"
Q3 = "INSERT INTO Users(name, passwd) VALUES (%s,%s)"
Q4 = "INSERT INTO scores (userId, game1, game2) VALUES (%s, %s, %s)"
