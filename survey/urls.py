from django.urls import path
# rest import 
from rest_framework.routers import DefaultRouter

# local import 
from .views import ResponseCreateView, SurveyViewSet


app_name = 'survey'

router = DefaultRouter()
router.register('survey', SurveyViewSet, basename='survey')


urlpatterns = [
    path('responses/', ResponseCreateView.as_view(), name='responses'),
]


urlpatterns = router.urls + urlpatterns