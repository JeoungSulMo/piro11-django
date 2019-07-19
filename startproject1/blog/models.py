import re
from django.forms import ValidationError
from django.utils import timezone
from django.db import models


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목', help_text='포스팅 제목을 입력해주세요 최대 100자 안으로',
                             choices=(
                                 ('제목1', '제목1 레이블'),
                                 ('제목2', '제목2 레이블'),
                                 ('제목3', '제목3 레이블'),
                             ))
    content = models.TextField(verbose_name='내용')
    tag = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
                              validators=[lnglat_validator],
                              help_text='경도, 위도 포멧으로 입력')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
