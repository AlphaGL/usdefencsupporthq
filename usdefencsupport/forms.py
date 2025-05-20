from django import forms
from .models import LeavePassRequest

class LeavePassRequestForm(forms.ModelForm):
    class Meta:
        model = LeavePassRequest
        fields = '__all__'
