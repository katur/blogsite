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


## Features
### Post-level features
- Posts are written in Markdown, with easy syntax for bold, italics, lists,
  links, and inline images.
- Authors can add and edit their own posts through a custom interface.
  When editing, the form is pre-populated with existing content.
- During editing, a live preview of the Markdown render is visible (using
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


### Future directions (not yet implemented)
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


## Instructions for Grader / Test accounts
I got permission from the Professor to do this instead of the question/answer
service. It is similar to the blog final project that has been done in
previous years of the course, but a major difference is that mine limits
the creation of users and blogs to site administrators. It is meant as a
feature for a website with strict control over who is blogging,
not as a service like wordpress.com that allows arbitrary users to start blogs.

To test, please go to the testing website (submitted via the homework
permission system, and also listed in `text_accounts_for_grader.txt`).
From the homepage, click on the prompt for the list of blogs,
and click on the blogs to browse their posts.
In the view showing paginated blog posts, select the links on the
right to filter by author and/or tag.
To see a post in its entirety and to be able to comment on it,
click on the post title.

To log in as an author, click on Log In (upper right of screen),
and log in as katherine (user and pw listed in `test_accounts_for_grader.txt`).
katherine has permissions for Birding Blog only, and does not have permission
to administer anything but her own posts.
Logged in as katherine, you will see her drafts in progress, as well as posts
scheduled to be published in the future (with an obvious background to
distinguish them from what is publically visible).
Posts authored by katherine will have an Edit link, and a link to add a post
should be on the right part of the screen.

On the pages to add or edit a post, you should see a live Markdown preview as
you type. Reminders of common Markdown syntax (e.g. italics, bold, links,
images) appear beneath the text area,
along with a link for help with more advanced syntax (e.g. lists).
For an unpublished post, you can choose to save or publish.
If you would like to publish in the future, enter the date; otherwise,
the date will default to the time published.
To upload an image, follow the link at the bottom of the screen,
which opens a popup window and provides the URL after upload
(remember since this is Markdown, you have to use the builtin
inline image syntax; a reminder of this appears beneath the textarea on the
add/edit pages).

If you would like to log in as an administer, log out and log in as laura
(user and pw in `test_accounts_for_grader.txt`). laura has write permissions
for both blogs. In addition, laura can access the site admin
(url in `test_accounts_for_grader.txt`) with privileges to add blogs,
add users, grant permissions to users, delete posts, edit other authors' posts,
etc.


## Development notes
### Code organization
The project is built using the Django web framework. There are two Django apps.
`blog` contains the blogging functionality, which I'm
hoping to eventually make easily importable into other projects.
`website` is just the simple testing website.

### Python / Package Requirements
- Python version is specified in `runtime.txt`.
- Package dependencies are listed in `requirements.txt`.
  It is best to install them in a fresh virtual environment,
  with `pip install -r requirements.txt`.
  Some notes:
    - `Django`: MVC web framework
    - `MySQL-python`: Python interface to MySQL
    - `Markdown`: Python implementation of Markdown, for formatting blog posts
    - `Pillow`: "friendly" Python Imaging Library fork, needed for uploading
      images
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

### CSS / Javascript
CSS is in [SASS](http://sass-lang.com/). Run
`sass -wc --style compressed website/static/stylesheets/styles.sass`
to compile.

Custom javascript (used for the live Markdown rendering) is in jQuery.

### Database / Deployment
The project is deployed on heroku, with a MySQL database. For image uploading,
I am using Amazon Web Services S3.
