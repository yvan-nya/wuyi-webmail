from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('id','name','phone','email','subject','message','file')
    list_display = ['name','email','subject','create_at','situation']
    search_fields = ['name','email','subject']
    list_filter = ['status']
    list_per_page: 10

admin.site.register(Client, ClientAdmin)