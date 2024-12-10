from django.db import models


from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FeedbackModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user.username}"
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Feddback'
        verbose_name_plural = 'Feddbacks'