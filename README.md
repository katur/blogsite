# Blog


## Overview
This is a website to test a blogging app. The goal is to eventually
make the blog app easily importable into any Django project.


## Features
### Post-level features
- Posts are written in Markdown, with easy syntax for bold, italics, lists,
  links, and inline images. This is the main reason I wanted to build a
  blogging app, because I find existing alternatives either too high-level
  (with Microsoft-Word-like interfaces that interpret text as HTML,
  subject to annoying misinterpretations), or too low-level (writing raw HTML).
- Authors can add and edit their own posts through a custom interface.
  When editing, the form is pre-populated with existing content.
- An author can choose whether to publish a post, or save it as a draft.
  If saved as a draft, it is only visible to the author (until the author
  chooses to publish it).
- Timestamps are automatically generated for post publication and modification
  times. Modification time is only displayed if it is after publication time.
- Publication time can be overridden to allow for a future publication time
  (in which case the post shows only for the author before publication time).
- Posts can be tagged with keywords.
- The number of post views are stored (using Django's session variables,
  so that multiple views by the same person are rarely recorded).

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
- image uploading
- live Markdown rendering while editing a post
- commenting (Disqus)
- allow deleting posts by the author (make sure to cascade effects)
- Markdown extension for image captions
- add option to sort posts by popularity (number of views), instead of
- add search term filter, and date filter. Refactor filtering so that each
  filter builds on the others that are already selected (e.g. so that tag cloud
  only reflects tags for the currently author selection)
- sharing posts on social media
- show conglomeration of posts across blogs
- better organize CSS so that styles are easier to customize
- add an option to disable truncation entirely


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
    - `django-taggit`: package for handling post tags
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
