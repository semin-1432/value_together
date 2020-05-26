from django.contrib import admin #앞의 post모델을 가져오는 것
from .models import Post

admin.site.register(Post) #관리자 페이지에서 만든 모델을 보기 위해 해당 코드로 모델 등록
