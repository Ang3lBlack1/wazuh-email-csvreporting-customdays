import os
import re
from datetime import datetime, timedelta

# Solicitar al usuario las fechas de inicio y fin
fecha_inicio = input("Ingrese la fecha de inicio en formato YYYY-MM-DD: ")
fecha_fin = input("Ingrese la fecha de fin en formato YYYY-MM-DD: ")
#fecha_inicio = '2024-02-01'
#fecha_fin = '2024-02-29'

# Convertir las fechas ingresadas a objetos datetime
#fecha_limpia = re.sub(r'[^\x00-\x7F]+', '', fecha_inicio)
fecha_inicio_obj = datetime.strptime(fecha_inicio, "%Y-%m-%d")
fecha_fin_obj = datetime.strptime(fecha_fin, "%Y-%m-%d")

# Crear un diccionario de fechas con la fecha de inicio y la fecha siguiente
fechas = {}
while fecha_inicio_obj <= fecha_fin_obj:
    fecha_siguiente = fecha_inicio_obj + timedelta(days=1)
    fechas[f"{fecha_inicio_obj.strftime('%Y-%m-%d')}T06:00:00.000Z"] = f"{fecha_siguiente.strftime('%Y-%m-%d')}T05:59:59.999Z"
    fecha_inicio_obj = fecha_siguiente

# Ejecutar el script para cada par de fechas
for clave, valor in fechas.items():
    os.system(f'bash run_csvreporting_customdays.sh reports.yml "{clave}" "{valor}"')
    print(f'bash run_csvreporting_customdays.sh reports.yml "{clave}" "{valor}"')
