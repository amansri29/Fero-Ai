from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed
from .models import Survey

def questions_changed(sender, **kwargs):
    """
    Making sure user do not add more than 10 questions to a survey
    """
    if kwargs['action'] == 'pre_add' and kwargs['instance'].questions.all().count() >= 10:
        raise ValidationError('Oops!! You can not add more than 10 questions to a survey')


m2m_changed.connect(questions_changed, sender=Survey.questions.through)