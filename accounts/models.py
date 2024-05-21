from django.db import models
from django.contrib.auth.models import User
import uuid
from django.dispatch import receiver
from base.emails import send_account_activation_mail
from base.models import BaseModel
from django.db.models.signals import post_save

class Profile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    is_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100)


@receiver(post_save, sender=User)

def send_verification_mail(sender,instance,created,**kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user=instance,email_token=email_token)
            email = instance.email
            send_account_activation_mail(email,email_token)

    except Exception as e:
        print(e)
