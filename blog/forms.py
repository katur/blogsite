from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime

from blog.models import Post


class NewPostForm(forms.ModelForm):
    time_published = forms.DateTimeField(required=False,
                                         widget=AdminSplitDateTime(),
                                         label='Publication time',
                                         help_text='Optional; defaults to now')

    content = forms.CharField(widget=forms.Textarea,
                              help_text='Use Markdown.')

    class Meta:
        model = Post
        fields = ['blog', 'title', 'content', 'tags', 'time_published',
                  'author']
