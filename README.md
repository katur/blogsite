# Markdown Blog


## Overview
This is a website featuring a blogging app, where posts are written in
[Markdown](http://daringfireball.net/projects/markdown/syntax)
(just like this README file).
The goal is to eventually make the blogging app easily importable into
any Django project.

The primary inspiration for building this blogging app is that
I find existing alternatives either too high-level (with Microsoft-Word-like
interfaces that interpret text as HTML, subject to annoying
misinterpretations), or too low-level (writing raw HTML, which is cumbersome).
Specifically, I want to add this app to my mom's birding website, and she has
complained in the past about her existing blogs on Blogger or Wordpress,
where text does not always format the way she intends.
I'm hoping that Markdown strikes a nice balance for her, and for others.

This blogging app is not meant to be like wordpress.com or blogger.com,
where anyone can create an account and create their own blogs.
Rather, it is meant to be added as an extension to a website where the website
administrators control what blogs get made and who contributes to them.
Some examples of where it might be useful:

- An individual's portfolio site, with a single blog and single contributor.
- A site like my mom's birding website, which will have several blogs with
  several contributors besides my mom, but my mom will be the only
  administrator that controls what blogs are created and who can contribute.
- A larger website, e.g. for a newspaper or nonprofit, that might run hundreds
  of blogs with thousands of contributors, but that would like to
  maintain strict control over which blogs are made and who can contribute.


## Notes / Instructions for Grader
I got permission from the Professor to do this instead of the question/answer
service. It is similar to a blog project done in previous years, but one
major difference is that mine leaves the creation of blogs and blog writers
to the site administrators.

To test the site, please go to the testing website (submitted via the homework
permission system, and also listed in `text_accounts_for_grader.txt`).
You should not be logged in, but you should be able to navigate to the list of
blogs, and browse both listed blogs. In the list view, you can click on filters
on the right side of the screen to limit which posts are seen by author or tag.
To see a post in its entirety and to be able to comment on it (through Disqus),
click on the post title.

To log in as a contributor, click on Log In (upper right of screen),
and log in as katherine (user and pw listed in `text_accounts_for_grader.txt`).
katherine has permissions for Birding Blog only, and does not have permission
to administer the site otherwise.
You will see that any drafts that Katherine has in progress, as well as those
scheduled to be published in the future, now show in the list view (with an
obvious background to distinguish them from what is publically visible).
On the upper right of the landing page for the Birding Blog,
you will see a link to add a new post, and will also see links to edit each
post that Katherine wrote. After clicking on these, you should be able to
add/edit post content and titles, see the live Markdown rendering as you write,
add tags, and save the draft or publish. To upload images, there are links
at the bottom of the screen (to upload a new image or browse your existing
uploads), which open popup windows and give the URLs for adding inline
images (but remember since this is Markdown, you have to use the builtin
inline image syntax; a reminder of this appears beneath the textarea on the
add/edit pages).

If you would like to log in as an administer, log out and log in as laura.



## Features
### Post-level features
- Posts are written in Markdown, with easy syntax for bold, italics, lists,
  links, and inline images.

- Authors can add and edit their own posts through a custom interface.
  When editing, the form is pre-populated with existing content.
- During editing, a preview of the Markdown render can be viewed live (using
  the Markdown.js Javascript Markdown parser).
- Authors can upload images. The images can be inserted into posts with the
  standard Markdown syntax, using the url of the uploaded image. (Any images
  available on the web can be uploaded this way.)
- An author can choose whether to publish a post immediately, or save it as a
  draft. If saved as a draft, it is only visible to the author (until the
  author chooses to publish it).
- Timestamps are automatically generated for post publication and modification
  times. Modification time is only displayed if it is after publication time.
- Publication time can be overridden to allow for a future publication time
  (in which case the post shows only for the author before publication time).
- Posts can be tagged with keywords.
- The number of post views are stored (using Django's session variables,
  so that multiple views by the same person are rarely recorded).
- Anyone can comment on posts (with Disqus commenting).

### Blog-level features
- A blog can have multiple authors
- List-view of posts is paginated, defaulting to 10 posts
  (but can override by defining BLOG\_POSTS\_PER\_PAGE in settings).
- Posts are truncated in the list view, defaulting to 500 characters
  (but can override by defining BLOG\_POST\_TRUNCATION\_FACTOR in settings).
- List-view of posts is sorted by reverse publication time.
- The list of posts can be filtered by tag and/or author.
- Frequency of tags within a blog visualized with a tag cloud.
- Each blog has an RSS feed (the feed includes all posts from the blog)

### Global features
- Same website can have multiple blogs
- Infrequent moderation tasks (creating a blog, adding authors) can be done
  through the Django admin interface. Such privileges should be restricted
  to site administrators.


### Future features (not implemented yet)
- Markdown extension for image captions.
- Markdown extension for video.
- Add option to sort posts by popularity (number of views), instead of
- Add search term filter, and date filter. Refactor filtering so that each
  filter builds on the others that are already selected (e.g. so that tag cloud
  only reflects tags for the currently author selection)
- Allow sharing posts on social media.
- Allow deleting posts by the author (skipped for now because want to make sure
  to cascade all effects properly, such as the deleting the post's views,
  the post's images if not used by other posts, etc)
- Show conglomeration of posts across blogs on /blog landing page.
- Better modularize website vs blog apps to make more easily importable into
  other projects. Better organize CSS to be easily customizable, too.


## Requirements
- Python version is specified in `runtime.txt`.
- Database is in MySQL
- Package dependencies are listed in `requirements.txt`.
  It is best to install them in a fresh virtual environment,
  with `pip install -r requirements.txt`.
  Some notes:
    - `Django`: MVC web framework
    - `MySQL-python`: Python interface to MySQL
    - `Markdown`: Python implementation of Markdown, for formatting blog posts
    - `Pillow`: "friendly" Python Imaging Library fork
    - `django-taggit`: package for handling post tags
    - `django-storages` and `boto`: for using S3 on Amazon Web Services to
      serve uploaded media
    - `gunicorn`, `dj-static`, `static3`, `dj-database-url`:
      packages for production-level deploy on heroku
      (Gunicorn is the WSGI HTTP server,
      dj-static serves static files and requires static3,
      dj-database-url simplifies defining the database connection as a
      path variable)
    - `wsgiref`: automatically included in virtualenv
- `Procfile` specifies the command to start the app.


## Development
CSS is in [SASS](http://sass-lang.com/). Run
`sass -wc --style compressed website/static/stylesheets/styles.sass`
to compile.
