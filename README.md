# Blog


## Overview
This is a website to test a blogging app. The goal is to eventually
make the blog app easily importable into any Django project.


## Features
- Same website can have multiple blogs
- Any blog can have multiple authors
- Timestamps generated for post publication and modification times. Post
  publication time can be overridden to allow for a future publication time.
  TODO: don't show modification time if it is the same as publication time
- Posts are sorted by reverse publication time.
  TODO: add toggle to sort by number of views instead of time
- Infrequent moderation tasks (creating a blog, adding authors) can be done
  through the Django admin interface. Such privileges should be restricted
  to site administrators.
- Authors can add, edit, and delete their own posts through a custom interface.
  They can set posts to be published in the future.
  TODO: Still have to do editing and deleting. When editing, pre-populate with
  existing content. Also, restrict adding/editing to blogs that the user is
  a contributor for.
- Keep track of number of post views
- Markdown rendering for posts
- Pagination of list view of blog posts (when all listed, or after filtering).
  Defaults to 10 posts, but can override by defining BLOG\_POSTS\_PER\_PAGE
  in settings.
- Character truncation in list view. Defaults to 500 characters, but can
  override by defining BLOG\_POST\_TRUNCATION\_FACTOR in settings.
  TODO: an an option to disable truncation entirely
- Posts can be tagged (django-taggit), and frequency of tags can be visualized
  with a tag cloud (tag cloud works within a blog, or across blogs)
- Results can be filtered by tag, author. TODO: date, search


#### Soon...
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
