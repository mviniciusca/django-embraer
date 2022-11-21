from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def courseindex(request):
    return render(request, 'course/index.html')

def coursecreate(request):
    if request.method == 'GET':
        form = UserForm()
        context = {
            'form': form,
        }
        return render(request, 'course/create.html', context=context)
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'course/index.html')


