from django.contrib import admin
from .models import Folder,Order,Comment,Message
# Register your models here.
admin.site.register(Folder),
admin.site.register(Order),
admin.site.register(Comment),
admin.site.register(Message),
