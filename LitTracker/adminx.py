import xadmin
from xadmin import views
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from models import *


class MainDashboard(object):
    widgets = [
        [
            {"type": "qbutton", "title": "Quick Start", "btns":
                [
                    {'title': "Google", 'url': "http://www.google.com"}
                ]},
        ],
        [
            {"type": "addform", "model": Order}
        ]
    ]

xadmin.site.register(views.website.IndexView, MainDashboard)



class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True



xadmin.site.register(views.BaseAdminView, BaseSetting)



class GolbeSetting(object):
    globe_models_icon = {
        Publisher: 'group',
        Item: 'book',
        InStock: 'inbox',
        Order: 'edit'
    }



xadmin.site.register(views.CommAdminView, GolbeSetting)



class BaseItemAdmin(object):
    fields = ('item', 'code')
    list_display = ('item', 'code')
    list_filter = ('item', 'code')



class BasePublisherAdmin(object):
    fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)



class BaseInStockAdmin(object):
    fields = ('item', 'publisher')
    list_display = ('item', 'publisher')
    list_filter = ('item', 'publisher')



class BaseOrderAdmin(object):
    fields = ('item', 'ordered_by', 'order_date', 'received_date')
    list_display = ('item', 'ordered_by', 'order_date', 'received_date')
    list_filter = ('item', 'ordered_by', 'order_date', 'received_date')

    wizard_form_list = [
        ('First\'s Form', ('item', 'ordered_by')),
        ('Second Form', ('order_date', 'received_date'))
    ]

    relfield_style = 'fk-ajax'
    reversion_enable = True



class OrderAdmin(object):
    list_display = ('item', 'ordered_by', 'order_date', 'received_date')
    list_display_links = ('item',)


    search_fields = ['item', 'ordered_by', 'order_date', 'received_date']
    relfield_style = 'fk-ajax'
    reversion_enable = True



xadmin.site.register(Item, BaseItemAdmin)
xadmin.site.register(Publisher, BasePublisherAdmin)
xadmin.site.register(InStock, BaseInStockAdmin)
xadmin.site.register(Order, OrderAdmin)

