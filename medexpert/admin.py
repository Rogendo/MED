from django.contrib import admin
from . models import Emergency
from .models import Updates,Hospitals,FirstAid
# Register your models here.
admin.site.register([Updates, Hospitals,  FirstAid])

class Table(admin.ModelAdmin):
	class meta:
		model = Emergency
admin.site.register(Emergency ,Table)


