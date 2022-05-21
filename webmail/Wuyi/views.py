from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import Clientform
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
#===================================================================================================================================#

#=============================== FRONTEND =========================================#
def home(request):
    return render(request, 'home.html')


def send_message(request):
    if request.method == "POST":
        form = Clientform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully !")
        return HttpResponseRedirect('/')
    else:
        form = Clientform()
    return render(request, 'home.html', {'form':form})


#=============================== BACKEND =========================================#
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def inbox(request):
    return render(request, 'inbox.html')


