
import numpy
"""
Enunciado:
 * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
 * en dos dimensiones.
 * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
 *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
 * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
 * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarán en lograrlo.
 * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.  
"""

def punto_de_encuentro(cord_a, cord_b, speed_a, speed_b):
    #Se aplica y despeja la formula 'cord1 + speed1*x = cord2 + speed2*x'
    
    diferencia_cordenadas = (cord_b - cord_a)[0] if (cord_b - cord_a)[0] != 0 else (cord_b - cord_a)[1]
    diferencia_speed = (speed_a - speed_b)[0] if (speed_a - speed_b)[0] != 0 else (speed_a - speed_b)[1]

    if diferencia_cordenadas == 0 and diferencia_speed == 0:
        momento_de_encuentro = 0
    else:
        try:
            momento_de_encuentro = int(diferencia_cordenadas) / int(diferencia_speed)
        except:
            return "No se chocan"
        
    if momento_de_encuentro < 0:
        return "No se chocan"
    
    return f"Se encuentran al recorrer {momento_de_encuentro} unidades en las cordenadas {cord_b + speed_b * momento_de_encuentro}"

def pedir_datos():
    while True:
        try:
            p_1 = numpy.array((int(input("X1: ")), int(input("Y1: "))))
            speed_1 = numpy.array((int(input("Desplazamiento1 X: ")), int(input("Desplazamiento1 Y: "))))
            p_2 = numpy.array((int(input("X2: ")), int(input("Y2: "))))
            speed_2 = numpy.array((int(input("Desplazamiento2 X: ")), int(input("Desplazamiento2 Y: "))))
            break
        except:
            print("Error al introducir los datos") 
            

    return p_1, p_2, speed_1, speed_2




if __name__ == "__main__":
    p_1, p_2, speed_1, speed_2 = pedir_datos()

    solucion = punto_de_encuentro(p_1, p_2, speed_1, speed_2)
    print(solucion)

"""
Prueba

    p_1 = numpy.array((0,0))
    p_2 = numpy.array((1,1))

    speed_1 = numpy.array((1,1))
    speed_2 = numpy.array((1,1))
"""