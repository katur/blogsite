from django.contrib import admin

from blog.models import Blog, Post


class BlogAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
