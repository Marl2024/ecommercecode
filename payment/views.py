from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ShippingForm, BillingForm
from .models import Order, ShippingAddress, OrderItem
from cart.cart import Cart
from product.models import Product


from django.contrib import messages
from django.shortcuts import redirect




def process_order(request):
    if request.method == 'POST':
        cart = Cart(request)
        cart_products = cart.get_prods()  # List of products in the cart
        quantities = cart.get_quants()     # Dictionary with product ids as keys and quantities as values
        totals = cart.cart_total()          # Total price of items in the cart



        billing_full_name = request.POST.get('billing_full_name')
        billing_email = request.POST.get('billing_email')
        billing_address = request.POST.get('billing_address')

        # Get the ShippingAddress instance based on the ID passed from the form
        order = Order.objects.get(id=request.POST.get('billing_address_id'))

        # Create the Order instance
        order = Order.objects.create(
            full_name=billing_full_name,
            email=billing_email,
            billing_address=billing_address,
            amount_paid=totals,
           
        )
      
       
        for product in cart_products:
            product_id = product.id
            quantity = quantities(product_id, 1)


            price = product.sale_price if product.is_sale else product.price 
        for key, valaue in quantities().items():
           

                #value 


        

            # Create the OrderItem instance
            order_item = OrderItem(
                order=order, # Associate the Order instance
                product=product,  # Use product instance
                quantity=quantity,
                price=price,
            )


            order_item.save()


        #delete the cart
        for key in list(request.session.keys()):
            if key == 'session_key':
                del request.session[key]
                

        request.session.pop("session_key", None)
        

        messages.success(request, 'Order placed successfully!')
        return redirect('home')

    messages.error(request, 'Invalid request method. Please try again.')
    return redirect('checkout')



        


def success(request):
    context = {'message': 'Registration successful!'}
    return render(request, 'success.html', context)




def success(request):
    context = {'message': 'Registration successful!'}
    return render(request, 'success.html', context)





def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()

    if request.method == 'POST':
        shipping_form = ShippingForm(request.POST)
        billing_form = BillingForm(request.POST)


        if shipping_form.is_valid():
            # Get the shipping data from the form
            shipping_full_name = shipping_form.cleaned_data['shipping_full_name']
            shipping_email = shipping_form.cleaned_data['shipping_email']
            shipping_address = shipping_form.cleaned_data['shipping_address']
            shipping_city = shipping_form.cleaned_data['shipping_city']
            shipping_state = shipping_form.cleaned_data['shipping_state']
            shipping_zipcode = shipping_form.cleaned_data['shipping_zipcode']
            shipping_country = shipping_form.cleaned_data['shipping_country']
            


            # Save the ShippingAddress
            shipping_address = ShippingAddress.objects.create(
                shipping_full_name=shipping_full_name,
                shipping_email=shipping_email,
                shipping_address=shipping_address,
                shipping_city =shipping_city ,
                shipping_state=shipping_state,
                shipping_zipcode=shipping_zipcode,
                shipping_country=shipping_country,
            )

            shipping_form = ShippingForm()  


        if billing_form.is_valid():    

            # Get the Billing data from the form
            full_name=billing_form.cleaned_data['billing_full_name']
            email=billing_form.cleaned_data['billing_email']
            billing_address=billing_form.cleaned_data['billing_address']
            amount_paid=totals

            

            order= Order.objects.create(

            
                full_name=full_name,
                email=email,
                billing_address=billing_address,
                amount_paid=amount_paid,

            )




         # Create OrderItems
            for product in cart_products:
                product_id = product.id
                quantity = quantities.get(product_id, 0)  # Safely get quantity
                if quantity > 0:  # Only create order items if quantity is valid
                    price = product.sale_price if product.is_sale else product.price

                    # Create the OrderItem instance
                    order_item = OrderItem(
                        order=order,  # Associate the Order instance
                        product=product,  # Use product instance
                        quantity=quantity,
                        price=price,
                    )
                    order_item.save()



            


   
            return redirect('success')  # Redirect to a success page
    

    else:
        shipping_form = ShippingForm()
        billing_form=BillingForm()

    return render(request, 'payment/checkout.html', {
        "cart_products": cart_products,
        "quantities": quantities,
        "totals": totals,
        'shipping_form': shipping_form,
        'billing_form':billing_form,


    })