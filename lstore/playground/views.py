from django.shortcuts import render
from storeE.models import Product
from django.http import HttpResponse


def say_hello(request):
#pull data from Database
# tranform data
# send email   
   # return HttpResponse('Hello World')
   #query_set=Product.objects.all()
   ##query_set.filter().filter().orderby()
   #for product in query_set:
      #print(product)

   return render(request,'hello.html',{'name':'Humans'})
