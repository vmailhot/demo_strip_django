from django.shortcuts import render, redirect
import stripe

# Create your views here.


def create_checkout_session(request):
    stripe.api_key =''
    session = stripe.checkout.Session.create(
        line_items=[{
        'price_data': {
            'currency': 'usd',
            'product_data': {
            'name': 'T-shirt',
            },
            'unit_amount': 2000,
        },
        'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000',
        cancel_url='http://localhost:8000',
    )

    return redirect(session.url, code=303)

def home(request):
  return render(request, 'home.html')
