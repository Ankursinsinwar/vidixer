# Create your models here.

from django.db import models
from users.models import User

class Project(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('in_progress', 'In Progress'),
        ('needs_review', 'Needs Review'),
        ('completed', 'Completed'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_projects')
    editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='editor_projects')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    uploaded_file = models.FileField(upload_to='uploads/raw/', null=True, blank=True)
    draft_video = models.FileField(upload_to='uploads/drafts/', null=True, blank=True)
    final_video = models.FileField(upload_to='uploads/final/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
