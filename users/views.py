from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm


def register(request):
    """
    Note about messages:
        - message.debug
        - message.info
        - message.success
        - message.warning
        - message.error
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account crated for {username}!')
            return redirect('rental-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
