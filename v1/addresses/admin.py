from django.contrib import admin
from .models.provinces import Province
from .models.districts import District
from .models.wards import Ward
from .models.addresses import Address
# Register your models here.

admin.site.register(Province)
admin.site.register(District)
admin.site.register(Ward)
admin.site.register(Address)
