from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime

from blog.models import Post


MARKDOWN_HELP_TEXT = """
Please use
<a href="http://daringfireball.net/projects/markdown/syntax">Markdown</a>.
Examples:
<br>
*bold*, **italics**, - bulleted, 1. numbered
<br>
&lt;http://google.com&gt;
<br>
[click here](http://google.com)
<br>
![squirrel](http://squirrel.jpg)
<br>
![squirrel](http://squirrel.jpg "My Pet Squirrel")
"""

DATETIME_HELP_TEXT = """
Optional; defaults to now. Example:
<br>
Date: 1996-12-04
<br>
Time: 13:14:34
"""


class PostForm(forms.ModelForm):
    time_published = forms.DateTimeField(required=False,
                                         widget=AdminSplitDateTime(),
                                         label='Publication time',
                                         help_text=DATETIME_HELP_TEXT)

    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': '24', 'cols': '80'}),
        help_text=MARKDOWN_HELP_TEXT)

    class Meta:
        model = Post
        fields = ['blog', 'title', 'content', 'tags', 'time_published',
                  'author']

    def save(self, commit=True, publish=False):
        instance = super(PostForm, self).save(commit=False)
        if publish and not instance.is_published:
            instance.is_published = True

        if commit:
            instance.save()

            # Below needed to save the tags
            self.save_m2m()
        return instance


class UploadImageForm(forms.Form):
    image = forms.ImageField()
