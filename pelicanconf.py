AUTHOR = 'Nicholas Carsner'
SITENAME = 'Somebody once asked me...'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("Carbon", "https://carbon.now.sh"),
)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/nicholascarsner"),
    ("GitHub", "https://github.com/ncarsner"),
)

DEFAULT_PAGINATION = 10

# Default category for posts without a category specified
DEFAULT_CATEGORY = 'Misc'

# Use directory names as categories (if you organize posts in subdirectories)
USE_FOLDER_AS_CATEGORY = True

# Manually specify menu items in desired order
DISPLAY_CATEGORIES_ON_MENU = False  # Disable automatic category menu
MENUITEMS = (
    ('Observer', '/category/observer.html'),
    ('User', '/category/user.html'),
    ('Student', '/category/student.html'),
    ('Teacher', '/category/teacher.html'),
    ('Philosopher', '/category/philosopher.html'),
)

# Generate empty category pages even if no posts exist
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', 'tags']

# Custom template variables for empty category messages
EMPTY_CATEGORY_MESSAGE = "No posts yet in this category. Check back soon!"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
