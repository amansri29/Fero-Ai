from django.contrib import admin
from .models import Answer, Question, Response, Survey


class SurveyModelAdmin(admin.ModelAdmin):
    list_display = ['subject', 'expring_date']
    
    
class ResponseModelAdmin(admin.ModelAdmin):
    list_display = ['responder_name', 'survey', 'response_date_time']
    list_filter = ['survey']


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Survey, SurveyModelAdmin)
admin.site.register(Response, ResponseModelAdmin)
