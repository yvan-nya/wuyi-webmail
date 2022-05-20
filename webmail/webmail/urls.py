from django.contrib import admin
from django.urls import path, include
from Wuyi import views

urlpatterns = [
    # Path to admin page
    path('admin/', admin.site.urls, name='admin'),
    # Path to home page (Frontend)
    path('', views.home, name = "home"),
    # Path to inbox page (Backend)
    path('inbox/', views.inbox, name = "inbox"),
    # Path to login/logout
    path('login/', include('django.contrib.auth.urls')),
]
