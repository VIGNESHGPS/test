from django import forms
from .models import Study

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['study_name', 'sponsor_name', 'study_description', 'study_phase']