"""
Ejercicio de Práctica:
Crear Clase Padre ->Vehiculo, con 2 class hijas (Coche y Bicicleta)
Clase Padre tiene que tener los siguientes atributos y métodos:

Vehiculo(clase padre):
-Atributos: color, ruedas
-métodos: __init__ y __str__

Coche (clase hija de Vehiculo) además de los atributos heredados 
-Atributos (heredados)+ velocidad (km/hr)
-métodos __init__ y __str__

Bicicleta (clase hija de Vehiculo)
-Atributos: heredados + tipo (urbana/montaña/etc)
-métodos: __init__ y __str__
"""

#comenzamos creando la clase Padre Vehiculo

class Vehiculo():
    def __init__(self, color, ruedas):
        self.color=color
        self.ruedas=ruedas
    
    def __str__(self):
        return 'Color es: '+ self.color + ', y tiene ' + str(self.ruedas) + ' ruedas.'

#creamos las clases hijas que llamaran a la clase padre
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas) #indica que los atributos color y ruedas vienen de la clase padre ya definidos
        self.velocidad=velocidad  #atributo propio
    
    def __str__(self):
        return super().__str__() + 'Velocidad (km/hr): ' + str(self.velocidad) 

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo=tipo

    def __str__(self):
        return super().__str__() + 'Tipo de Bici: ' +self.tipo

#Creamos un objeto de cada clase
  
vehiculo =Vehiculo('rojo',4)
print("\033[95m1.-LLamos a la clase Vehiculo y nos muestra su print con sus atributos\033[0m")
print(vehiculo)

coche=Coche('violeta',4, 250)
print("\033[95m2.-LLamos a la clase Coche (Hija de Vehiculo) y nos muestra su print con sus atributos + los heredados\033[0m")

print(coche)

bici=Bicicleta('blanca', 2, 'urbana')
print("\033[95m3.-LLamos a la clase Bicicleta (Hija de Vehiculo) y nos muestra su print con sus atributos + los heredados\033[0m")
print(bici)
