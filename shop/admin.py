from django.contrib import admin
from .models import Category,Product
# Register your models here.
#@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name','slug']
  prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category,CategoryAdmin)

#@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['name','price','stock','available','created','updated']
  list_editable = ['price','stock','available']
  prepopulated_fields = {'slug':('name',)}
  list_per_page = 20
admin.site.register(Product,ProductAdmin)

