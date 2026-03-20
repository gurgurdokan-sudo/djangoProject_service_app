from django.contrib import admin
from .models import User, ServiceMaster, ServicePlan, ServiceRecord

admin.site.register(User)
admin.site.register(ServiceMaster)
admin.site.register(ServicePlan)
admin.site.register(ServiceRecord)
