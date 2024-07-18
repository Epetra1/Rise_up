from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Title)
admin.site.register(Points)
admin.site.register(Review)
