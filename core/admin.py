from django.contrib import admin
from core.models import Contact
from core.models import Product,Orders,OrderUpdate


# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
