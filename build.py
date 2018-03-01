from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader = FileSystemLoader("templates"),
    autoescape = select_autoescape(['html', 'xml'])
)

def getYear():
    import datetime
    return datetime.datetime.now().year

page_vars = {
    "title" : "CRYPTOGEARZ | High-Quality Cryptocurrency clothing, accessories, and gear!",
    "author" : "CRYPTOGEARZ",
    "description": "We sell high-quality cryptocurrency related gear, clothing, and gear!",
    "keywords": "bitcoin,cryptogears,cryptogearz,ethereum,litecoin,ripple,iota,neo,cryptocurrency,clothing,gear",
    "social" : {
        "twitter" : "https://twitter.com/cryptogearz_",
        "instagram": "https://www.instagram.com/cryptogearz",
        "email": "cryptogearz1@gmail.com",
        "gpg": "public.key.txt",
    },
    "shop": "https://inktale.com/a/cryptogearz",
    "year" : getYear(),
}

# Index
index = env.get_template('index.html')
with open("index.html", "w") as f:
    f.write(index.render(page_vars))

# Colophone
colophon = env.get_template('colophon.html')
with open("colophon.html", "w") as f:
    f.write(colophon.render(page_vars))
