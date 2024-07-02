import os

registro = []
especies = []

menu = '''
1. Registrar mascota
2. Listar todas las mascotas
3. Imprimir ficha de registro
4. Salir
'''

titulo = f'''{"Listado de mascotas"}
{"="*110}
{"Especie":<15}{"Nombre":<20}{"Peso":<10}{"Costo de consulta":<25}{"Impuesto":<15}{"Costo total":<20}
{"="*110}
'''

def registroM():
        while True:
            try:
                os.system("cls")
                esp = input("Especie: ")
                nom = input("Nombre: ")
                kg = int(input("Peso: "))
                presio = int(input("Costo de consulta: "))
                imp = presio * 0.05
                total = presio + imp
                registro.append([esp,nom,kg,presio,imp,total])
                if esp not in especies:
                    especies.append(esp)
                    break
                else:
                    input("Mascota registrada con exito")
                    break
            except Exception as ex:
                 print("Error: ", ex)

def listar():
    salida = titulo
    for i in registro:
        salida+=f"{i[0]:<15}"
        salida+=f"{i[1]:<20}"
        salida+=f"{i[2]:<10}"
        salida+=f"{i[3]:<25}"
        salida+=f"{i[4]:<15}"
        salida+=f"{i[5]:<20}"
        salida+=f"\n"
    return salida

def listarxEspecie(especie):
    salida = titulo
    for i in registro:
        if i[0]==especie:
            salida+=f"{i[0]:<15}"
            salida+=f"{i[1]:<20}"
            salida+=f"{i[2]:<10}"
            salida+=f"{i[3]:<25}"
            salida+=f"{i[4]:<15}"
            salida+=f"{i[5]:<20}"
            salida+=f"\n"
        return salida
        
def imprimir():
    try:
        opc2=input("Impresion de registro\n1. Imprimir todo\n2. Filtrar por especie\n")
        if opc2 == "1":
            with open("registro.txt","w") as file:
                file.write(listar())
        elif opc2 == "2":
            especie = input("Especie: ")
            for i in range(len(registro)):
                    if especie == registro[i][0]:
                        with open("registrofiltrado.txt","w") as file:
                            file.write(listarxEspecie(especie))
                    else:
                        print("Especie no encontrada")
    except Exception as ex:
        print("Error: ", ex)

    

while True:
     try:
        os.system("cls")
        print(menu)
        opc = input("Ingrese opcion: ")
        if opc == "4":
            break
        elif opc == "1":
            registroM()
        elif opc == "2":
            print(listar())
            input()
        elif opc == "3":
            imprimir()
     except Exception as ex:
        print("Error: ", ex)
   
