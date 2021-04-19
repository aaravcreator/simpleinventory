from django.contrib import admin
from .models import Product,ProductCategory,ProductType,Customer,Vendor,PurchaseFromVendor,Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'type','weight','jarti', 'getprice','getvendor')
    list_filter = ('category',)

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'mobile_no', 'email')

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductType)
admin.site.register(Customer)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(PurchaseFromVendor)
admin.site.register(Order)


# Register your models here.
