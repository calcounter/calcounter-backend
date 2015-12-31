from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user = models.OneToOneField(User, unique=True)

    def __str__(self):
        return self.user.username


class Meal(models.Model):
    description = models.CharField(max_length=200, blank=True, default='')
    calories = models.CharField(max_length=5)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='meals')

    def __str__(self):
        return self.description

    # on save, update timestamps
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        super(Meal, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)

@receiver(post_save, sender=User)
def user_post_save(sender, instance, signal, *args, **kwargs):
    Profile.objects.get_or_create(user=instance)



