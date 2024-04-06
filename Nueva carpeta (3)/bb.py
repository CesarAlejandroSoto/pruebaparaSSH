class Plazadevicio:
    
    def __init__(self,nombre,precio,cantidad):
        
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
        
class Pangolo(Plazadevicio):
    def __init__(self, nombre, precio, cantidad,color_cuero):
        super().__init__(nombre, precio, cantidad)
        self.color_cuero=color_cuero
        
proveedordebareta=Plazadevicio("ñuridos",5000,10)
print(proveedordebareta.nombre)

vicioso= Pangolo("ñuridos",500,1,"blanco")
print(vicioso.nombre)
print(vicioso.cantidad)
print(vicioso.precio)