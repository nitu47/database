
from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display =('id','name')
    search_fields=('name',)
    list_filter=('name',)
# admin.site.register(Category,CategoryAdmin)\
    
@admin.register(Food)

class FoodAdmin(admin.ModelAdmin):
    list_display =('id','name','price','category')
    search_fields=('name','category__name')
    list_filter=('name','price')
    list_per_page=10
# admin.site.register(Food)


@admin.register(Table)

class TableAdmin(admin.ModelAdmin):
    list_display =('id','number','status')
    search_fields=('status',)
    list_filter=('status',)
    list_per_page=10
# admin.site.register(Table)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra=0
    autocomplete_fields=('food',)

@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display =('id','User','total_price','status','payment_status')
    search_fields=('User__username',)
    list_filter=('status','payment_status')
    list_editable=('status','payment_status')
    inlines=[OrderItemInline]
# admin.site.register(Order)




#@admin.register(OrderItem)

#class OrderItemAdmin(admin.ModelAdmin):
 #   list_display =('id','order','food')


# admin.site.register(OrderItem)
