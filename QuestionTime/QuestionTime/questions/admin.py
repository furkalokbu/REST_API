from django.contrib import admin
from django.db.models.query_utils import Q
from questions.models import Answer, Question

admin.site.register(Answer)
admin.site.register(Question)
