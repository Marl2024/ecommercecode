from product.models import Product
from django.http import JsonResponse

class Cart():
    def __init__(self, request):
        self.session = request.session

        #to get session
        cart = self.session.get('session_key')
        
        #create session
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # make it available to all pages
        self.cart = cart


    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
           # self.cart[product_id] = {'price': str (product.price)}
           self.cart[product_id] = int(product_qty)

        self.session.modified= True
    
    def cart_total(self):
        #get product ids
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in = product_ids)
        quantities = self.cart
        
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total 


    def __len__(self):
        return len(self.cart)


    def get_prods(self):
        #get ids from cart
        product_ids= self.cart.keys()
        #Use ids to database
        products = Product.objects.filter(id__in=product_ids)
        
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        ourcart = self.cart
        #update dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)
        #delete form the cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True