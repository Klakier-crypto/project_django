from django.db import models

PRODUCT_STATUS = (
    ('Pending', 'Waiting for review'),
    ('Available', 'Avaliable'),
    ('Not Available', 'Not Available')
)


# Create your models here.
class Shop(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    product_url = models.URLField(null=True, blank=True) #blank pozwala na ominięcie wymagania pola w formularzu, null - wartość pusta
    status = models.CharField(choices=PRODUCT_STATUS, max_length=30, default='Pending')


class Opinion(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    reason = models.TextField()

