"""Final pass over every built page: structured data, social previews, lazy images.
Runs automatically at the end of areas.py (python3 areas.py rebuilds everything)."""
import json, re, pathlib

ROOT = pathlib.Path(__file__).parent
SITE = "https://www.glpxstudio.com/"
VERSION = "20261005f"
SKIP = {"index-v1.html", "index-v2.html", "artifact-index.html"}

BUSINESS = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "additionalType": "https://schema.org/Photographer",
    "name": "GLPX Studio",
    "url": SITE,
    "logo": SITE + "assets/img/logo-black.png",
    "image": SITE + "assets/img/br-director.jpg",
    "description": "Branding, headshot, editorial and corporate event photography in Orlando, FL. Sessions in English and Spanish.",
    "telephone": "+1-407-534-7581",
    "email": "glpxstudio@gmail.com",
    "address": {"@type": "PostalAddress", "addressLocality": "Orlando", "addressRegion": "FL", "addressCountry": "US"},
    "areaServed": ["Orlando", "Winter Park", "Lake Nona", "Downtown Orlando", "Baldwin Park", "Dr. Phillips", "Windermere",
                   "Thornton Park", "Kissimmee", "Winter Garden", "Altamonte Springs", "Lake Mary", "Sanford", "Oviedo", "Celebration"],
    "knowsLanguage": ["en", "es"],
    "sameAs": ["https://www.instagram.com/glpxstudio/"],
}
LD = '<script type="application/ld+json">' + json.dumps(BUSINESS, ensure_ascii=False) + "</script>\n"


def finish(path, url=None):
    html = path.read_text()
    name = path.name
    url = url or SITE + ("" if name == "index.html" else name)
    head_add = ""
    if "application/ld+json" not in html:
        head_add += LD
    if 'rel="canonical"' not in html:
        head_add += f'<link rel="canonical" href="{url}">\n'
    if "og:image" not in html:
        main = html.split("<main>", 1)[-1]
        m = re.search(r'<img src="(assets/img/(?!logo)[^"]+)"', main.split("<footer", 1)[0])
        img = SITE + (m.group(1) if m else "assets/img/og-home.jpg")
        if name == "index.html" and url == SITE:
            img = SITE + "assets/img/og-home.jpg"  # 1200x630 share card
            head_add += '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
        head_add += f'<meta property="og:image:alt" content="GLPX Studio, Orlando branding and headshot photography">\n'
        title = re.search(r"<title>(.*?)</title>", html, re.S).group(1)
        desc_m = re.search(r'<meta name="description" content="([^"]*)"', html)
        if 'property="og:title"' not in html:
            head_add += f'<meta property="og:title" content="{title}">\n'
            if desc_m:
                head_add += f'<meta property="og:description" content="{desc_m.group(1)}">\n'
        head_add += (f'<meta property="og:type" content="website">\n<meta property="og:url" content="{url}">\n'
                     f'<meta property="og:image" content="{img}">\n<meta property="og:site_name" content="GLPX Studio">\n'
                     f'<meta name="twitter:card" content="summary_large_image">\n')
    if 'rel="icon"' not in html:
        head_add += '<link rel="icon" href="assets/img/favicon.png">\n<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">\n'
    if head_add:
        html = html.replace("</head>", head_add + "</head>", 1)

    # Every booking button opens our own Book a Call page (calendar embedded there)
    html = re.sub(r'href="https://api\.leadconnectorhq\.com/widget/booking/[\w]+" target="_blank" rel="noopener"', 'href="book.html"', html)

    # Cache-bust stylesheets/scripts so phones load fixes right away (bump VERSION after style changes)
    html = re.sub(r'(assets/(?:style|v2|inner)\.css|assets/site\.js)(\?v=[\w.]+)?"', lambda m: m.group(1) + "?v=" + VERSION + '"', html)

    # Lazy-load every photo after the first two on the page (those are above the fold).
    before, sep, after = html.partition("<main>")
    if sep:
        count = 0
        def lazy(m):
            nonlocal count
            count += 1
            tag = m.group(0)
            if count <= 2 or "loading=" in tag:
                return tag
            return tag.replace("<img ", '<img loading="lazy" decoding="async" ', 1)
        after = re.sub(r"<img [^>]*>", lazy, after)
        html = before + sep + after
    path.write_text(html)


for p in sorted(ROOT.glob("*.html")):
    if p.name not in SKIP:
        finish(p)
print("finished pages")
