from django.contrib import admin

from users.models import UserProfile
from channels.models import Channel, Program, Slot
# Register your models here.
admin.site.register(Channel)
admin.site.register(Program)
admin.site.register(Slot)
