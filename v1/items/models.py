from django.db import models
from v1.commons.models.created_modified import CreatedModified
from v1.users.models import User
from v1.addresses.models.addresses import Address


# Create your models here.
class Item(CreatedModified):
    Status = [
        ('R', 'rent'),
        ('S', 'sold'),
        ('A', 'available'),
        ('B', 'booked')
    ]
    name = models.CharField(max_length=255)
    address = models.ForeignKey(
        Address, related_name='%(class)s_address',
        on_delete=models.DO_NOTHING, blank=True, null=True)
    description = models.TextField()
    price = models.IntegerField()
    image = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name='created_by',
        on_delete=models.CASCADE, blank=True, null=True)
    view_count = models.IntegerField(default=0)
    status = models.CharField(max_length=1, choices=Status, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
