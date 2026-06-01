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
        fields = ['item', 'completed', 'due_date', 'side_note', 'priority']

    # Pre-fill selections when loading an existing item to Edit
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance and self.instance.time_taken:
            duration = self.instance.time_taken
            
            # Extract days directly from the timedelta object
            days = duration.days
            
            # Extract hours and minutes from the remaining seconds block
            remaining_seconds = duration.seconds
            hours = remaining_seconds // 3600
            minutes = (remaining_seconds % 3600) // 60
            
            # Map minutes accurately to our closest 5-minute selector increment
            minutes = min(range(0, 60, 5), key=lambda x: abs(x - minutes))
            
            # Inject selections straight back into your input controls
            self.initial['duration_days'] = str(days) if days > 0 else ''
            self.initial['duration_hours'] = f"{hours:02d}:00:00" if hours > 0 else ''
            self.initial['duration_minutes'] = f"00:{minutes:02d}:00" if minutes > 0 else ''

    # Consolidate separate UI selections back into one unified database object
    def clean(self):
        cleaned_data = super().clean()
        days_val = cleaned_data.get('duration_days')
        hours_val = cleaned_data.get('duration_hours')
        mins_val = cleaned_data.get('duration_minutes')

        total_duration = timedelta()

        if days_val:
            total_duration += timedelta(days=int(days_val))
        if hours_val:
            h = int(hours_val.split(':')[0])
            total_duration += timedelta(hours=h)
        if mins_val:
            m = int(mins_val.split(':')[1])
            total_duration += timedelta(minutes=m)

        # Assign back to your underlying database field
        if days_val or hours_val or mins_val:
            cleaned_data['time_taken'] = total_duration
        else:
            cleaned_data['time_taken'] = None

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.time_taken = self.cleaned_data.get('time_taken')
        if commit:
            instance.save()
        return instance