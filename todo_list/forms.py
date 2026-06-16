from django import forms
from datetime import timedelta
from .models import List

class ListForm(forms.ModelForm):
    # Define distinct choice blocks for Days, Hours, and Minutes
    # Creating dropdown menu for Time Taken 
    DAY_CHOICES = [(str(d), f"{d} days" if d != 1 else "1 day") for d in range(8)] # 0 to 7 days
    HOUR_CHOICES = [(f"{h:02d}:00:00", f"{h} hours") for h in range(24)]
    MINUTE_CHOICES = [(f"00:{m:02d}:00", f"{m} mins") for m in range(0, 60, 5)]

    # Setup the structural form select controls
    duration_days = forms.ChoiceField(
        choices=[('', '-- Select Days --')] + DAY_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    duration_hours = forms.ChoiceField(
        choices=[('', '-- Select Hours --')] + HOUR_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    duration_minutes = forms.ChoiceField(
        choices=[('', '-- Select Minutes --')] + MINUTE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = List
        fields = ['item', 'completed', 'due_date', 'side_note', 'priority', 'file', 'image']