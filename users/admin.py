from django.contrib import admin

# Register your models here.
from .models import sport_Game,Volunteer_Programs,News,sport,sportSummar,comments

admin.site.register(sport_Game)
admin.site.register(Volunteer_Programs)
admin.site.register(News)
admin.site.register(sport)
admin.site.register(sportSummar)
admin.site.register(comments)