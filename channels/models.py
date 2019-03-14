from django.db import models

from users.models import UserProfile


class Channel(models.Model):
    """ A model for creating new channels by channel admin"""

    channel_name = models.CharField(max_length=256)
    channel_admin = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    channel_broadcaster = models.CharField(max_length=256)
    channel_desc = models.TextField()

    def __str__(self):
        return self.channel_name


class Program(models.Model):
    """A model for adding a new program to the existing channel or newly created channel"""

    prog_name = models.CharField(max_length=256)
    channel = models.ForeignKey(Channel, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    prog_desc = models.TextField(null=True,)

    def __str__(self):
        return self.channel.channel_name + '-' + self.prog_name


class Slot(models.Model):
    """A model for adding advertisement slots in a program"""

    prog = models.ForeignKey(Program, on_delete=models.PROTECT)
    duration = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.prog.prog_name + '-' + str(self.duration)
