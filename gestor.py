from io import open
import pickle
class Personaje():
    def __init__(self,nombre,vida,ataque,defensa,alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
    def __str__(self):
        return '{} => Vida: {} Ataque: {} Defensa: {} Alcance: {}'.format(self.nombre,self.vida,self.ataque,self.defensa,self.alcance)
    
class Gestor():
    personajes =[]

    def __init__(self):
        self.cargar()
    def agregar(self,p):
        self.personajes.append(p)
        self.guardar()
    def borrar(self,nombre):
        for personaje in self.personajes:
            if personaje.nombre == nombre:
                self.personajes.remove(personaje)
                self.guardar()
                return 
            print('{} ha sido eliminado'.format(nombre))
    def mostrar(self):
        if len(self.personajes) == 0:
            print('Fichero vacio')
            return
        for p in self.personajes:
            print(p)
    def cargar(self):
        fichero = open('personajes.pckl','ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            print('Fichero vacio')
        finally:
            fichero.close()
    def guardar(self):
        fichero = open('personajes.pckl','wb')
        pickle.dump(self.personajes,fichero)
        fichero.close()

