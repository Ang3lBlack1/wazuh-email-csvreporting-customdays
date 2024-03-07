#!/bin/bash
#DIA=`date +"%d/%m/%Y"`
#HORA=`date +"%H:%M"`

#APP_DIR=$(dirname $0)
#source ${APP_DIR}/venv/bin/activate
#python3 ${APP_DIR}/app_csvreporting.py $1 >> ${APP_DIR}/csvreporting.log
#deactivate
APP_DIR=$(dirname "$0")
source "${APP_DIR}/venv/bin/activate"

# Obtiene la fecha y hora actual en el formato deseado
current_date=$(date +"%Y-%m-%d %T")

# Ejecuta el script de Python y redirige la salida al archivo csvreporting.log con la fecha y hora
python3 "${APP_DIR}/app_csvreporting.py" "$1" "$2" "$3" | while IFS= read -r line; do
    echo "[$current_date] $line" >> "${APP_DIR}/csvreporting.log"
done

deactivate
