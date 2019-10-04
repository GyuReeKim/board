from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50) # 짧은 형태의 글
    content = models.TextField() # 긴 형태의 글 # django에서 TextField는 form 클래스에서 크기조절이 가능한 큰 상자가 생긴다.
    due_date = models.DateField()
    author = models.CharField(max_length=50)