# -*- coding: utf-8  -*-
# © Kan IT AB
# Written by Tobias Alm
from django.shortcuts import render, redirect

import logging
from accounts.forms import CustomUserCreationForm
from common.const import CONST_LOG_NAME

log = logging.getLogger(CONST_LOG_NAME)


def sign_up(request):
    context = {}
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('embu:start')
    else:
        form = CustomUserCreationForm()
        context['form'] = form
    return render(request,
                  'registration/signup.html',
                  context=context)
