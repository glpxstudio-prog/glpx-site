"""Blog posts, legal pages and redirects carried over from the old Pixpa site.
Old addresses are kept exactly (glpxstudio.com/blog/<slug>, /terms-and-conditions, /privacy-policy)
so Google keeps the rankings those pages already have.
Source text lives in _blog_src/*.md. Runs from areas.py after finish.py."""
import re, pathlib, html as H
import markdown
import build, finish
from build import page, closer, BOOK, ROOT

SITE = "https://www.glpxstudio.com/"
SRC = ROOT / "_blog_src"

# Newest first, same order as the old blog index
POSTS = [
    "how-much-do-headshots-cost-orlando",
    "studio-vs-on-location-headshots-orlando",
    "best-places-for-branding-photos-in-orlando",
    "branding-photos-vs-headshots",
    "what-to-wear-for-headshots-orlando",
    "actor-headshots-orlando-commercial-vs-theatrical",
    "how-to-choose-the-perfect-photographer",
    "your-local-guide-finding-the-best-photographer-in-orlando-near-me",
    "branding-photography-orlando-professional-services-to-elevate-your-business-brand",
    "essential-qualities-to-consider-when-hiring-an-orlando-photographer-for-your-next-shoot",
    "the-essential-role-of-digitals-in-your-modeling-career-why-you-need-them",
    "how-to-prepare-for-your-first-professional-photoshoot-a-photographers-guide",
    "why-professional-photography-matters-for-your-brand",
    "15-creative-poses-to-enhance-your-model-photography-portfolio",
]
TOPIC = {  # where each post should send readers next
    "how-much-do-headshots-cost-orlando": ("Headshots", "headshots.html"),
    "studio-vs-on-location-headshots-orlando": ("Team headshots", "corporate-headshots-orlando.html"),
    "best-places-for-branding-photos-in-orlando": ("Branding", "branding.html"),
    "branding-photos-vs-headshots": ("Branding", "branding.html"),
    "what-to-wear-for-headshots-orlando": ("Headshots", "headshots.html"),
    "actor-headshots-orlando-commercial-vs-theatrical": ("Headshots", "headshots.html"),
    "how-to-choose-the-perfect-photographer": ("Branding", "branding.html"),
    "your-local-guide-finding-the-best-photographer-in-orlando-near-me": ("Headshots", "headshots.html"),
    "branding-photography-orlando-professional-services-to-elevate-your-business-brand": ("Branding", "branding.html"),
    "essential-qualities-to-consider-when-hiring-an-orlando-photographer-for-your-next-shoot": ("Headshots", "headshots.html"),
    "the-essential-role-of-digitals-in-your-modeling-career-why-you-need-them": ("Editorial", "editorial.html"),
    "how-to-prepare-for-your-first-professional-photoshoot-a-photographers-guide": ("Branding", "branding.html"),
    "why-professional-photography-matters-for-your-brand": ("Branding", "branding.html"),
    "15-creative-poses-to-enhance-your-model-photography-portfolio": ("Editorial", "editorial.html"),
}
REL = re.compile(r'((?:href|src)=")(?!https?:|mailto:|tel:|sms:|#|/|data:)')


def read(slug):
    raw = (SRC / f"{slug}.md").read_text().strip("\n")
    lines = raw.split("\n")
    title = lines[0].lstrip("# ").strip()
    date = lines[1].split(":", 1)[1].strip() if lines[1].startswith("date:") else ""
    body = "\n".join(lines[2:]).strip()
    return title, date, body


def to_html(md):
    out = markdown.markdown(md, extensions=["tables", "sane_lists"])
    out = re.sub(r"<h1>(.*?)</h1>", r"<h2>\1</h2>", out)  # one h1 per page
    return out


def excerpt(md, n=28):
    for para in md.split("\n\n"):
        p = para.strip()
        if p and not p.startswith(("#", "-", "|", "*", "1.")):
            words = re.sub(r"[*_`]", "", p).split()
            return " ".join(words[:n]) + ("…" if len(words) > n else "")
    return ""


def write_nested(path_rel, title, desc, body, extra_head=""):
    """Build with the shared template, run the final pass, then move into a folder so the old URL works."""
    tmp = ROOT / "_tmp_page.html"
    page(tmp.name, title, desc, body, extra_head)
    url = SITE + path_rel
    finish.finish(tmp, url)
    html = tmp.read_text()
    tmp.unlink()
    depth = path_rel.rstrip("/").count("/") + 1
    html = REL.sub(lambda m: m.group(1) + "../" * depth, html)
    html = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', html)
    dest = ROOT / path_rel / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html)


def article_ld(title, date, desc, url):
    import json
    return ('<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "BlogPosting", "headline": title,
        "datePublished": date, "description": desc, "mainEntityOfPage": url,
        "author": {"@type": "Person", "name": "Gerson Lopez"},
        "publisher": {"@type": "Organization", "name": "GLPX Studio", "logo": {"@type": "ImageObject", "url": SITE + "assets/img/logo-black.png"}},
        "image": SITE + "assets/img/br-director.jpg",
    }, ensure_ascii=False) + "</script>\n")


