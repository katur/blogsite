from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone


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
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, editable=False)
    author = models.ForeignKey(User)
    time_published = models.DateTimeField(editable=False)
    time_modified = models.DateTimeField(editable=False)
    content = models.TextField(blank=True)
    number_of_views = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        ordering = ['-time_published']

    def save(self, *args, **kwargs):
        """Update timestamps and slug."""
        if not self.id:
            # The post was just created
            self.slug = slugify(self.title)

            if not self.time_published:
                self.time_published = timezone.now()

        self.time_modified = timezone.now()

        return super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return unicode(self).encode('utf-8')
