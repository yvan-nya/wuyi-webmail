from unicodedata import name
from venv import create
from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import Clientform
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
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
    if 'q' in request.GET:
        q = request.GET['q']
        all_client_list = Client.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) |
            Q(email__icontains=q) | Q(subject__icontains=q) |
            Q(status__icontains=q) | Q(message__icontains=q)
        ).order_by('-create_at')
    else:
        all_client_list = Client.objects.all().order_by('-create_at')
    paginator = Paginator(all_client_list, 10)
    page = request.GET.get('page')
    all_client = paginator.get_page(page)
    #=============================== MESSAGES COUNTER =========================================#
    # Total
    total = Client.objects.all().count()
    # Read
    read = Client.objects.filter(status='Read')
    # Unread
    pending = Client.objects.filter(status='Pending')
    # Today
    base = datetime.now().date()
    today = Client.objects.filter(create_at__gt = base)
    return render(request, 'inbox.html', {'clients':all_client, 
    "total":total, "read":read, "pending":pending, "today":today})

# Fonction to delete the messages
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_message(request, client_id):
    client = Client.objects.get(id = client_id)
    client.delete()
    messages.success(request, "Messages successfully deleted !")
    return HttpResponseRedirect('/inbox/')

# Fonction to view the message individually
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def client(request, client_id):
    client = Client.objects.get(id = client_id)
    if client != None:
        return render(request, "client.html",{"client":client})

#Function to mark the message as read
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def mark_message(request):
    if request.method =="POST":
        client = Client.objects.get(id =request.POST.get('id'))
        if client != None:
            client.status = request.POST.get('status')
            client.save()
            messages.success(request, "Messages marked as READ !")
            return HttpResponseRedirect('/inbox/')