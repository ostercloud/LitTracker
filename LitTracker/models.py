from django.db import models



class Item(models.Model):
    item = models.CharField(max_length=200)
    code = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.item)

    class Meta:
        verbose_name = u"Item"
        verbose_name_plural = verbose_name


class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = u"Publisher"
        verbose_name_plural = verbose_name



class Order(models.Model):
    item = models.ForeignKey(Item)
    ordered_by = models.ForeignKey(Publisher)
    order_date = models.DateTimeField('Date Ordered')
    received_date = models.DateTimeField('Date Received', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.item)

    class Meta:
        verbose_name = u"Order"
        verbose_name_plural = verbose_name



class InStock(models.Model):
    item = models.ForeignKey(Item)
    publisher = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return unicode(self.item)

    class Meta:
        verbose_name = u"In Stock"
        verbose_name_plural = verbose_name

    pendingitems = Order.objects.exclude(received_date__null=False).filter(item=item).order_by('order_date')[0:1].get()
