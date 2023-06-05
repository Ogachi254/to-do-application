from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Todo(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('health', 'Health'),
        ('education', 'Education'),
        ('children', 'Children'),
        ('vacation', 'Vacation'),
        ('discipline', 'Discipline'),
        ('creativity', 'Creativity'),
        ('critical thinking', 'Critical Thinking'),
        ('family', 'Family'),
        ('art', 'Art'),
        ('strategy', 'Strategy'),
        ('conflict', 'Conflict'),
        ('understanding', 'Understanding'),
        ('pleasure', 'Pleasure'),
        ('fun', 'Fun'),
        ('pain', 'Pain'),
        ('stress', 'Stress'),
        ('anger management', 'Anger Management'),
        ('weight loss', 'Weight Loss'),
        ('sleep', 'Sleep'),
        ('excersice', 'Exercise'),
        ('party', 'Party'),
        ('ceremony', 'Ceremony'),
        ('study', 'Study'),
        ('programming', 'Programming'),
        ('employment', 'Employment'),
        ('debt', 'Debt'),
        ('fintech', 'Fintech'),
        ('assets', 'Assets'),
        ('agreements', 'Agreements'),
        ('company', 'Company'),
        ('fees', 'Fees'),
    ]

    title = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='food', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.title

