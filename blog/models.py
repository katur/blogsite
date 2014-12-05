import datetime

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Blog(models.Model):
    """A blog.

    There may be several blogs on different topics within the same website.
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    authors = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return unicode(self).encode('utf-8')


class Post(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=60, editable=False)
    author = models.ForeignKey(User)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        """Update timestamps and slug."""
        if not self.id:
            # The post was just created
            self.slug = slugify(self.title)
            self.time_created = datetime.datetime.today()

        self.time_modified = datetime.datetime.today()
        return super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return unicode(self).encode('utf-8')
