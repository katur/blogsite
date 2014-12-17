from django.contrib import admin

from blog.models import Blog, Post, PostView, UploadedImage


class BlogAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog', 'author', 'is_published',
                    'time_published')
    list_filter = ('blog', 'author', 'is_published', 'time_published')


class PostViewAdmin(admin.ModelAdmin):
    list_display = ('post', 'session_key', 'time_created')


class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'user', 'time_uploaded')
    list_filter = ('user', 'time_uploaded')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostView, PostViewAdmin)
admin.site.register(UploadedImage, UploadedImageAdmin)
