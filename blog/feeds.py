from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.utils import feedgenerator

from blog.models import Blog
from blog.views import get_visible_posts


class AllPostsFeed(Feed):
    feed_type = feedgenerator.Rss201rev2Feed

    def get_object(self, request, blog_slug):
        return get_object_or_404(Blog, slug=blog_slug)

    def title(self, obj):
        return 'All posts for blog %s' % obj.name

    def link(self, obj):
        return obj.get_absolute_url()

    def description(self, obj):
        return 'Posts from blog %s' % obj.name

    def items(self, obj):
        posts = get_visible_posts(obj)
        return posts

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return item.get_absolute_url()

    def item_description(self, item):
        truncation = 300
        if len(item.content) > truncation:
            return item.content[0:truncation] + '...'
        else:
            return item.content

    def item_author_name(self, item):
        return item.author.get_full_name()

    def item_pubdate(self, item):
        return item.time_published

    def item_updateddate(self, item):
        return item.time_modified
