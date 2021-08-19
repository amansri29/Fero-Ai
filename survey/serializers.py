from rest_framework import serializers

from .models import Question, Survey, Response, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
            


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many = True)
    
    class Meta:
        model = Survey
        fields = ['id', 'subject', 'expring_date', 'questions']
        
    def validate_questions(self, value):
        """
        check if total number of questions are less than 10
        """
        
        if len(value) > 10:
            raise serializers.ValidationError("You can add maximum 10 questions")
        return value
    
    
    def create(self, validated_data):
       questions = validated_data.pop('questions', None)
       
       survey = Survey.objects.create(**validated_data)
       
       if not questions is None:
           for question in questions:
            #    check  if question is already exist in our model
                if Question.objects.filter(question = question['question']).exists():
                    survey.questions.add(Question.objects.get(question = question['question']))
                else:
                    survey.questions.add(Question.objects.create(**question))
       
       return survey
       
       
        
                    
        

class AnswerSerializer(serializers.ModelSerializer):
    question_desc = serializers.CharField(source='question.question', read_only = True)
    class Meta:
        model = Answer
        fields = ['question', 'question_desc', 'answer']      

class ResponseSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    
    class Meta:
        model = Response
        fields = ['id', 'survey', 'responder_name', 'response_date_time', 'answers']
        
    
    def create(self, validated_data):
       answers = validated_data.pop('answers', None)
       response = Response.objects.create(**validated_data)
       
       if not answers is None:
           for answer in answers:
                Answer.objects.create(response = response, **answer)
       
       return response
        
    
        



    