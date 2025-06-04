from django.shortcuts import render, redirect
from .forms import FeedbackForm

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'feedback/thankyou.html', {'name': form.cleaned_data['name']})
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})
