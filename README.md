# Blog


## Overview
This is a website to test a blogging app. The goal is to eventually
make the blog app easily importable into any Django project.


## Features
- Same website can have multiple blogs
- Any blog can have multiple authors
- Timestamps generated for post publication and modification times. Post
  publication time can be overridden to allow for a future publication time.
  TODO: only show modification time when after publication time. Posts are
  sorted by reverse publication time.
- Infrequent moderation tasks (creating a blog, adding authors)
  is done through the Django admin. Such privileges should not be granted
  to all authors, but rather to the site administrators.
- Keep track of number of post views
- Markdown rendering for posts
- Pagination of list view of blog posts (when alllisted, or after filtering).
  Defaults to 10 posts, but can override by defining BLOG\_POSTS\_PER\_PAGE
  in settings.
- Character truncation in list view. Defaults to 500 characters, but can
  override by defining BLOG\_POST\_TRUNCATION\_FACTOR in settings.
  TODO: an an option to disable truncation entirely
- Tags (django-taggit), and tag cloud (tag cloud also works across blogs)
- Nice way to set options for pagination and truncation


#### Soon...
- Authors can add, edit, and delete their own posts through a custom interface.
  They can set posts to be published in the future.
  When editing, the forms are pre-populated with previous content.
- Filtering results by tag, author, date, search
- Image uploading
- Markdown extension for inserting and formatting images in posts
- RSS

#### If time...
- Commenting (through disqus)
- Share posts through social media
- Search to filter results
- Live Markdown rendering so that you can see what the post will look like
  as you're writing.
- Show conglomeration of posts from all blogs as landing page.
- Add toggle to sort posts by popularity, to both this and the individual
  blog landing pages.


## Requirements
Python version is specified in `runtime.txt`.

Package dependencies are listed in `requirements.txt`.

`Procfile` specifies the command to start the app.


## Development
CSS is in [SASS](http://sass-lang.com/). Run
`sass -wc --style compressed website/static/stylesheets/styles.sass`
to compile.
