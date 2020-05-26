from django.conf import settings #다른 파일에 있는 것을 추가
from django.db import models
from django.utils import timezone

#모델을 정의#모델=object
class Post(models.Model): #post:모델 이름 //models는 Post가 장고 모델임을 의미
#이 코드 때문에 장고는 Post가 데이터 베이스에 저장되어야 한다고 앎
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#다른 모델에 대한 링크
    title = models.CharField(max_length=200) #글자수가 제한된 텍스트를 정의할 때 사용, 제목같은데 사용
    text = models.TextField() #글자 수에 제한이 없는 긴 텍스트를 위한 속성. 블로그 콘텐츠 용
    created_date = models.DateTimeField( #날짜와 시간
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):#publish라는 method
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #post모델의 제목텍스트(string)을 반환
