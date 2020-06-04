from django import forms

from .models import Post

class PostForm(forms.ModelForm): #우리가 만들 폼의 이름

    class Meta: #이 폼을 만들기 위해 Meta라는 model이 쓰임
        model = Post
        fields = ('title', 'text',)
