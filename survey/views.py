from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import SurveyResponse
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# Load tokenizer and model globally (once)
tokenizer = AutoTokenizer.from_pretrained("mental/mental-bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("mental/mental-bert-base-uncased")
model.eval()

def predict_depression_prob(text):
    """Return probability of depression from input text."""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = F.softmax(logits, dim=1)
    return probs[0][1].item()  # probability of "depressed"

def survey_view(request):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            # Calculate PHQ-9 total score
            phq9_score = sum(int(form.cleaned_data[f"phq9_q{i}"]) for i in range(1, 10))

            # Combine open-ended responses
            open_text = " ".join([
                form.cleaned_data.get("open_q1", ""),
                form.cleaned_data.get("open_q2", ""),
                form.cleaned_data.get("open_q3", "")
            ])

            # Predict depression probability
            bert_prob = predict_depression_prob(open_text)

            # Save to database
            SurveyResponse.objects.create(
                name=form.cleaned_data["name"],
                age=form.cleaned_data["age"],
                sex=form.cleaned_data["sex"],
                phq9_score=phq9_score,
                mentalbert_prob=bert_prob
            )

            return redirect("success")
    else:
        form = SurveyForm()

    # Prepare PHQ-9 fields for template display
    phq9_fields = [form[f"phq9_q{i}"] for i in range(1, 10)]

    return render(request, "survey/survey.html", {"form": form, "phq9_fields": phq9_fields})

def success_view(request):
    """Simple success page after form submission."""
    return render(request, "survey/success.html")

