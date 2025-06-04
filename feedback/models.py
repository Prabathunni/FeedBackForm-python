from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)  # Intern's Full Name
    email = models.EmailField()
    start_date = models.DateField()
    end_date = models.DateField()
    supervisor_name = models.CharField(max_length=100, blank=True)
    experience_rating = models.CharField(max_length=10, choices=[
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Poor', 'Poor'),
    ])
    skills_learned = models.TextField()
    overall_satisfaction = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    suggestions = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
