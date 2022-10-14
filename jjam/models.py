from random import choices
from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ("당근", "당근"),
    ("전파사항", "전파사항"),
    ("분실물", "분실물"),
    ("칭찬하기", "칭찬하기"),
)
class Question(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES, max_length =10)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_question")
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name="voter_question")
    
    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_answer")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name="voter_answer")

class QuestionCount(models.Model):
    ip = models.CharField(max_length=30)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.ip