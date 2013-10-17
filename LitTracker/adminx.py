import xadmin
from xadmin import views
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction
from LitTracker.models import *


class MainDashboard(object):
    widgets = [
    ]


xadmin.site.register(views.website.IndexView, MainDashboard)

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


xadmin.site.register(Item, BaseItemAdmin)
xadmin.site.register(Publisher, BasePublisherAdmin)
xadmin.site.register(InStock, BaseInStockAdmin)
xadmin.site.register(Order, BaseOrderAdmin)

