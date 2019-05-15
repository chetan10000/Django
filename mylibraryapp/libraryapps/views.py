from .forms import BookForm
from .serializer import BookSerializer  
from django.shortcuts import render
from .models import Author, Book , Language , Genre
from .serializer import BookSerializer
from django.db.models import Q
from django.shortcuts import redirect


# Books view #
def Home(request):
    products=Book.objects.all()
    serializer=BookSerializer(products,many=True)
    context={'Books':serializer.data}
    template='home1.html'
    return render(request,template,context)

#Search view #
def search(request):
    try:
        q=request.GET.get('q')
    except:
        q=None
    if q:
        for name in q.split():
            products=Book.objects.filter(Q(author__first_name__icontains=name)|Q(author__last_name__icontains=name)|Q(genre__name__icontains=q))
            if products.count()==0:
                template = 'error.html'
                context = {}
                return render(request,template,context)

            serializer=BookSerializer(products,many=True)
            context={'Books':serializer.data}
            template='result.html'
           

    else:
        template = 'home1.html'
        context = {}

    return render(request,template,context)


# create new book object #
def create(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'forms.html', {
        'form': form
    })

# detail of book object #
def detail(request, id):
    products=Book.objects.get(pk=id)
    serializer=BookSerializer(products,many=False)
    context={'Books':serializer.data,'pk':products.id}
    template='detail.html'
    return render(request,template,context)

# remove book object #

def remove(request , id):
    book = Book.objects.get(pk=id)
    book.delete()
    context={}
    return redirect('books')

# edit book object #
def Edit(request, id=None):
    instance = Book.objects.get(pk=id)
    form = BookForm(request.POST ,request.FILES ,instance=instance)
    if form.is_valid():
        instance =form.save(commit = False)
        instance.save()
        return redirect('books')
    context ={

        "instance":instance,
        "form":form
    
        }
    return render(request,'forms.html',context)
    




