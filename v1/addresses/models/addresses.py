from django.db import models
from v1.commons.models.created_modified import CreatedModified
from .districts import District
from .provinces import Province
from .wards import Ward


class Address(CreatedModified):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(
        Province, related_name='%(class)s_province',
        on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey(
        District, related_name='%(class)s_district',
        on_delete=models.CASCADE, blank=True, null=True)
    ward = models.ForeignKey(
        Ward, related_name='%(class)s_ward',
        on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
