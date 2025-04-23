from django.db import models
from uuid import uuid4

from django.db import models





class BaseModel(models.Model):

    id = models.UUIDField(

        primary_key=True, editable=False, default=uuid4,
verbose_name="uuid"

    )

    created_time = models.DateTimeField(auto_now_add=True)

    updated_time = models.DateTimeField(auto_now=True)



    class Meta:

        abstract = True

        ordering = ["-updated_time"]


class Phone(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    file = models.FileField(upload_to='file')

    def __str__(self):
        return f"{self.brand} {self.name}"

    class Meta:
        db_table='upload_file'
        permissions = [
            ('can_publish_phone', 'Can publish phone'),
        ]