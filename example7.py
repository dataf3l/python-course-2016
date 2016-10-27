class Animal:
    z = 99
    pass
class Persona(Animal):
    x = "hola"
    y = 2
    z = 1
    def __init__(self, x=None, z=None):
        self.x = x
	if not(z is None):
            self.z = z
	
    def hablar(self):
        print(self.z)


a = Persona("guepa he", 92010)
a.hablar()
b = Persona()
b.hablar()
b.w = 1
print(b.w)
print(dir(b))
