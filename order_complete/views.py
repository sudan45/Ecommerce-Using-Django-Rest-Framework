from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from checkout.forms import CheckoutForm
import requests

# Create your views here.
def order_complete(request):
   if request.method == 'POST': 
      form = CheckoutForm(request.POST)
      if form.is_valid():
         response = requests.post('http://localhost:8000/api/v1/checkout/', request.POST)
         print('response', response.text)
         if response.status_code != 200:
            return HttpResponse("Your order could not be submitted. Please try again.")  
   template = loader.get_template('order_complete.html')
   return HttpResponse(template.render({"active_tab":"order_complete","request":request}))






        