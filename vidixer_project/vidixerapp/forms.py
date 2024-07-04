from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'uploaded_by', 'video_file']
        widgets = {
            'uploaded_by': forms.HiddenInput(),
        }
