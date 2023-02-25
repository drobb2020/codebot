from django.db import models
from django.contrib.auth.models import User


class Code(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='code')
    question = models.TextField(max_length=5000)
    code_answer = models.TextField(max_length=5000)
    language = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
