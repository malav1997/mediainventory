from django.db import models

from users.models import UserProfile
from channels.models import Slot

# Create your models here.
class Payment(models.Model):
    """ A model for creating new channels by channel admin"""

    payment_id = models.CharField(max_length=256, null=False)
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    slot = models.ForeignKey(Slot, on_delete=models.PROTECT)

