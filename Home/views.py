from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def HomePage(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            save = form.save()
            messages.success(request, 'Your message has been sent .')
    else:
        form = ContactForm()
        # pass
    return render(request, 'home.html')
