from datetime import datetime

AUTHOR = "Dioscoro Bondoy III"
SITEURL = "http://localhost:8000"
SITENAME = "Dioscoro III"
SITETITLE = "Dioscoro III"
SITESUBTITLE = "Dioscoro Random Thoughts"
SITEDESCRIPTION = "Dioscoro Random Thoughts"
SITELOGO = "images/profile.png"
# FAVICON = '/images/favicon.ico'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

ROBOTS = "index, follow"

THEME = "Flex"
PATH = "content"
OUTPUT_PATH = "blog/"
TIMEZONE = "Asia/Manila"

DISABLE_URL_HASH = True

# PLUGIN_PATHS = ['pelican-plugins']

# PLUGINS = ['i18n_subsites']

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

GITHUB_CORNER_URL = "https://github.com/dvbondoy"

SOCIAL = (
    ("github", "https://github.com/dvbondoy"),
    ("rss", "/blog/feeds/all.atom.xml"),
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

# CC_LICENSE = {
#     "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
#     "version": "4.0",
#     "slug": "by-sa",
#     "icon": True,
#     "language": "en_US",
# }

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

#DISQUS_SITENAME = "flex-pelican"
#ADD_THIS_ID = "ra-55adbb025d4f7e55"

STATIC_PATHS = ["images", "extra/ads.txt", "extra/CNAME"]

EXTRA_PATH_METADATA = {
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/CNAME": {"path": "CNAME"},
}

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True