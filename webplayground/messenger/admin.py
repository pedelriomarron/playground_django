from django.contrib import admin
from .models import Message,Thread

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    pass

class ThreadAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)
admin.site.register(Thread, ThreadAdmin)
