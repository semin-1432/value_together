from django import forms

from .models import Post

class PostForm(forms.ModelForm): #PostForm 우리가 만들 폼 이름
#이 폼이 Modelform이라는 걸 장고한테 전달

    class Meta: #어떤 모델이 쓰여야 하는가 전달
        model = Post
        fields = ('title', 'text',) # 두 필드
