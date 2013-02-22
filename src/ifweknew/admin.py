from django.contrib.admin import ModelAdmin
from django.contrib.admin import site as admin_site
from ifweknew.models import Wish

admin_site.register(Wish, ModelAdmin)
