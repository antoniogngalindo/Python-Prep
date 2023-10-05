import sys

def main():
    if len(sys.argv) !=4:
        print ('se espera 4 parametros')
        return
    else:
        param1 = sys.argv[1]
        param2 = sys.argv[2]
        param3 = sys.argv[3]
        print (f'el parametro 0 es {sys.argv[0]}')
        print (f'parametro 1 es {param1}, parametro 2 es {param2} y parametro 3 es {param3}')
        return

if __name__ == "__main__":
    main()

    #comandos:
    #cd M10_manejodearchivos
    #py clase09_ej1.py hola oi hey
    
    #imprimido:
    #el parametro 0 es clase09_ej1.py
    #parametro 1 es hola, parametro 2 es oi y parametro 3 es hey