import uuid
from django.db import models

class Customer(models.Model):
    customer_id = models.UUIDField(default = uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    agent_id = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return self.name