# Blog


## Overview
This is a website to test a blogging app. The goal is to eventually
make the blog app easily importable into any Django project.


## Features
### Post-level features
- Posts are written in Markdown, with easy syntax for bold, italics, lists,
  links, and inline images. This is the main reason I wanted to build a
  blogging app, because I find existing alternatives either too high-level
  (e.g. Microsoft-Word-like interface that interprets your text as HTML,
  subject to annoying misinterpretations), or too low-level (raw HTML).
  TODO: custom extension for image captions
- Authors can add their own posts through a custom interface.
  TODO: Add editing and deleting. When editing, pre-populate with
  existing content. Also, restrict any updates to blogs for which the user
  is an author, and restrict editing/deleting to user's own posts.
- Timestamps are automatically generated for post publication and modification
  times. Post publication time can be overridden to allow for a future
  publication time, in which case the post shows only for the author before
  publication time.
  Modification time is only displayed if it is after publication time.
  TODO: limit viewing the blog post page to the author only, until after
  publication.
- Posts can be tagged with keywords.
- The number of post views are stored (using Django's session variables,
  so that multiple views by the same person are rarely recorded).
- TODO: Image uploading
- TODO: Markdown extension for image captions
- TODO: live Markdown rendering
- TODO: Commenting (through disqus)
- TODO: Post can be shared with social media

### Blog-level features
- A blog can have multiple authors
- List-view of posts is paginated, defaulting to 10 posts
  (but can override by defining BLOG\_POSTS\_PER\_PAGE in settings).
- Posts are truncated in the list view, defaulting to 500 characters
  (but can override by defining BLOG\_POST\_TRUNCATION\_FACTOR in settings).
  TODO: an an option to disable truncation entirely
- List-view of posts is sorted by reverse publication time.
  TODO: add option to sort by number of views instead of time
- Frequency of tags within a blog visualized with a tag cloud
- The list of posts can be filtered by tag and/or author.
  TODO: add date filter, search filter
- TODO: RSS generator

### Global features
- Same website can have multiple blogs
- Infrequent moderation tasks (creating a blog, adding authors) can be done
  through the Django admin interface. Such privileges should be restricted
  to site administrators.
- TODO: (maybe) show conglomeration of posts


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
