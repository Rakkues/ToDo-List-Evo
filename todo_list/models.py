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

    # New upload fields
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)
    
    
