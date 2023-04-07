from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Your message successfully sent")
        return redirect('contact:index')
    ctx = {
        "form": form
    }
    return render(request, 'wordify/contact.html', ctx)
