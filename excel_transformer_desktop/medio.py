import pandas as pd
import json
import sys

# Solicitar URL del archivo Excel
url_excel = input("Introduce la URL del archivo Excel: ")

# Leer archivo Excel
try:
    df = pd.read_excel(url_excel)
except:
    print("Error al leer el archivo Excel.")
    sys.exit()

# Solicitar ruta del archivo de reglas
ruta_reglas = input("Introduce la ruta del archivo de reglas JSON: ")

# Leer archivo de reglas
try:
    with open(ruta_reglas) as f:
        reglas = json.load(f)
except:
    print("Error al leer el archivo de reglas JSON.")
    sys.exit()

# Función para aplicar las reglas a valor
def aplicar_reglas(valor, tipo, tamano):
    if pd.isna(valor):
        return ''
    if tipo == 'NUMERICO':
        valor = str(int(valor)).zfill(tamano)
    elif tipo == 'ALFANUMERICO':
        valor = str(valor)[:tamano].ljust(tamano, '$')
    return valor

# Aplicar reglas a cada columna
for regla in reglas:
    nombre = regla['nombre']
    tipo = regla['tipo']
    tamano = regla['TAMANO']
    df[nombre] = df[nombre].apply(lambda x: aplicar_reglas(x, tipo, tamano))

# Solicitar ruta del archivo de salida
ruta_salida = input("Introduce la ruta donde se guardará el archivo de salida: ")

# Guardar archivo de salida
try:
    with open(ruta_salida, 'w') as f:
        for index, row in df.iterrows():
            anio = str(row['ANIO']).zfill(4)
            concepto = str(row['CONCEPTO'])[:10].ljust(10, '$')
            valor = str(int(row['VALOR'])).zfill(20)
            f.write(f"{anio}{concepto}{valor}\n")
except:
    print("Error al guardar el archivo de salida.")
    sys.exit()

print("Archivo de salida guardado correctamente.")
