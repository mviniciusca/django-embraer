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
            context = {
                'name' : form.cleaned_data['name'],
                'telephone' : form.cleaned_data['telephone'],
                'email' : form.cleaned_data['email']
            }
        return render(request, 'course/index.html', context=context)

def courseedit(request, user_id):
    context = {
        'id' : user_id
    }
    return render(request, 'course/index.html', context=context)

