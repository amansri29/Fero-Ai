import datetime

from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response as ResponseDRF

# local imports
from .models import Response, Survey
from .serializers import ResponseSerializer, SurveySerializer


class ResponseCreateView(generics.ListCreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    
class SurveyViewSet(ModelViewSet):
    serializer_class = SurveySerializer
    # filter_fields = ('budget','enable')
    queryset = Survey.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        """
            overiding the function to check and respond 
            if the survey is expired or not
        """
        instance = self.get_object()
        print((datetime.datetime.now().date() - instance.expring_date).days)
        
        if (datetime.datetime.now().date() - instance.expring_date).days >= 0:
            return ResponseDRF(status=200, data = {"message" : "This survey is expired"})

        
        serializer = self.get_serializer(instance)
        return ResponseDRF(serializer.data)
    
    
    @action(detail = True, methods = ['GET',], url_path='responses', url_name = "responses")
    def get_responses(self, request, *args, **kwargs):
        """
        This view is responsible to return all the responses of the particular survey
        """
        survey = self.get_object()
        responses = Response.objects.filter(survey = survey)
        
        return ResponseDRF(ResponseSerializer(responses, many = True).data)
        
        