# Blog


## Overview
This is a website to test a blogging app. The goal is to eventually
make the blog app easily importable into any Django project.


## Features
- Same website can have multiple blogs
- Any blog can have multiple authors
- Timestamps generated for post publication and modification times, which can
  be overridden to allow for a future publication time
- Posts are sorted by reverse creation time
- Infrequent moderation tasks (creating a blog, adding authors)
  is done through the Django admin. Such privileges should not be granted
  to all authors, but rather to the site administrators.
- Keep track of number of post views
- Markdown rendering for posts
- Pagination (set in settings). TODO: implement default
- Character truncation in list view (set in settings). TODO: implement default


#### Soon...
- Authors can add, edit, and delete their own posts through a custom interface.
  They can set posts to be published in the future.
  When editing, the forms are pre-populated with previous content.
- Tags (django-taggit), and associated navigation by tag
- Image uploading
- Markdown extensions to insert and format images in posts
- RSS
- Commenting (disqus)

#### If time...
- Live Markdown rendering so that you can see what the post will look like
  as you're writing.
- Share posts through social media
- Search to filter results
- Nice way to set options for pagination and truncation
- Show conglomeration of posts from all blogs as landing page.
- Add toggle to view by popularity, to both this and the individual
  blog landing pages.


## Requirements
Python version is specified in `runtime.txt`.

Package dependencies are listed in `requirements.txt`.

`Procfile` specifies the command to start the app.


## Development
CSS is in [SASS](http://sass-lang.com/). Run
`sass -wc --style compressed website/static/stylesheets/styles.sass`
to compile.
