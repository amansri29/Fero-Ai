# importing validationerror
from django.core.exceptions import ValidationError
from django.db import models


class Question(models.Model):
    question = models.TextField()
    
    def __str__(self):
        return self.question
    


class Survey(models.Model):
    subject = models.CharField(max_length=150)
    # survey will expire on this date
    expring_date = models.DateField()
    questions = models.ManyToManyField(Question, related_name='Survey')
    
    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    answer = models.TextField()
    
    def __str__(self):
        return f'Ques- {self.question.question} Ans- {self.answer}'
    
    

class Response(models.Model):
    response_date_time = models.DateTimeField(auto_now_add=True)
    responder_name = models.CharField(max_length=100)
    survey = models.ForeignKey(Survey, related_name='response', on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer, related_name='response')
    
    def __str__(self):
        return f'{self.responder_name} - {self.survey.subject}'
    
