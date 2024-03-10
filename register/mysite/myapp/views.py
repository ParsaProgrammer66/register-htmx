from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST,request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            user=User.objects.create_user(cd['username'],cd['password'])
            user.save()
    else:
        form=SignupForm()
    return render(request,'myapp/signup.html',{'form':form})

def check_username(request):
    username=request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div style='color:red'>This username already exists</div>")
    else:
        return HttpResponse("<div style='color:green'>This username is avaylable</div>")