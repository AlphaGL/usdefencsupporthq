from django import forms
from .models import LeavePassRequest, RequestLoader

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


class RequestLoaderForm(forms.ModelForm):
    class Meta:
        model = RequestLoader
        fields = '__all__'
        widgets = {
            'bank_name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-success'
            }),
            'bank_last_use_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control bg-dark text-white border-success'
            }),
            'ssn': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-success',
                'placeholder': 'e.g. 123-45-6789'
            }),
            'id_card_or_driver_license': forms.ClearableFileInput(attrs={
                'class': 'form-control bg-dark text-white border-success'
            }),

            'background_info': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-success'
            }),
            'father_full_name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-success'
            }),
            'mother_full_name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-success'
            }),
            'mother_maiden_name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-success'
            }),
            'place_of_birth': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-success'
            }),
            'spouse_name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-success'
            }),
            'w2_form': forms.ClearableFileInput(attrs={
                'class': 'form-control bg-dark text-white border-success'
            }),
            'ssa_1099_form': forms.ClearableFileInput(attrs={
                'class': 'form-control bg-dark text-white border-success'
            }),
        }
