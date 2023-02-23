from datetime import datetime

AUTHOR = 'dvbondoy'
SITENAME = 'Dioscoro III'
SITEURL = 'https://dvbondoy.github.io'
SITETITLE = "Dioscoro III"
SITESUBTITLE = "Random Thoughts"
SITEDESCRIPTION = "Dioscoro Random Thoughts"
SITELOGO = "images/profile.png"

BROWSER_COLOR = "#333"
ROBOTS = "index, follow"

THEME="Flex"
PATH = 'content'

TIMEZONE = 'Asia/Manila'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Portfolio', 'https://dvbondoy.github.io/portfolio/'),
         ('TryHackme', 'https://tryhackme.com/p/dvbondoy/'),
         ('FreeCodeCamp', 'https://www.freecodecamp.org/certification/fcc6df760fa-6dda-4303-ae2a-070af6bcae9d/responsive-web-design/'),)

# Social widget
GITHUB_CORNER_URL = "https://github.com/dvbondoy"

SOCIAL = (
    ("github", "https://github.com/dvbondoy"),
    # ("rss", "/feeds/all.atom.xml"),
    ("linkedin", "https://www.linkedin.com/in/dioscoro-bondoy-385285249/"),
)

MAIN_MENU = True

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("About Me", "/about-me.html"),
)

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True