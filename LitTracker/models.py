from django.db import models



class Item(models.Model):
    item = models.CharField(max_length=200)
    code = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.item)


class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.name)



class Order(models.Model):
    item = models.ForeignKey(Item)
    ordered_by = models.ForeignKey(Publisher)
    order_date = models.DateTimeField('Date Ordered')
    received_date = models.DateTimeField('Date Received', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.item)

class InStock(models.Model):
    item = models.ForeignKey(Item)
    publisher = models.ForeignKey(Publisher)

    def __unicode__(self):
        return unicode(self.item)