from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'uploaded_by', 'video_file']  # Include 'uploaded_by' field
        # fields = ['title', 'description', 'video_file']  # Don't include 'uploaded_by' field
