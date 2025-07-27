from django.db import models
from django.contrib.auth import get_user_model

class Subscription(models.Model):
    subscriber = models.ForeignKey(get_user_model(), related_name='subscriber', on_delete=models.CASCADE)
    to_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='subscriptions')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("subscriber", "to_user")

    def __str__(self):
        return f'{self.subscriber.username} subscribed to {self.to_user.username}'