# Markdown Blog


## Overview
This is a test website that includes a blogging app. The goal is to eventually
make the blogging app easily importable into any Django project.

The main inspiration for this blogging app is that posts are written in
Markdown. I chose to do this because I find existing alternatives either
too high-level (with Microsoft-Word-like interfaces that interpret text as
HTML, subject to annoying misinterpretations),
or too low-level (writing raw HTML).
Specifically, I want to add this app to my mom's birding website, and she has
complained in the past about her existing blogs on Blogger or Wordpress,
where text is not always formatted the way she intends.
But the alternative of writing in raw HTML is too cumbersome.
I'm hoping that Markdown strikes a nice balance.

This blogging app is not meant to be like wordpress.com or blogger.com,
where anyone can create an account and create their own blogs.
Rather, it is meant to be added as an extension
to a website where the website administrators control what blogs get made and
who contributes to them.
Some examples of where it might be useful:

- An individual's portfolio site, with a single blog and single contributor
- A site like my mom's birding website, which will have several blogs with
  several contributors besides my mom, but my mom being the only administrator
  that controls what blogs are created and who can contribute to them
- A larger site, such as a newspaper or nonprofit, that might run hundreds
  of blogs with thousands of contributors, but that would still want to
  maintain strict control over which blogs are made and who can write to them


## Notes to Grader
I got permission from the Professor to do this instead of the question/answer
service. It is similar to a blog project done in the past. One major difference
is that this



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
