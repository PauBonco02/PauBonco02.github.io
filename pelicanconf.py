AUTHOR = 'Pau Boncompte'
SITENAME = 'Pau Boncompte'
SITETITLE = 'Pau Boncompte'

'''
# For development
SITEURL = "http://localhost:8000"
RELATIVE_URLS = True
'''

# For production
SITEURL = "https://PauBonco02.github.io"
RELATIVE_URLS = False


SITELOGO = "/images/profileimage.JPG"
FAVICON = "/images/favicon.ico"
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

PATH = "content"
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'en'
THEME = "themes/Flex-master"
LOAD_CONTENT_CACHE = False

DISABLE_URL_HASH = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True
PAGE_ORDER_BY = 'order'

# Social widget
SOCIAL = (
    ('github', 'https://github.com/PauBonco02'),
    ('linkedin', 'https://www.linkedin.com/in/pau-boncompte-carre/'),
    ('instagram', 'https://www.instagram.com/pau.bonco/'),
    ('envelope', 'mailto:pauboncompte02@gmail.com'),
)

STATIC_PATHS = ['images', 'static','extra/custom.css']

USE_LESS = True

EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
}

CUSTOM_CSS = "static/custom.css"

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = False
THEME_COLOR_ENABLE_USER_OVERRIDE = False

DEFAULT_PAGINATION = 10

# Plugin settings
PLUGIN_PATHS = ['plugins']
PLUGINS = ['photos']

# --- pelican-photos settings ---
PHOTO_LIBRARY = "images/gallery" # Main folder for all galleries
PHOTO_GALLERY = (1024, 768, 80)           # (Max width, max height, quality)
PHOTO_ARTICLE = (760, 506, 80)            # For images in articles
PHOTO_THUMB = (192, 144, 60)              # For thumbnails in the grid
PHOTO_SQUARE_THUMB = True                # Set to True for square thumbnails
PHOTO_RESIZE_JOBS = 5                     # Number of CPU cores to use
PHOTO_LIGHTBOX_GALLERY_ATTR = "data-pswp-gallery" # Connects images to PhotoSwipe