from django.db import models

class List(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
    # C_002 Schema Extensions (Optional fields with priority set as 'Medium' by default)
    due_date = models.DateTimeField(null=True, blank=True)
    side_note = models.TextField(null=True, blank=True) 
    time_taken = models.DurationField(null=True, blank=True) 
    priority = models.CharField(
        max_length=6, 
        choices=PRIORITY_CHOICES, 
        default='Medium', 
        null=True, 
        blank=True
    )

<<<<<<< HEAD
    def __str__(self):
        return self.item + ' | ' + str(self.completed)
=======
    # New upload fields
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)
    
    @property
    def formatted_duration(self):
        actual_field = getattr(self, 'time_taken', None)
        if not actual_field:
            return "-"
            
        total_seconds = int(actual_field.total_seconds())
        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60
        
        parts = []
        if days > 0:
            parts.append(f"{days} Day{'s' if days > 1 else ''}")
        if hours > 0:
            parts.append(f"{hours} Hr")
        if minutes > 0:
            parts.append(f"{minutes} Min")
            
        return " ".join(parts) if parts else "0 Min"
        
    
>>>>>>> main
