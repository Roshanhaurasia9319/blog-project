from django.shortcuts import render,redirect
from django.contrib import messages 
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid(): #check is the username is valid or not
            form.save() # saves the user information
            username=form.cleaned_data.get('username')
            messages.success(request,'Acount created Successfully!!!!')
            return redirect('index')
    else:
        form=UserRegisterForm()    
    return render(request,'users/register.html',{'form':form})    
   
