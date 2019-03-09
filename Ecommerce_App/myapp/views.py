from django.shortcuts import render
from.models import Products,ProductsImage

# Create your views here.
def Home(request):
    products=Products.objects.all()
    context={'items':products}
    template='home.html'
    return render(request,template,context)

def all(request):
    products=Products.objects.all()
    context={'items':products}
    template='all.html'
    return render(request,template,context)


def search(request):
   
    try:
        q=request.GET.get('q')
    except:
        q=None
    if q:
        products=Products.objects.filter(title=q)
        context={'query':q,'products':products}
        template='result.html'
      
    else:
        template='home.html'
        context={}
    return render(request,template,context)

   