from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto zostało założone dla użytkownika {username}!')
            return redirect('register') # trzeba zmienić na stronę główną portalu!!!
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

