# Markdown Blog
### By Katherine Erickson

## Overview
This is a website featuring a blogging app, where posts are written in
[Markdown](http://daringfireball.net/projects/markdown/syntax).

The inspiration for building this blogging app is that
I find existing alternatives either too high-level (with Microsoft-Word-like
interfaces that interpret text as HTML, subject to annoying
misinterpretations), or too low-level (writing raw HTML, which is cumbersome).
Specifically, I want to add this app to my mom's birding website, and she has
complained in the past about her existing blogs on Blogger or Wordpress,
where text does not always format the way she intends.
I'm hoping that Markdown strikes a nice balance for her, and for others.

This blogging app is not meant to be like wordpress.com or blogger.com,
where anyone can create an account and start their own blogs.
Rather, it is an extension to a website where the website
administrators maintain control over the blogs and who contributes
to them. Some examples of where it might be useful:

- An individual's portfolio site, with a single blog and single contributor.
- A site like my mom's birding website, which will have several blogs with
  several contributors besides my mom, but my mom will be the only one
  administering what blogs are created and who can contribute.
- A larger website (e.g., a newspaper or nonprofit), that might run hundreds
  of blogs with thousands of contributors, but would like to
  maintain strict control over blog creation and contribution.


## Features
### Global features
- A website can have multiple blogs.
- Infrequent moderation tasks (e.g., creating a blog, adding authors), as well
  as "superadmin" privileges (e.g., deleting or modifying other authors' posts)
  can be accessed through the built-in Django admin interface (located at
  /admin). Such privileges should be restricted to site administrators.

### Blog-level features
- A blog can have multiple authors.
- The list of posts is paginated, defaulting to 10 posts/page
  (but can be overridden by defining `BLOG_POSTS_PER_PAGE` in settings).
- Posts are truncated in the list view, defaulting to 500 characters
  (but can be overridden by defining `BLOG_POST_TRUNCATION_FACTOR` in settings).
- The list of posts is sorted by reverse publication time.
- The list of posts can be filtered by tag and/or author.
- The frequency of tags within a blog is visualized with a tag cloud.
- Each blog has an RSS feed (the feed includes all posts from the blog).

### Post-level features
- Posts are written in Markdown, which has easy syntax for bold, italics, lists,
  links, and inline images.
- Each post has a permalink, at which the entire post can be read.
- Authors can add and edit their own posts through a custom interface.
  When editing, the form is pre-populated with existing content.
- During editing, a live preview of the rendered Markdown is presented (using
  Markdown.js, a Javascript Markdown parser).
- Authors can upload images, which returns an image permalink. The images can be
  inserted inline into posts with the standard Markdown syntax, using the url of
  the uploaded image.
- An author can choose whether to publish a post immediately, or save it as a
  draft. If saved as a draft, it is only visible to the author until the
  author chooses to publish it.
- Timestamps are automatically generated for post publication and modification
  times. Modification time is only displayed if it is after publication time.
- Publication time can be overridden to allow for a future publication time
  (in which case the post is visible for only the author before publication time).
- Posts can be tagged with keywords.
- The number of views for each post is tracked. I use Django's session variables
  to limit recording multiple views by the same person.
- Anyone can comment on posts (with Disqus commenting, which allows commenters
  to log in with Disqus, Facebook, Twitter, and Google accounts).

<!---
### Features to build in the future (not yet implemented)
- Markdown extension for image captions and for video.
- Add option to sort posts by popularity (number of views), instead of by time
  published.
- Add filters for search term and date. Refactor filters to limit options based
  on already-selected filters.
- Share posts on social media.
- Author can delete their own posts (make sure to consider cascading to views,
  images, comments)
- Show conglomeration of posts across blogs on landing page.
- Better modularize website vs blog apps to make more easily importable into
  other projects. Better organize CSS to be easily customizable, too.
-->

## Instructions for Grader / Instructions for Testing
I have permission from Professor Korn to do this instead of the question/answer
service. It is similar to the blog project that has been done in previous years,
but a major difference is that mine limits the creation of users and blogs to
site administrators. It is meant as an extension for a website with strict
control over who is blogging, not as a service like wordpress.com that allows
arbitrary users to create accounts and start blogs.

To test, please go to the testing website (url submitted via the homework
submission system).
From the homepage, click on the prompt for the list of blogs,
and click on the blogs to browse their posts.
In the view showing paginated blog posts, select the links on the
right to filter by author and/or tag.
To see a post in its entirety and to comment on it,
click on the post title.

To log in as an author, click on Log In (upper right of screen), and log in as
tona (user and pw listed in `grader.txt`, uploaded through the homework
submission system).
tona only has permissions for "Birding Blog," and does not have permission
to administer anything but his own posts.
Logged in as tona, you will see his drafts in progress, as well as posts
scheduled to be published in the future.
Posts authored by tona will have an Edit link, and a link to add a post
will be on the right part of the "Birding Blog" list view.

On the pages to add or edit a post, you will see a live Markdown preview as
you type. Reminders of common Markdown syntax (e.g., italics, bold, links,
images) appear beneath the textarea,
along with a link for help with more advanced syntax (e.g., lists).
For an unpublished post, you can choose to save or publish.
If you would like to publish in the future, enter the date; otherwise,
the date will default to the time when published.
To upload an image, follow the link at the bottom of the edit page,
which opens a popup window and provides the URL after upload
(remember, since this is Markdown, you have to use the built-in
image syntax; a reminder of this appears beneath the textarea).

To test as an administrator, log in as laura (user and pw in `grader.txt`).
laura has author permissions for both blogs. In addition, laura can access the
built-in Django admin (located at /admin) to add blogs, add users, and grant
permissions to users.


## Developer's Guide
The project is built using the Django MVC web framework. The `blogsite` directory
contains the project-level configuration and settings files. Then, there are two
Django apps: `blog`, which contains the blogging functionality, and `website`,
a simple app representing a host website into which the blog is integrated.

### Python / Package Requirements
- The Python version is specified in `runtime.txt`.
- Package dependencies, including versions, are listed in `requirements.txt`.
  It is best to install them in a fresh virtual environment,
  with `pip install -r requirements.txt`. Some descriptions:
    - `Django`: MVC web framework
    - `MySQL-python`: Python interface to MySQL
    - `Markdown`: Python implementation of Markdown, for formatting blog posts
    - `Pillow`: "friendly" Python Imaging Library fork, for uploading images
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
- Commenting uses Disqus. While no packages are required for this, you must
  set up a Disqus account, and set `disqus_shortname` in
  `blog/templates/disqus.html`.

### CSS / Javascript
CSS is written in [SASS](http://sass-lang.com/). Run
`sass -wc --style compressed website/static/stylesheets/styles.sass` from the
project root to compile.

JavaScript used for the live Markdown rendering is written with jQuery.

### Database / Deployment
The project is deployed on Heroku with a MySQL database. Uploaded images are
stored on Amazon Web Service's S3 platform.
