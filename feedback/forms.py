from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'name', 'email', 'start_date', 'end_date',
            'supervisor_name', 'experience_rating',
            'skills_learned', 'overall_satisfaction', 'suggestions'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'skills_learned': forms.Textarea(attrs={'rows': 3}),
            'suggestions': forms.Textarea(attrs={'rows': 3}),
            'experience_rating': forms.Select(),
            'overall_satisfaction': forms.RadioSelect(),
        }
