# Blog


## Overview
This is a website to test a blogging app. The goal is to eventually
make the blog app easily importable into any Django project.


## Features
- Same website can have multiple blogs
- Any blog can have multiple authors
- Timestamps generated for post creation and modification times
- Posts are sorted by reverse creation time
- Infrequent moderation tasks (creating a blog, adding authors)
  is done through the Django admin. Such privileges should not be granted
  to all authors, but rather to the site administrators.


#### Soon...
- Pagination (show just 10 posts per page), and truncation in list view to 500
  characters
- Routine update tasks (adding / editing / deleting posts) can be done
  by any of the listed authors on the project, to their own posts only.
  The forms for updating are pre-populated with the content.
- Markdown rendering for posts
- Tags (django-taggit), and associated navigation by tag
- Markdown extensions to insert and format images in posts
- Image uploading
- RSS
- Commenting (disqus)

#### If time...
- Live Markdown rendering so that you can see what the post will look like
  as you're writing.
- Share posts through social media
- Search to filter results
- Schedule posts for future publication (perhaps with optional timestamp
  parameter, that is allowed to be set to the future only)
- Show conglomeration of posts from all blogs as blogs landing page
- Option to treat main blog differently (so could live at /blog)
- Nice way to set options for pagination and truncation
- Keep track of number of views


## Requirements
Python version is specified in `runtime.txt`.

Package dependencies are listed in `requirements.txt`.

`Procfile` specifies the command to start the app.


## Development
CSS is in [SASS](http://sass-lang.com/). Run
`sass -wc --style compressed website/static/stylesheets/styles.sass`
to compile.
