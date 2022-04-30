from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

def validate_even(value):
    if value != 10:
        raise ValidationError(
            _("Enter valid phone number"),
        )
# Create your models here.

class Login(models.Model):
    member_id = models.IntegerField(primary_key=True)

class FeedBack(Login):
    password = None
    feed_back = models.CharField(max_length=150)


class RegisterEvent(Login):
    class EventTypes(models.TextChoices):
        WEDDING = 1
        SOCIAL = 2
        CORPORATE = 3
    password = None
    event_type = models.TextField(choices=EventTypes.choices)
    requirements = models.TextField(max_length=300)
    no_of_guests = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError(
                      "Dates unmatched"
                      "Please enter correct dates")

class Rooms(Login):

    class RoomType(models.TextChoices):
        AC = 1
        NON_AC = 2

    password = None
    amount = models.IntegerField()
    accommodate_date_start = models.DateField()
    room_no = models.IntegerField()
    no_of_people = models.IntegerField()
    accommodate_date_end = models.DateField()

    class Meta:
        unique_together = (("member_id", "room_no"),)

    def clean(self):
        cleaned_data = super().clean()
        accommodate_date_start = cleaned_data.get("accommodate_date-start")
        accommodate_date_end = cleaned_data.get("accommodate_date_end")

        if accommodate_date_start and accommodate_date_end:
            if accommodate_date_start > accommodate_date_end:
                raise ValidationError("Enter correct dates for accommodation")
class Payment(models.Model):
    class Meta:
        abstract = True

    class PaymentType(models.TextChoices):
        UPI = 1
        CREDIT_CARD = 2
        DEBIT_CARD = 3
        ONLINE_BANKING = 4

    payment_type = models.TextField(choices=PaymentType.choices)
    amount = models.FloatField()
    payment_id = models.CharField(max_length=13, primary_key=True)

class MembershipRegistration(AbstractBaseUser, PermissionsMixin):

    class Types(models.TextChoices):
        SILVER = 1
        GOLD = 2
        PLATINUM = 3
    membership_payment_id = models.IntegerField(max_length=13)
    membership_payment_amount = models.IntegerField()
    membership_type = models.TextField(choices=Types.choices)
    email = models.EmailField(primary_key=True,)
    name = models.TextField(_('user_name'), blank=False)
    phone = models.IntegerField(max_length=10)
    password = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
    date_of_birth = models.DateField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

class Manager(BaseUserManager):
    def create_user(self,email,user_name,password,**other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email,user_name=user_name,**other_fields)
        user.set_password(password)
        user.save()
        return user