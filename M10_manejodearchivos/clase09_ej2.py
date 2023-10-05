import sys
import os
import datetime

def informaciones(temp, humedad, lluvia):
    marcatiempo = datetime.datetime.now()
    marcatiempo = int(datetime.datetime.timestamp(marcatiempo))
    
    datos = str(marcatiempo) + ',' + temp + ',' + humedad + ',' + lluvia + '\n'

    with open('clase09_ej2.csv', 'a') as archivo_csv:
        archivo_csv.write(datos)

def main():
    if len(sys.argv) != 2:
        
        print('Se esperan 3 parámetros.')
        print('True (si) o False (no) para si llovio')
        return

    
    lluvia = sys.argv[1]
    temp = input ('temperatura en celsius?')
    humedad = input ('porcentaje de humedad?')

    informaciones(temp, humedad, lluvia)

if __name__ == "__main__":
    main()