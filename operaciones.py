def suma(x,y):
    return int(x)+int(y)
def resta(x,y):
    return int(x)-int(y)
def producto(x,y):
    return int(x)*int(y)
def division(x,y):
    return int(x)/int(y)

def error_type(x,y):
    try:
        x,y = int(x),int(y)
        return True
    except TypeError:
        return "Error: Tipo de dato no válido"

def error_zero(x,y):
    try:
        division
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero"