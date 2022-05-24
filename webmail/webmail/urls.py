from django.contrib import admin
from django.urls import path, include
from Wuyi import views
from webmail import settings
from django.conf.urls.static import static

urlpatterns = [
    # Path to admin page
    path('admin/', admin.site.urls, name='admin'),
    # Path to home page (Frontend)
    path('', views.home, name = "home"),
    path('login/', include('django.contrib.auth.urls')),
    # Path to send a message
    path('send_message/', views.send_message, name = "send_message"),
    # Path to inbox page (Backend)
    
    path('inbox/', views.inbox, name = "inbox"),
    # Path to login/logout
    path('delete_message/<str:client_id>', views.delete_message, name="delete_message")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
