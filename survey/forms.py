from django import forms

PHQ9_QUESTIONS = [
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, or hopeless",
    "Trouble falling or staying asleep, or sleeping too much",
    "Feeling tired or having little energy",
    "Poor appetite or overeating",
    "Feeling bad about yourself, or that you are a failure",
    "Trouble concentrating on things",
    "Moving or speaking so slowly people notice or being restless",
    "Thoughts you would be better off dead, or hurting yourself",
]

PHQ9_CHOICES = [(0, "Not at all"), (1, "Several days"), (2, "More than half the days"), (3, "Nearly every day")]

class SurveyForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    sex = forms.ChoiceField(choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])

    # PHQ-9 questions
    for i, q in enumerate(PHQ9_QUESTIONS, 1):
        locals()[f"phq9_q{i}"] = forms.ChoiceField(label=q, choices=PHQ9_CHOICES, widget=forms.RadioSelect)

    # Open-ended
    open_q1 = forms.CharField(widget=forms.Textarea, label="Describe how you’ve been feeling lately")
    open_q2 = forms.CharField(widget=forms.Textarea, label="What do you think triggers your low mood?")
    open_q3 = forms.CharField(widget=forms.Textarea, label="How do you usually cope with stress?")
