from django import forms
from jjam.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['category','subject', 'content']
        labels = {
            'category': '게시판',
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer  # 사용할 모델
        fields = ['content']
        labels = {
            'content': '내용',
        }    