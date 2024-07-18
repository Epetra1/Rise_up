from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

# I made all these models cause we still need to think what kind of representation are we doing in forntend 
# and maybe we might need images videos or maybe animations  for points module and icons and imagees for titles... and so on 
# not sure if i did it right .. please let me know \






# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(null=True, blank=True, unique=False)
    bio = models.TextField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to='profile_pictures')

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Category(models.Model):
    category_title = models.CharField(null = True, max_length= 50)

class Course(models.Model):
    course = models.CharField(null=False, max_length=50)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True)
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE, null = True)

class Title(models.Model):
    title = models.CharField(null = True, max_length=100)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, null = True)
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE, null = True)


class Topic (models.Model):
    topic = models.CharField(null = True, max_length = 100)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, null = True )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

class Points(models.Model):
    points = models.TextField(null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null = True )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

def validate_less_than_or_equal_to_ten(value):
    if value > 10:
        raise ValidationError('Value must be less than or equal to 10.')

class Review(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True)
    rating = models.IntegerField(validators=[validate_less_than_or_equal_to_ten])

    def save(self, *args, **kwargs):
        self.validate_less_than_or_equal_to_ten(self.rating)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user} - {self.rating}'