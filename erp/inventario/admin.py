from django.contrib import admin
from inventario.models import Carro

# Register your models here.
class InventarioAdmin(admin.ModelAdmin):
    list_display = ["marca", "cantidad", "pais"]
    list_search = ["marca"]

admin.site.register(Carro, InventarioAdmin)