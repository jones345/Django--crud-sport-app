from django.contrib import admin

# Register your models here.
from .models import sport,sportGame,Volunteer,News

admin.site.register(sport)
admin.site.register(sportGame)
admin.site.register(Volunteer)
admin.site.register(News)