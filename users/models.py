from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    USERNAME_FIELD = 'username'
    email = models.EmailField(unique=True)
    

    def __str__(self):
        return self.username

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    level = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question_text

