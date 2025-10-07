El programa debe verificar si la longitud de una pista disponible es suficiente para el despegue de un avion, considerando la masa, un ajuste por temperatura y una penalizacion operativa que reduce la pista efectiva.

# 1 Diccionario de constantes
constantes = {
    "K": 15,     
    "a": 0.01     
}
# Se imprime el diccionario para que se vean las constantes 


# 2 Diccionario vacío para los datos de entrada
entrada = {}
# Se agregan los elementos al diccionario 
entrada["masa"] = float(input("Masa de la aeronave (ton): "))
entrada["l_disp"] = float(input("Longitud disponible de pista (m): "))
entrada["deltaT"] = float(input("Exceso de temperatura (°C): "))
entrada["penal"] = float(input("Penalización operativa (m): "))
# Se imprime el diccionario con los nuevos datos agregados 

# 3 Diccionario vacio para resultados de las ecuacionesk
salida = {}
# Ecuaciones agregsndo resultados a el diccipnario salida
salida["lreq_base"] = constantes["K"] * entrada["masa"]
salida["lreq_aj"] = salida["lreq_base"] * (1 + constantes["a"] * entrada["deltaT"])
salida["leff"] = entrada["l_disp"] - entrada["penal"]

# Condicional que compara la longitud efectiva disponible de la pista con la longitud ajustada requerida para el despegue utilizando el diccionario de salida, y imprimiendo mensaje
if salida["leff"] >= salida["lreq_aj"]:
    salida["mensaje"] = "La pista es suficiente para el despegue"
else:
    salida["mensaje"] = "La pista NO es suficiente para el despegue"

# Lista con los valores sacados del diccionario salida 
lista_resultados = [salida["lreq_base"], salida["lreq_aj"], salida["leff"],salida["mensaje"]]
# Lista con los nombres correspondientes a cada valor
nombres = ["Longitud base requerida", "Longitud ajustada requerida", "Longitud efectiva disponible", "Resultado final"]

# for para imprimir una lista con los nombres y valores ordenados 
for nombre, valor in zip(nombres, lista_resultados):
    print(f"-{nombre}: {valor:} m")
