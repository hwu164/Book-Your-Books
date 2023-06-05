from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator

# Create your models here.
# https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.
class Bin(models.Model):
    bin_id = models.AutoField(primary_key=True, editable=False)
    bin_name = models.CharField(max_length=5)
    def_loc = models.CharField(max_length=10)
    num_books = models.SmallIntegerField()

    
    def __str__(self):
        return self.bin_name

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True, editable=False)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

class Booked_Bin(models.Model):
    booking_id = models.AutoField(primary_key=True, editable=False)
    bin = models.ForeignKey(Bin, on_delete=models.PROTECT,related_name='bookings')
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    date = models.DateField(auto_now=False, auto_now_add=False)
    period = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.date} {self.period} ({self.bin_id})"

