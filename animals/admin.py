from django.contrib import admin
from .models import Animal, CareInstructions
# Register your models here.


admin.site.register(Animal)
admin.site.register(CareInstructions)