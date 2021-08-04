# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mainsite import forms, models
from django.shortcuts import render,redirect

# Create your views here.

def indexView(request):
    form = forms.ContactUsForm
    bout = models.about_me.objects.get(pk=2)

    if request.method == 'POST':
        print(request.POST)
        contact = forms.ContactUsForm(request.POST)
        if contact.is_valid():
            contact.save()
            return redirect('thankyou')

    context = {'hire_me': form, 'about':bout}
    return render(request, 'index.html', context)


def thankyouView(requests):
    return render(requests, 'thankyou.html')
