# 2 Diccionario vacío para los datos de entrada
entrada = {}
# Diccionario vacio para resultados de las ecuacionesk
salida = {}
# 1 Diccionario de constantes
constantes={}
nombres=[]
lista_resultados=[]
control = True
while control == True:
    print( "\n1.Verificacion de pista\n2.Listado de elementos\n3.Salir.")
    opcion=int(input("ingrese una opcion: "))
    match opcion: 
        case 1: 
            print("\nVERIFICACIÓN DE LONGITUD DE PISTA")

            # 1 Diccionario de constantes
            constantes = {
                "K": 15,      # m/ton (factor base)
                "a": 0.01     # 1% por °C
            }

            print("\nConstantes:", constantes)

            


            print("\nIngreso de datos ")
            entrada["masa"] = float(input("Masa de la aeronave (ton): "))
            entrada["l_disp"] = float(input("Longitud disponible de pista (m): "))
            entrada["deltaT"] = float(input("Exceso de temperatura (°C): "))
            entrada["penal"] = float(input("Penalización operativa (m): "))

            print("Diccionario de datos", entrada)

            
            

            # Ecuaciones agregsndo resultados a el diccipnario salida
            salida["lreq_base"] = constantes["K"] * entrada["masa"]
            salida["lreq_aj"] = salida["lreq_base"] * (1 + constantes["a"] * entrada["deltaT"])
            salida["leff"] = entrada["l_disp"] - entrada["penal"]

            # Condición de control
            if salida["leff"] >= salida["lreq_aj"]:
                salida["mensaje"] = "La pista es suficiente para el despegue"
            else:
                salida["mensaje"] = "La pista NO es suficiente para el despegue"


            # Lista con los valores
            lista_resultados = [salida["lreq_base"], salida["lreq_aj"], salida["leff"],salida["mensaje"]]
            # Lista con los nombres
            nombres = ["Longitud base requerida", "Longitud ajustada requerida", "Longitud efectiva disponible", "Resultado final"]

            print("\nResultados en lista:")
            for nombre, valor in zip(nombres, lista_resultados):
                print(f"-{nombre}: {valor:} m")
        case 2: 
            if not entrada:
                print("\nEl diccionario esta vacio")
            else:
                print("\nDatos de entrada en lista:")
                for clave, valor in entrada.items():
                    print(f"-{clave}: {valor}")

            print("\nConstantes en lista:")
            for clave, valor in constantes.items():
                print(f"-{clave} = {valor}")

            print("\nResultados en lista:")
            for nombre, valor in zip(nombres, lista_resultados):
                print(f"-{nombre}: {valor:} m")

        case 3: 
            control = False
        case _:
            print("opcion invalida")