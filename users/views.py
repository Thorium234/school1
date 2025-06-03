from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm





def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile_user')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('login')
    

