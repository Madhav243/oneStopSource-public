from django import forms

from resources.models import Topic,SubTopic,Requests

class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields=('author','title','description','pic')


class SubTopicForm(forms.ModelForm):
    class Meta():
        model=SubTopic
        fields=('author','title','description','pic','link')
        

class RequestsForm(forms.ModelForm):
    class Meta():
        model=Requests
        fields=('topic','subTopic','newResourceTitle','description')