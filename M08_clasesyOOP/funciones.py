class Funciones:
    def __init__(self, lista):
        self.lista=lista
    
    
    def es_primo(self):
        numeros = set(self.lista)
        for num in numeros:
            if (self.__primo(num)):
                print('primo:', num)
            else:
                
                print('no primo:', num)
        
    def __primo (self, num):
        if num > 0:
            for div in range (2, num):
                if num%div == 0:
                    return False
        else: 
            return False
        return  True  
    
    def repeticion(self):
        contador = {}
        
        for num in self.lista: #para cada elemento de la lista
            if num in contador: #si el pertenence al dicc
                contador[num] += 1 #el elemento se vuelve en clave y recibe un valor de +1
            else:
                contador[num] = 1 #sino el valor recibe 1
        veces = max(contador.values()) #funcion max retorna mayor valor
        moda = None #none = vacio
        for num, repeticiones in contador.items(): # clave, valor
            if repeticiones == veces: #verifica si el valor de cada clave es igual al valor encuentrado en la variable veces
                moda = num #moda recibe el valor clave
                break
        
        return moda, veces
    
    def conversion(self):
        medidas = ['°C', '°F', '°K']
        numeros = set(self.lista)
        for valor in numeros:
            for medida1 in medidas:
                for medida2 in medidas:
                    print ('conversion', medida1, "para", medida2)
                    self.__conversion(valor, medida1, medida2)
                    print()

    def __conversion(self, valor, medida1, medida2):
        if medida1 == '°C' and medida2 == '°F':
            valorfinal = valor * 9/5 + 32
            print (valor, medida1 , "es igual a ", valorfinal, medida2)
        elif medida1 == '°C' and medida2 == '°K':
            valorfinal = valor + 273.15 
            print(valor, medida1 , "es igual a ", valorfinal, medida2)
        elif medida1 == '°K' and medida2 == '°C':
            valorfinal = valor - 273.15
            print (valor, medida1 , "es igual a ", valorfinal, medida2)
        elif medida1 == '°F' and medida2 == '°C':
            valorfinal = (valor -32) * 5/9
            print (valor, medida1 , "es igual a ", valorfinal, medida2)
        elif medida1 == '°F' and medida2 == '°K':
            valorfinal = (valor -32) * 5/9 + 273.15
            print(valor, medida1 , "es igual a ", valorfinal, medida2)
        elif medida1 == '°K' and medida2 == '°F':
            valorfinal = (valor - 273.15) * 9/5 + 32
            print (valor, medida1 , "es igual a ", valorfinal, medida2)
        elif medida1 == medida2:
            valorfinal = valor
        
            print (valor, medida1, "---medida de origen y de destino iguales, no hay conversion")
        elif not isinstance (medida1, str):
            print ('medida de origen no reconocida')
        elif not isinstance(medida2, str):
            print ('medida destino no reconocida')
        return valorfinal
    
    def factorial(self):
        numeros = set(self.lista)
        for i in numeros:
            print ('factorial de ', i, 'es', self.__factorial(i))

    def __factorial(self, num):        
        
        if not isinstance(num, int):
            return 'debe ser inteiro'
        if num< 0:
            return 'debe ser positivo'   
        if num>1:
            num = num * self.__factorial(num -1)
           
        return num

