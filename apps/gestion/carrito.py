

class carrito:

    def __init__(self , request) :
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')

        if not carrito:
            self.session['carrito'] = {}
            self.carrito = self.session['carrito']
        else:
            self.carrito = carrito

    def agregar(self , producto):
        id = producto.id

        if  id not in self.carrito.keys():

            self.carrito[id]={
                'producto': producto.nombre ,
                'precio': producto.precio ,
                'cantidad': 1 ,
                'imagen': producto.imagen,
                'cantidad':1
            }       
        else:
            self.carrito[id]['cantidad'] += 1


        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True