from django import forms
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item', 'completed', 'due_date', 'side_note', 'time_taken', 'priority', 'file', 'image']
