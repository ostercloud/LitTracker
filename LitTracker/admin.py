from django.contrib import admin
from LitTracker.models import *

class BaseItemAdmin(admin.ModelAdmin):
    fields = ('item', 'code')
    list_display = ('item', 'code')
    list_filter = ('item', 'code')


class BasePublisherAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)


class BaseInStockAdmin(admin.ModelAdmin):
    fields = ('item', 'publisher')
    list_display = ('item', 'publisher')
    list_filter = ('item', 'publisher')


class BaseOrderAdmin(admin.ModelAdmin):
    fields = ('item', 'ordered_by', 'order_date', 'received_date')
    list_display = ('item', 'ordered_by', 'order_date', 'received_date')
    list_filter = ('item', 'ordered_by', 'order_date', 'received_date')


admin.site.register(Item, BaseItemAdmin)
admin.site.register(Publisher, BasePublisherAdmin)
admin.site.register(InStock, BaseInStockAdmin)
admin.site.register(Order, BaseOrderAdmin)

