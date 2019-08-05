import re
from django.conf import settings
from django.forms import ValidationError
from django.shortcuts import resolve_url
from django.urls import reverse
from django.utils import timezone
from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import Thumbnail


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목', help_text='포스팅 제목을 입력해주세요 최대 100자 안으로'
                             # choices=(
                             #     ('제목1', '제목1 레이블'),
                             #     ('제목2', '제목2 레이블'),
                             #     ('제목3', '제목3 레이블'),
                             )
    content = models.TextField(verbose_name='내용')
    tag = models.CharField(max_length=100, blank=True)

    # >> ImageSpecField를 이용해 원본 이미지 유지 하면서 썸네일 만들기

    # photo = models.ImageField(blank=True)
    # photo_thumbnail = ImageSpecField(source="photo",
    #                                  processors=[Thumbnail(300, 300)],
    #                                  format='JPEG',
    #                                  options={'quality': 60})

    # >> 원본 유지 x 바로 만들기
    photo = ProcessedImageField(blank=True,
                                processors=[Thumbnail(300, 300)],
                                format='JPEG',
                                options={'quality': 60})

    lnglat = models.CharField(max_length=50, blank=True,
                              validators=[lnglat_validator],
                              help_text='경도, 위도 포멧으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
