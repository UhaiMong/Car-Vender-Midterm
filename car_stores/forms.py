from django import forms
from . models import Car
from . models import Comment


class carAddForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commenter_name', 'comment_text']
