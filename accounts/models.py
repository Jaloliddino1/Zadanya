from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.name}"

    class Meta:
        permissions = [
            ('can_publish_phone', 'Can publish phone'),
        ]
