from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class Cohort(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="student_images")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)