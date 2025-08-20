from django.contrib import admin
from .models import SurveyResponse

@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "sex", "phq9_score", "mentalbert_prob", "submitted_at")
