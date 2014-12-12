import uuid

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
    is_published = models.BooleanField(default=False)
    time_published = models.DateTimeField(blank=True, null=True)
    time_modified = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['is_published', '-time_published']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return unicode(self).encode('utf-8')

    def save(self, *args, **kwargs):
        # Reject unauthorized author
        if self.author not in self.blog.authors.all():
            raise Exception(str(self.author) + ' is not authorized to post to '
                            + str(self.blog))

        # Create slug if it does not yet exist
        if not self.id:
            # The post was just created
            self.slug = slugify(self.title)

        # If published and no publication time, set to now
        if self.is_published and not self.time_published:
            self.time_published = timezone.now()

        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog.views.blog_post',
                       args=[self.blog.slug, str(self.id), self.slug])

    def get_number_of_views(self):
        return PostView.objects.filter(post=self).count()

    def is_future_publication(self):
        if self.time_published and self.time_published > timezone.now():
            return True
        else:
            return False


class PostView(models.Model):
    post = models.ForeignKey(Post)
    ip = models.IPAddressField()
    session_key = models.CharField(max_length=50)
    time_created = models.DateTimeField(auto_now_add=True)


def get_updated_filename(instance, filename):
    path = "images/{}/{}_{}".format(instance.user.id, uuid.uuid4(), filename)
    return path


class UploadedImage(models.Model):
    time_uploaded = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to=get_updated_filename)
