from django import forms
from .models import LeavePassRequest

class LeavePassRequestForm(forms.ModelForm):
    class Meta:
        model = LeavePassRequest
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-success'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-dark text-white border-success'
            }),
            'name_of_soldier': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-success'
            }),
            'leave_duration': forms.Select(attrs={
                'class': 'form-select bg-dark text-white border-success'
            }),
            'reason_for_leave': forms.Textarea(attrs={
                'class': 'form-control bg-dark text-white border-success',
                'rows': 4
            }),
        }
