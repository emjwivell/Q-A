from django.contrib import admin
from app.models import UserProfile, Tag, Question, Answer, Vote

admin.site.register(UserProfile)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Vote)
