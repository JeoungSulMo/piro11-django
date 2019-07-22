from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'content_size', 'created_at', 'updated_at']
    actions = ['make_published', 'make_Draft', 'make_withdrawn']

    def content_size(self, post):
        return '{}글자' .format(len(post.content))

    content_size.short_description = '내용 글자수'
    content_size.allow_tags = True
#admin.site.register(Post, PostAdmin)

    def make_withdrawn(self, request, queryset):
        updated_count = queryset.update(status='w')
        self.message_user(request, '{}건의 포스팅을 withdrawn 상태로 변경'.format(updated_count))
    make_withdrawn.short_description = '지정포스팅을 withdrawn 상태로 변경합니다.'


    def make_Draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 Draft 상태로 변경'.format(updated_count))
    make_Draft.short_description = '지정포스팅을 Draft 상태로 변경합니다.'


    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 published 상태로 변경'.format(updated_count))
    make_published.short_description = '지정포스팅을 published 상태로 변경합니다.'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass