from django.contrib import admin

from blog.models import Blog, Post


class BlogAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog', 'author', 'is_published',
                    'time_published')
    list_filter = ('blog', 'author', 'is_published', 'time_published')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
