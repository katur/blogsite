from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone

from taggit.managers import TaggableManager


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

    def get_absolute_url(self):
        return reverse('blog.views.blog',
                       args=[self.slug])


class Post(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, editable=False)
    author = models.ForeignKey(User)
    published = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['-published']

    def save(self, *args, **kwargs):
        """Update timestamps and slug."""
        if not self.id:
            # The post was just created
            self.slug = slugify(self.title)

        if not self.published:
            self.published = timezone.now()

        if self.author not in self.blog.authors.all():
            raise Exception(str(self.author) + ' is not authorized to post to '
                            + str(self.blog))

        return super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return unicode(self).encode('utf-8')

    def get_number_of_views(self):
        return PostView.objects.filter(post=self).count()

    def get_absolute_url(self):
        return reverse('blog.views.blog_post',
                       args=[self.blog.slug, str(self.id), self.slug])


class PostView(models.Model):
    post = models.ForeignKey(Post)
    ip = models.IPAddressField()
    session_key = models.CharField(max_length=50)
    time_created = models.DateTimeField(auto_now_add=True)
