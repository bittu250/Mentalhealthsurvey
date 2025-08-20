from django.db import models

class SurveyResponse(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=10)
    phq9_score = models.PositiveIntegerField()
    mentalbert_prob = models.FloatField(default=0.01)  # numeric probability 0–1
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - PHQ9: {self.phq9_score}, BERT: {self.mentalbert_prob:.2f}"



# Create your models here.