# ------------------------------------------------------------------ posts
index_rows = []
for i, slug in enumerate(POSTS):
    title, date, md = read(slug)
    desc = H.escape(excerpt(md, 26).replace('"', "'"), quote=True)
    topic, topic_href = TOPIC[slug]
    nxt = POSTS[(i + 1) % len(POSTS)]
    nxt_title = read(nxt)[0]
    body = f'''  <section class="page-hero post-hero">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow"><a href="blog/index.html">Journal</a> · {date}</p>
        <h1>{title}</h1>
        <p class="post-by">By Gerson Lopez · GLPX Studio, Orlando FL</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap post-wrap">
      <article class="post">
{to_html(md)}
      </article>
      <aside class="post-side">
        <p class="eyebrow">Work with GLPX</p>
        <h3>Photos that do some of the selling.</h3>
        <p>Branding, headshot, editorial and event photography across Orlando. Every shoot is quoted after a free call.</p>
        <a class="btn btn--red" href="{BOOK}" target="_blank" rel="noopener">Book a free call</a>
        <a class="btn btn--ghost" href="{topic_href}">See {topic.lower()} work</a>
      </aside>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap post-next">
      <p class="eyebrow">Next in the journal</p>
      <h2><a href="blog/{nxt}/index.html">{nxt_title}</a></h2>
      <p><a href="blog/index.html">All posts →</a></p>
    </div>
  </section>

{closer("Ready when <em>you</em> are.")}'''
    url = f"{SITE}blog/{slug}/"
    write_nested(f"blog/{slug}", f"{title} · GLPX Studio", desc, body,
                 '<meta property="og:type" content="article">\n' + article_ld(title, date, desc, url))
    index_rows.append(f'''      <a class="post-row" href="blog/{slug}/index.html">
        <span class="kicker">{date}</span>
        <h3>{title}</h3>
        <p>{excerpt(md, 30)}</p>
      </a>''')

blog_index = f'''  <section class="page-hero post-hero">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">The GLPX journal</p>
        <h1>Notes from <em>behind the camera.</em></h1>
        <p class="lede">Guides on hiring a photographer in Orlando, getting ready for a shoot, and making your photos work for your brand.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap post-list">
{chr(10).join(index_rows)}
    </div>
  </section>

{closer("Have a shoot <em>in mind?</em>")}'''
write_nested("blog", "Journal · Photography Guides from GLPX Studio, Orlando",
             "Photography guides from GLPX Studio in Orlando: choosing a photographer, preparing for a shoot, branding photos, headshots and model digitals.",
             blog_index)

# ------------------------------------------------------------------ legal
for slug, label in [("terms-and-conditions", "Terms &amp; conditions"), ("privacy-policy", "Privacy policy")]:
    title, date, md = read(slug)
    body = f'''  <section class="page-hero post-hero">
    <div class="wrap"><div class="hero-copy">
      <p class="eyebrow">Legal · Last updated {date}</p>
      <h1>{label}</h1>
    </div></div>
  </section>
  <section class="section">
    <div class="wrap"><article class="post post--legal">
{to_html(md)}
    </article></div>
  </section>'''
    write_nested(slug, f"{title} · GLPX Studio", f"{H.unescape(label)} for GLPX Studio photography services in Orlando, FL.", body)

# ------------------------------------------------------------------ redirects from old Pixpa addresses
REDIRECTS = {
    "headshot": "headshots.html",
    "about-us": "about.html",
    "contact-us": "contact.html",
    "services": "index.html",
    "portfolio": "portfolio.html",
    "fashion-editorial": "editorial.html",
    "proofing": "client-gallery.html",
    "thank-you-page": "contact.html",
    "easter-photos": "branding.html",
    "home": "index.html",
    "homepage": "index.html",
    "newsletter": "index.html",
}
# Old Pixpa comment pages for each blog post (Search Console shows these as 404)
for s in POSTS:
    REDIRECTS[f"blog-post-comments/{s}"] = f"blog/{s}/"
for old, new in REDIRECTS.items():
    target = SITE + ("" if new == "index.html" else new)
    up = "../" * (old.count("/") + 1)
    d = ROOT / old
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Moved · GLPX Studio</title>
<link rel="canonical" href="{target}">
<meta name="robots" content="noindex, follow">
<meta http-equiv="refresh" content="0; url={up}{new}">
<script>location.replace("{up}{new}" + location.hash)</script>
</head><body><p>This page moved to <a href="{up}{new}">{target}</a>.</p></body></html>
''')

# ------------------------------------------------------------------ sitemap additions
sm = (ROOT / "sitemap.xml").read_text()
extra = [f"blog/{s}/" for s in POSTS] + ["blog/", "terms-and-conditions/", "privacy-policy/"]
add = "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in extra if f"{SITE}{u}<" not in sm)
(ROOT / "sitemap.xml").write_text(sm.replace("</urlset>", add + "</urlset>"))
print("blog posts:", len(POSTS), "redirects:", len(REDIRECTS))
